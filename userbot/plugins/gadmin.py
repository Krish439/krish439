import asyncio
from datetime import datetime
import asyncio
import random

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights, MessageEntityMentionName

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from userbot import legend

from ..core.managers import eod, eor
from ..helpers.utils import _format
from ..sql_helper.gban_sql_helper import (
    all_gbanned,
    gbaner,
    is_gbanned,
    ungbaner,
)
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event, gban_pic, mention
from ..sql_helper.globals import gvarstatus 

menu_category = "admin"

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

async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await eor(event, "Need a user to do this...")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await eor(event, f"**ERROR !!**\n\n`{str(err)}`")
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj




@legend.legend_cmd(
    pattern="gpromote(?:\s|$)([\s\S]*)",
    command=("gpromote", menu_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}gpromote <username/reply/userid> <reason (optional)>",
    },
)
async def _(legendevent):
    i = 0
    await legendevent.get_sender()
    me = await legendevent.client.get_me()
    legend = await eor(legendevent, "`Promoting globally...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await legendevent.get_chat()
    if legendevent.is_private:
        user = legendevent.chat
        rank = legendevent.pattern_match.group(1)
    else:
        legendevent.chat.title
    try:
        user, rank = await get_full_user(legendevent)
    except:
        pass
    if me == user:
        await legend.edit("You can't promote yourself...")
        return
    try:
        if not rank:
            rank = "ℓεɠεɳ∂"
    except:
        return await legend.edit("**ERROR !!**")
    if user:
        telchanel = [
            d.entity.id
            for d in await legendevent.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=True,
            invite_users=True,
            change_info=Tru,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
        )
        for x in telchanel:
            try:
                await legendevent.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await legend.edit(f"**Promoting User in :**  `{i}` Chats...")
            except:
                pass
    else:
        await legend.edit(f"**Reply to a user !!**")
    await legend.edit(
        f"[{user.first_name}](tg://user?id={user.id}) **Was Promoted Globally In** `{i}` **Chats !!**"
    )
    await event.client.send_message(
        BOTLOG_CHATID,
        f"#GPROMOTE \n\n**Globally Promoted User :** [{user.first_name}](tg://user?id={user.id}) \n\n**Total Chats :** `{i}`",
    )



@legend.legend_cmd(
    pattern="gdemote(?:\s|$)([\s\S]*)",
    command=("gdemote", menu_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}gdemote <username/reply/userid> <reason (optional)>",
    },
)
async def _(legendevent):
    i = 0
    await legendevent.get_sender()
    me = await legendevent.client.get_me()
    legend = await eor(legendevent, "`Demoting Globally...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await legendevent.get_chat()
    if legendevent.is_private:
        user = legendevent.chat
        rank = legendevent.pattern_match.group(1)
    else:
        legendevent.chat.title
    try:
        user, rank = await get_full_user(legendevent)
    except:
        pass
    if me == user:
        await legend.edit("You can't Demote yourself !!")
        return
    try:
        if not rank:
            rank = "legend"
    except:
        return await legend.edit("**ERROR !!**")
    if user:
        telchanel = [
            d.entity.id
            for d in await legendevent.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None,
        )
        for x in telchanel:
            try:
                await legendevent.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await legend.edit(f"**Demoting Globally In Chats :** `{i}`")
            except:
                pass
    else:
        await legend.edit(f"**Reply to a user !!**")
    await legend.edit(
        f"[{user.first_name}](tg://user?id={user.id}) **Was Demoted Globally In** `{i}` **Chats !!**"
    )
    await event.client.send_message(
        BOTLOG_CHATID,
        f"#GDEMOTE \n\n**Globally Demoted :** [{user.first_name}](tg://user?id={user.id}) \n\n**Total Chats :** `{i}`",
    )



@legend.legend_cmd(
    pattern="gban(?:\s|$)([\s\S]*)",
    command=("gban", menu_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def lolgban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    legend = await eor(event, "`Gbanning...`")
    reason = ""
    await event.get_reply_message()
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
        try:
            reason = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    elif event.pattern_match.group(1):
        usr = event.text.split(" ", maxsplit=2)[1]
        userid = await get_user_id(usr)
        try:
            reason = event.text.split(" ", maxsplit=2)[2]
        except IndexError:
            reason = ""
    elif event.is_private:
        userid = (await event.get_chat()).id
        try:
            reason = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    else:
        return await eod(
            legend, "**To gban a user i need a userid or reply to his/her message!!**"
        )
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if str(userid) == 5122474448:
        return await eod(legend, "🥴 **Nashe me hai kya lawde ‽**")
    if is_gbanned(userid):
        return await eor(
            legend,
            "This kid is already gbanned and added to my **Gban Watch!!**",
        )
    async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
            try:
                await event.client.edit_permissions(
                    gfuck.id, userid, view_messages=False
                )
                chats += 1
                await legend.edit(f"**Gbanning...** \n**Chats :** __{chats}__")
            except BaseException:
                pass
    gbaner(userid)
    a = gvarstatus("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = []
        for d in b:
            c.append(d)
        gbpic = random.choice(c)
    else:
        gbpic = gban_pic
    gmsg = f"🥴 [{name}](tg://user?id={userid}) **Gbanned** By {mention} \n\n📍 Added to Gban Watch!!\n**🔰 Total Chats :**  `{chats}`"
    if reason != "":
        gmsg += f"\n**🔰 Reason :**  `{reason}`"
    ogmsg = f"[{name}](tg://user?id={userid}) **Is now GBanned by** {mention} **in**  `{chats}`  **Chats!! 😏**\n\n**📍 Also Added to Gban Watch!!**"
    if reason != "":
        ogmsg += f"\n**🔰 Reason :**  `{reason}`"
    if gvarstatus("ABUSE") == "ON":
        await event.client.send_file(event.chat_id, gbpic, caption=gmsg)
        await legend.delete()
    else:
        await legend.edit(ogmsg)
    if reason:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#GBAN\
            \nGlobal Ban\
            \n**User : **[{name}](tg://user?id={userid})\
            \n**ID : **`{userid}`\
            \n**Reason :** `{reason}`\
            \n__Banned in {chats} groups__"
        )
    else:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#GBAN\
            \nGlobal Ban\
            \n**User : **[{name}](tg://user?id={userid})\
            \n**ID : **`{userid}`\
            \n__Banned in {chats} groups__"
        )
    try:
        if reply:
            await reply.forward_to(BOTLOG_CHATID)
            await reply.delete()
    except BadRequestError:
        pass


@legend.legend_cmd(
    pattern="ungban(?:\s|$)([\s\S]*)",
    command=("ungban", menu_category),
    info={
        "header": "To unban the person from every group where you are admin.",
        "description": "will unban and also remove from your gbanned list.",
        "usage": "{tr}ungban <username/reply/userid>",
    },
)
async def lolgban(event):
    "To unban the person from every group where you are admin."
    legend = await eor(event, "`Ungban in progress...`")
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        userid = await get_user_id(event.pattern_match.group(1))
    elif event.is_private:
        userid = (await event.get_chat()).id
    else:
        return await eor(legend, "`Reply to a user or give their userid... `")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if not is_gbanned(userid):
        return await eor(legend, "`User is not gbanned.`")
    async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
            try:
                await event.client.edit_permissions(
                    gfuck.id, userid, view_messages=True
                )
                chats += 1
                await legend.edit(
                    f"**Ungban in progress...** \n**Chats :** __{chats}__"
                )
            except BaseException:
                pass
    ungbaner(userid)
    await legend.edit(
        f"📍 [{name}](tg://user?id={userid}) **is now Ungbanned from `{chats}` chats and removed from Gban Watch!!**",
    )
    await event.client.send_message(
        BOTLOG_CHATID,
        f"#UNGBAN\
        \nGlobal Unban
        \n**User : **[{name}](tg://user?id={userid})\
        \n**ID : **`{userid}`\
        \n__Unbanned in {chats} groups__"
         )


@legend.legend_cmd(
    pattern="listgban$",
    command=("listgban", menu_category),
    info={
        "header": "Shows you the list of all gbanned users by you.",
        "usage": "{tr}listgban",
    },
)
async def gablist(event):
    "Shows you the list of all gbanned users by you."
    hmm = await eor(event, "`Fetching Gbanned users...`")
    gbanned_users = all_gbanned()
    GBANNED_LIST = "**Gbanned Users :**\n"
    if len(gbanned_users) > 0:
        for user in gbanned_users:
            hel = user.chat_id
            legend = int(hel)
            try:
                tity = await event.client.get_entity(legend)
                name = tity.first_name
            except ValueError:
                name = "User"
            GBANNED_LIST += f"📍 [{name}](tg://user?id={legend}) (`{legend}`)\n"
    else:
        GBANNED_LIST = "No Gbanned Users!!"
    await hmm.edit(GBANNED_LIST)


@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if is_gbanned(str(user.id)):
            if chat.admin_rights:
                try:
                    await event.client.edit_permissions(
                        chat.id,
                        user.id,
                        view_messages=False,
                    )
                    gban_watcher = f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n**⚜️ Victim Id :**  [{user.first_name}](tg://user?id={user.id})\n"
                    gban_watcher += (
                        f"**🔥 Action 🔥**  \n`Banned this piece of shit....` **AGAIN!**"
                    )
                    await event.reply(gban_watcher)
                except BaseException:
                    pass



@legend.legend_cmd(
    pattern="gmute(?:\s|$)([\s\S]*)",
    command=("gmute", menu_category),
    info={
        "header": "To mute a person in all groups where you are admin.",
        "description": "It doesnt change user permissions but will delete all messages sent by him in the groups where you are admin including in private messages.",
        "usage": "{tr}gmute username/reply> <reason (optional)>",
    },
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == legend.uid:
            return await eor(event, "`Sorry, I can't gmute myself`")
        elif user.id == 5122474448:
            return await eor(event, "`Nashe Me H Kya Lawde`")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await eor(event, "`Sorry. I am unable to fetch the user`")
    if is_muted(userid, "gmute"):
        return await eor(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} ` is already gmuted`",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await eor(event, f"**Error**\n`{e}`")
    else:
        if reason:
            await eor(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully gmuted`\n**Reason :** `{reason}`",
            )
        else:
            await eor(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully gmuted`",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


@legend.legend_cmd(
    pattern="ungmute(?:\s|$)([\s\S]*)",
    command=("ungmute", menu_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == legend.uid:
            return await eor(event, "`Sorry, I can't gmute myself`")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await eor(event, "`Sorry. I am unable to fetch the user`")
    if not is_muted(userid, "gmute"):
        return await eor(
            event, f"{_format.mentionuser(user.first_name ,user.id)} `is not gmuted`"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await eor(event, f"**Error**\n`{e}`")
    else:
        if reason:
            await eor(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully ungmuted`\n**Reason :** `{reason}`",
            )
        else:
            await eor(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully ungmuted`",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


@legend.legend_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


@legend.legend_cmd(
    pattern="gkick(?:\s|$)([\s\S]*)",
    command=("gkick", menu_category),
    info={
        "header": "kicks the person in all groups where you are admin.",
        "usage": "{tr}gkick <username/reply/userid> <reason (optional)>",
    },
)
async def lolgkick(event):  # sourcery no-metrics
    "kicks the person in all groups where you are admin"
    swte = await eor(event, "`gkicking.......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, swte)
    if not user:
        return
    if user.id == legend.uid:
        return await eod(swte, "`why would I kick myself`")
    san = await admin_groups(event.client)
    count = 0
    LEGEND = len(san)
    if LEGEND == 0:
        return await eod(swte, "`you are not admin of atleast one group` ")
    await swte.edit(
        f"`initiating gkick of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(LEGEND):
        try:
            await event.client.kick_participant(san[i], user.id)
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For kicking there`",
            )
    end = datetime.now()
    swttaken = (end - start).seconds
    if reason:
        await swte.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {swttaken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await swte.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {swttaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Kicked in {count} groups__\
                \n**Time taken : **`{swttaken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Kicked in {count} groups__\
                \n**Time taken : **`{swttaken} seconds`",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)
