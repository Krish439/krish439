from asyncio import sleep

from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)
from telethon.utils import get_display_name

from userbot import legend

from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers import media_type
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper.globals import gvarstatus
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, main_pic

# =================== STRINGS ============
PP_TOO_SMOL = "`ये तस्वीर बोहोत छोटी है।`"
PP_ERROR = "`प्रोसेसिंग के वक्त फेल हो गया।`"
NO_ADMIN = "`अबे नुबड़े में एडमिन नही हु`"
NO_PERM = "`मेरे पास इतनी क्षमता नहीं है। बोहोत बुरा हुआ`"
CHAT_PP_CHANGED = "`फोटो चेंज हो गया भाई।`"
INVALID_MEDIA = "`ये वेलिड नही है।`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

ADMIN_PIC = gvarstatus("ADMIN_PIC")
if ADMIN_PIC:
    LEGEND = [x for x in NORMAL_PIC.split()]
    PIC = list(LEGEND)
    help_pic = random.choice(PIC)
else:
    help_pic = main_pic

LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

menu_category = "admin"
# ================================================


@legend.legend_cmd(
    pattern="gpic( -s| -d)$",
    command=("gpic", menu_category),
    info={
        "header": "ग्रुप का फोटो बदलने के लिए अथवा फोटो लगाने के लिए",
        "description": "फोटो को रिप्लाई करके इस कमांड को उसे करे।",
        "flags": {
            "-s": "ग्रुप फोटो सेट करने के लिए",
            "-d": "ग्रुप फोटो डिलीट करने के लिए",
        },
        "usage": [
            "{tr}gpic -s <reply to image>",
            "{tr}gpic -d",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def set_group_photo(event):  # sourcery no-metrics
    "ग्रुप फोटो चेंज करने के लिए"
    type = (event.pattern_match.group(1)).strip()
    if type == "-s":
        replymsg = await event.get_reply_message()
        photo = None
        if replymsg and replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await event.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split("/"):
                photo = await event.client.download_file(replymsg.media.document)
            else:
                return await eod(event, INVALID_MEDIA)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await bot.send_file(
                    event.chat_id,
                    help_pic,
                    caption=f"⚜ `ग्रुप फोटो चेंज हो गया` ⚜\n🔰 चैट ~ {gpic.chat.title}",
                )
            except PhotoCropSizeSmallError:
                return await eod(event, PP_TOO_SMOL)
            except ImageProcessFailedError:
                return await eod(event, PP_ERROR)
            except Exception as e:
                return await eod(event, f"**Error : **`{str(e)}`")
            process = "updated"
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await eod(event, f"**Error : **`{e}`")
        process = "deleted"
        await eod(event, "```ग्रुप फोटो डिलीट कर दिया.```")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#GROUPPIC\n"
            f"Group profile pic {process} successfully "
            f"CHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@legend.legend_cmd(
    pattern="promote(?:\s|$)([\s\S]*)",
    command=("promote", menu_category),
    info={
        "header": "किसी को एडमिन बनाने के लिए",
        "description": "किसी यूज़र को एडमिन बनाने के लिए\
            \nNote : तुम्हारे पास उतनी राइट्स होनी चाहिए",
        "usage": [
            "{tr}promote <userid/username/reply>",
            "{tr}promote <userid/username/reply> <custom title>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def promote(event):
    "To promote a person in chat"
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(event, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "ℓєgєи∂"
    if not user:
        return
    legendevent = await eor(event, "`प्रोमोटिंग...`")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await legendevent.edit(NO_PERM)
    await bot.send_file(
        event.chat_id,
        "https://te.legra.ph/file/74530a36e7b5e60ced878.jpg",
        caption=f"**⚜प्रोमोटेड ~** [{user.first_name}](tg://user?id={user.id})⚜\n**सफलतापूर्वक ** ~ `{event.chat.title}`!! \n**एडमिन का टैग ~**  `{rank}`",
    )
    await event.delete()
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#PROMOTE\
            \nUSER: [{user.first_name}](tg://user?id={user.id})\
            \nCHAT: {get_display_name(await event.get_chat())} (`{event.chat_id}`)",
        )


@legend.legend_cmd(
    pattern="demote(?:\s|$)([\s\S]*)",
    command=("demote", menu_category),
    info={
        "header": "किसी को एडमिन से हटाने के लिए",
        "description": "किसी यूज़र को एडमिन से हटाने के लिए\
            \nNote : आपको इसके लिए उचित अधिकारों की आवश्यकता है और आपको उस व्यक्ति का प्रचार करने वाले स्वामी या व्यवस्थापक भी होने चाहिए।आपको इसके लिए उचित अधिकारों की आवश्यकता है और आपको उस व्यक्ति का प्रचार करने वाले स्वामी या व्यवस्थापक भी होने चाहिए",
        "usage": [
            "{tr}demote <userid/username/reply>",
            "{tr}demote <userid/username/reply> <custom title>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def demote(event):
    "To demote a person in group"
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, NO_ADMIN)
        return
    user, _ = await get_user_from_event(event)
    if not user:
        return
    legendevent = await eor(event, "`डेमोटिंग ...`")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    rank = "????"
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await legendevent.edit(NO_PERM)
    await bot.send_file(
        event.chat_id,
        help_pic,
        caption=f"डेमोटेड \nUser:[{user.first_name}](tg://{user.id})\n चैट: {event.chat.title}",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#DEMOTE\
            \nUSER: [{user.first_name}](tg://user?id={user.id})\
            \nCHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@legend.legend_cmd(
    pattern="ban(?:\s|$)([\s\S]*)",
    command=("ban", menu_category),
    info={
        "header": "यूज़र को बेन करने के लिए",
        "description": "उस यूज़र को परमानेंट बन करने के लिए\
            \nनोट : तुम्हारे पास इतनी राइट्स होनी चाहिए.",
        "usage": [
            "{tr}ban <userid/username/reply>",
            "{tr}ban <userid/username/reply> <reason>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _ban_person(event):
    "किसी को बन करने के लिए"
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == event.client.uid:
        return await eod(event, "__खुद को बेन नही कर सकते!!.__")
    legendevent = await eor(event, "`बेन हो रहा है..!`")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await legendevent.edit(NO_PERM)
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await legendevent.edit(
            "`मेरे पास मैसेज डिलीट करने की राइट्स नही है! लेकिन फिर भी बेन हो गया!`"
        )
    if reason:
        await bot.send_file(
            event.chat_id,
            help_pic,
            caption=f"{_format.mentionuser(user.first_name ,user.id)}` बेन हो गया !!`\n**कारण : **`{reason}`",
        )
    else:
        await bot.send_file(
            event.chat_id,
            help_pic,
            caption=f"{_format.mentionuser(user.first_name ,user.id)} `बेन हो गया !!`",
        )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#BAN\
                \nयूज़र: [{user.first_name}](tg://user?id={user.id})\
                \nचैट: {get_display_name(await event.get_chat())}(`{event.chat_id}`)\
                \nकारण : {reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#BAN\
                \nयूज़र: [{user.first_name}](tg://user?id={user.id})\
                \nचैट: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@legend.legend_cmd(
    pattern="unban(?:\s|$)([\s\S]*)",
    command=("unban", menu_category),
    info={
        "header": "Will unban the guy in the group where you used this command.",
        "description": "Removes the user account from the banned list of the group\
            \nNote : You need proper rights for this.",
        "usage": [
            "{tr}unban <userid/username/reply>",
            "{tr}unban <userid/username/reply> <reason>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def nothanos(event):
    "To unban a person"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    legendevent = await eor(event, "`Unbanning...`")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await legendevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} `is Unbanned Successfully. Granting another chance.`"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )
    except UserIdInvalidError:
        await legendevent.edit("`Uh oh my unban logic broke!`")
    except Exception as e:
        await legendevent.edit(f"**Error :**\n`{e}`")


@legend.legend_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@legend.legend_cmd(
    pattern="mute(?:\s|$)([\s\S]*)",
    command=("mute", menu_category),
    info={
        "header": "To stop sending messages from that user",
        "description": "If is is not admin then changes his permission in group,\
            if he is admin or if you try in personal chat then his messages will be deleted\
            \nNote : You need proper rights for this.",
        "usage": [
            "{tr}mute <userid/username/reply>",
            "{tr}mute <userid/username/reply> <reason>",
        ],
    },  # sourcery no-metrics
)
async def startmute(event):
    "To mute a person in that paticular chat"
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await sleep(2)
        await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "`This user is already muted in this chat ~~lmfao sed rip~~`"
            )
        if event.chat_id == legend.uid:
            return await eod(event, "`You cant mute yourself`")
        try:
            mute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**Error **\n`{e}`")
        else:
            await event.edit("`Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **`")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#PM_MUTE\n"
                f"**User :** [{replied_user.user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await eor(
                event, "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
            )
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == legend.uid:
            return await eor(event, "`Sorry, I can't mute myself`")
        if is_muted(user.id, event.chat_id):
            return await eor(
                event, "`This user is already muted in this chat ~~lmfao sed rip~~`"
            )
        result = await event.client.get_permissions(event.chat_id, user.id)
        try:
            if result.participant.banned_rights.send_messages:
                return await eor(
                    event,
                    "`This user is already muted in this chat ~~lmfao sed rip~~`",
                )
        except AttributeError:
            pass
        except Exception as e:
            return await eor(event, f"**Error : **`{e}`", 10)
        try:
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await eor(
                        event,
                        "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`",
                    )
            elif "creator" not in vars(chat):
                return await eor(
                    event, "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
                )
            mute(user.id, event.chat_id)
        except Exception as e:
            return await eor(event, f"**Error : **`{e}`", 10)
        if reason:
            await eor(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is muted in {get_display_name(await event.get_chat())}`\n"
                f"`Reason:`{reason}",
            )
        else:
            await eor(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is muted in {get_display_name(await event.get_chat())}`\n",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#MUTE\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@legend.legend_cmd(
    pattern="unmute(?:\s|$)([\s\S]*)",
    command=("unmute", menu_category),
    info={
        "header": "To allow user to send messages again",
        "description": "Will change user permissions ingroup to send messages again.\
        \nNote : You need proper rights for this.",
        "usage": [
            "{tr}unmute <userid/username/reply>",
            "{tr}unmute <userid/username/reply> <reason>",
        ],
    },
)
async def endmute(event):
    "To mute a person in that paticular chat"
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await sleep(1)
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        if not is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "`__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）`"
            )
        try:
            unmute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**Error **\n`{e}`")
        else:
            await event.edit(
                "`Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍`"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#PM_UNMUTE\n"
                f"**User :** [{replied_user.user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        user, _ = await get_user_from_event(event)
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client.get_permissions(event.chat_id, user.id)
                if result.participant.banned_rights.send_messages:
                    await event.client(
                        EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                    )
        except AttributeError:
            return await eor(
                event,
                "`This user can already speak freely in this chat ~~lmfao sed rip~~`",
            )
        except Exception as e:
            return await eor(event, f"**Error : **`{e}`")
        await eor(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} `is unmuted in {get_display_name(await event.get_chat())}\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍`",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNMUTE\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@legend.legend_cmd(
    pattern="kick(?:\s|$)([\s\S]*)",
    command=("kick", menu_category),
    info={
        "header": "To kick a person from the group",
        "description": "Will kick the user from the group so he can join back.\
        \nNote : You need proper rights for this.",
        "usage": [
            "{tr}kick <userid/username/reply>",
            "{tr}kick <userid/username/reply> <reason>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def endmute(event):
    "use this to kick a user from chat"
    user, reason = await get_user_from_event(event)
    if not user:
        return
    legendevent = await eor(event, "`Kicking...`")
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except Exception as e:
        return await legendevent.edit(NO_PERM + f"\n{e}")
    if reason:
        await legendevent.edit(
            f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await legendevent.edit(
            f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`"
        )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)\n",
        )


@legend.legend_cmd(
    pattern="pin( loud|$)",
    command=("pin", menu_category),
    info={
        "header": "For pining messages in chat",
        "description": "reply to a message to pin it in that in chat\
        \nNote : You need proper rights for this if you want to use in group.",
        "options": {"loud": "To notify everyone without this it will pin silently"},
        "usage": [
            "{tr}pin <reply>",
            "{tr}pin loud <reply>",
        ],
    },
)
async def pin(event):
    "To pin a message in chat"
    to_pin = event.reply_to_msg_id
    if not to_pin:
        return await eod(event, "`Reply to a message to pin it.`", 5)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await eod(event, NO_PERM, 5)
    except Exception as e:
        return await eod(event, f"`{e}`", 5)
    await eod(event, "`Pinned Successfully!`", 3)
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#PIN\
                \n__successfully pinned a message in chat__\
                \nCHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)\
                \nLOUD: {is_silent}",
        )


@legend.legend_cmd(
    pattern="unpin( all|$)",
    command=("unpin", menu_category),
    info={
        "header": "For unpining messages in chat",
        "description": "reply to a message to unpin it in that in chat\
        \nNote : You need proper rights for this if you want to use in group.",
        "options": {"all": "To unpin all messages in the chat"},
        "usage": [
            "{tr}unpin <reply>",
            "{tr}unpin all",
        ],
    },
)
async def pin(event):
    "To unpin message(s) in the group"
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        return await eod(
            event,
            "__Reply to a message to unpin it or use __`.unpin all`__ to unpin all__",
            5,
        )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "all":
            await event.client.unpin_message(event.chat_id)
        else:
            return await eod(
                event, "`Reply to a message to unpin it or use .unpin all`", 5
            )
    except BadRequestError:
        return await eod(event, NO_PERM, 5)
    except Exception as e:
        return await eod(event, f"`{e}`", 5)
    await eod(event, "`Unpinned Successfully!`", 3)
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#UNPIN\
                \n__successfully unpinned message(s) in chat__\
                \nCHAT: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@legend.legend_cmd(
    pattern="undlt( -u)?(?: |$)(\d*)?",
    command=("undlt", menu_category),
    info={
        "header": "हालही में डिलीट मैसेज को देखने के लिए",
        "description": "हाल ही में डिलीट किए गए मैसेज को देखने के लिए, डिफॉल्ट रूप से सिर्फ 5 मैसेज शो होंगे. आप 1 से 15 के बीच में मैसेज देख सकते हो.",
        "flags": {
            "u": "use this type to upload media to chat else will just show as media."
        },
        "usage": [
            "{tr}undlt <count>",
            "{tr}undlt -u <count>",
        ],
        "examples": [
            "{tr}undlt 7",
            "{tr}undlt -u 7 (इससे आपको 7 मैसेज मिलेंगे इसको रिप्लाई करते हुए",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _iundlt(event):  # sourcery no-metrics
    "ग्रुप के डिलीट मैसेज देखने के लिए"
    legendevent = await eor(event, "`सर्च जारी है .....`")
    type = event.pattern_match.group(1)
    if event.pattern_match.group(2) != "":
        lim = int(event.pattern_match.group(2))
        if lim > 15:
            lim = int(15)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(5)
    adminlog = await event.client.get_admin_log(
        event.chat_id, limit=lim, edit=False, delete=True
    )
    deleted_msg = f"⚜ **समूह में {lim} हाल ही में डिलीट किए गए है:~** ⚜"
    if not type:
        for msg in adminlog:
            sweet = (
                await event.client(GetFullUserRequest(id=msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                deleted_msg += f"\n☞ __{msg.old.message}__ **इसने भेजा** {_format.mentionuser(sweet.first_name ,sweet.id)}"
            else:
                deleted_msg += f"\n☞ __{_media_type}__ **इसने भेजा** {_format.mentionuser(sweet.first_name ,sweet.id)}"
            await eor(legendevent, deleted_msg)
    else:
        main_msg = await eor(legendevent, deleted_msg)
        for msg in adminlog:
            sweet = (
                await event.client(GetFullUserRequest(id=msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(
                    f"{msg.old.message}\n**इसने भेजा** {_format.mentionuser(sweet.first_name ,sweet.id)}"
                )
            else:
                await main_msg.reply(
                    f"{msg.old.message}\n**इसने भेजा** {_format.mentionuser(sweet.first_name ,sweet.id)}",
                    file=msg.old.media,
                )
