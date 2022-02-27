import io
import re
from collections import defaultdict
from datetime import datetime
from typing import Optional, Union

from telethon import Button, events
from telethon.errors import UserIsBlockedError
from telethon.events import CallbackQuery, StopPropagation
from telethon.utils import get_display_name

from userbot import Config, legend

from ..core import check_owner, pool
from ..core.logger import logging
from ..core.session import tgbot
from ..helpers import reply_id
from ..helpers.utils import _format
from ..sql_helper.bot_blacklists import check_is_black_list
from ..sql_helper.bot_pms_sql import (
    add_user_to_db,
    get_user_id,
    get_user_logging,
    get_user_reply,
)
from ..sql_helper.bot_starters import add_starter_to_db, get_starter_details
from ..sql_helper.globals import delgvar, gvarstatus
from ..sql_helper.idaddar import get_all_users
from . import BOTLOG, BOTLOG_CHATID
from .botmanagers import ban_user_from_bot

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


class FloodConfig:
    BANNED_USERS = set()
    USERS = defaultdict(list)
    MESSAGES = 3
    SECONDS = 6
    ALERT = defaultdict(dict)
    AUTOBAN = 10


async def check_bot_started_users(user, event):
    if user.id == Config.OWNER_ID:
        return
    check = get_starter_details(user.id)
    if check is None:
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        notification = f"👤 {_format.mentionuser(user.first_name , user.id)} ने चालू किया है मुझे।\
                \n**ID: **`{user.id}`\
                \n*नाम: **{get_display_name(user)}"
    else:
        start_date = check.date
        notification = f"👤 {_format.mentionuser(user.first_name , user.id)} ने रिस्टार्ट किया है मुझे।\
                \n**ID: **`{user.id}`\
                \n**नाम: **{get_display_name(user)}"
    try:
        add_starter_to_db(user.id, get_display_name(user), start_date, user.username)
    except Exception as e:
        LOGS.error(str(e))
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, notification)


@legend.bot_cmd(
    pattern=f"^/start({botusername})?([\s]+)?$",
    incoming=True,
    func=lambda e: e.is_private,
)
async def bot_start(event):
    chat = await event.get_chat()
    user = await legend.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{user.first_name}](tg://user?id={user.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = user.first_name
    my_last = user.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{user.username}" if user.username else my_mention
    if chat.id != Config.OWNER_ID:
        customstrmsg = gvarstatus("START_TEXT") or None
        if customstrmsg is not None:
            start_msg = customstrmsg.format(
                mention=mention,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            )
        else:
            start_msg = f"हेलो 👤{mention},\nमें {my_mention} का असिस्टेंट बोट हु।\n आप मेरे गुरु से यहाँ से संपर्क कर सकते हैं\n\n [LegendBot](https://t.me/LEGEND_K_USERBOT)"
            buttons = [
                (
                    Button.inline("🔰 रूल्स 🔰 ", data="rules"),
                    Button.inline(" डिप्लॉय 🚀", data="deploy"),
                ),
                (Button.url("🔱 सपोर्ट 🔱", "https://t.me/LEGEND_K_USERBOT"),),
            ]
    else:
        start_msg = "हेलो सर!\nमैं आपका कैसे मदद कर सकता हु?"
        buttons = [
            (
                Button.url(" सपोर्ट ", "https://t.me/LEGEND_K_USERBOT"),
                Button.url(" अपडेट्स ", "https://t.me/OFFICIAL_K_LEGENDBOT"),
            ),
            (
                Button.inline(" यूजर्स ", data="users"),
                Button.inline(" सेटिंग्स ", data="osg"),
            ),
            (Button.inline(" हैक ", data="hack"),),
        ]
    try:
        await event.client.send_message(
            chat.id,
            start_msg,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Error**\nThere was a error while user starting your bot. `{e}`",
            )


@legend.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.answer("यह आपके लिए नहीं है मेरे गुरु", cache_time=0, alert=True)
    else:
        await tgbot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                (Button.inline("Close", data="close"),),
            ],
        )


@legend.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        total_users = get_all_users()
        users_list = "⚜ जो भी आपका यूजरबॉट उसे किया है सबका लिस्ट है.⚜ \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="सबका लिस्ट .",
                allow_cache=False,
            )
    else:
        await event.answer(
            "रुकिए आप मेरे मास्टर नही हो सो मैं आपको इस बटन का क्लिक करने का एक्सेस नही दे सकता हु",
            cache_time=0,
            alert=True,
        )


@legend.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="सुन fix",
            link_preview=False,
            buttons=[
                (Button.inline(" ट्यूटोरियल ", data="LOGED"),),
                (Button.url("गीतहब ❓", "https://github.com/LEGEND-AI/LEGENDBOT"),),
            ],
        )


@legend.bot_cmd(incoming=True, func=lambda e: e.is_private)
async def bot_pms(event):  # sourcery no-metrics
    chat = await event.get_chat()
    if check_is_black_list(chat.id):
        return
    if chat.id != Config.OWNER_ID:
        msg = await event.forward_to(Config.OWNER_ID)
        try:
            add_user_to_db(msg.id, get_display_name(chat), chat.id, event.id, 0, 0)
        except Exception as e:
            LOGS.error(str(e))
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**एरर**\nजब मैं आपकी मैसेज डाटाब्से में स्टोर कर रहा हु तो\n`{str(e)}`",
                )
    else:
        if event.text.startswith("/"):
            return
        reply_to = await reply_id(event)
        if reply_to is None:
            return
        users = get_user_id(reply_to)
        if users is None:
            return
        for usr in users:
            user_id = int(usr.chat_id)
            reply_msg = usr.reply_id
            user_name = usr.first_name
            break
        if user_id is not None:
            try:
                if event.media:
                    msg = await event.client.send_file(
                        user_id, event.media, caption=event.text, reply_to=reply_msg
                    )
                else:
                    msg = await event.client.send_message(
                        user_id, event.text, reply_to=reply_msg, link_preview=False
                    )
            except UserIsBlockedError:
                return await event.reply("यह बोट यूजर ने ब्लॉक किया है| ❌")
            except Exception as e:
                return await event.reply(f"**इरर:**\n`{e}`")
            try:
                add_user_to_db(
                    reply_to, user_name, user_id, reply_msg, event.id, msg.id
                )
            except Exception as e:
                LOGS.error(str(e))
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"**एरर**\nजब मैं आपकी मैसेज डाटाब्से में स्टोर कर रहा हु तो\n`{str(e)}`",
                    )


@legend.bot_cmd(edited=True)
async def bot_pms_edit(event):  # sourcery no-metrics
    chat = await event.get_chat()
    if check_is_black_list(chat.id):
        return
    if chat.id != Config.OWNER_ID:
        users = get_user_reply(event.id)
        if users is None:
            return
        reply_msg = None
        for user in users:
            if user.chat_id == str(chat.id):
                reply_msg = user.message_id
                break
        if reply_msg := next(
            (user.message_id for user in users if user.chat_id == str(chat.id)),
            None,
        ):
            await event.client.send_message(
                Config.OWNER_ID,
                f"⬆️ **ये वाला मैसेज यूजर ने एडिट किया हैं।** {_format.mentionuser(get_display_name(chat) , chat.id)} as :",
                reply_to=reply_msg,
            )
            msg = await event.forward_to(Config.OWNER_ID)
            try:
                add_user_to_db(msg.id, get_display_name(chat), chat.id, event.id, 0, 0)
            except Exception as e:
                LOGS.error(str(e))
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"**एरर**\nजब मैं आपकी मैसेज डाटाब्से में स्टोर कर रहा हु तो\n`{str(e)}`",
                    )

    else:
        reply_to = await reply_id(event)
        if reply_to is not None:
            users = get_user_id(reply_to)
            result_id = 0
            if users is None:
                return
            for usr in users:
                if event.id == usr.logger_id:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    result_id = usr.result_id
                    break
            if result_id != 0:
                try:
                    await event.client.edit_message(
                        user_id, result_id, event.text, file=event.media
                    )
                except Exception as e:
                    LOGS.error(str(e))


@tgbot.on(events.MessageDeleted)
async def handler(event):
    for msg_id in event.deleted_ids:
        users_1 = get_user_reply(msg_id)
        users_2 = get_user_logging(msg_id)
        if users_2 is not None:
            result_id = 0
            for usr in users_2:
                if msg_id == usr.logger_id:
                    user_id = int(usr.chat_id)
                    result_id = usr.result_id
                    break
            if result_id != 0:
                try:
                    await event.client.delete_messages(user_id, result_id)
                except Exception as e:
                    LOGS.error(str(e))
        if users_1 is not None:
            reply_msg = next(
                (
                    user.message_id
                    for user in users_1
                    if user.chat_id != Config.OWNER_ID
                ),
                None,
            )
            try:
                if reply_msg:
                    users = get_user_id(reply_msg)
                    for usr in users:
                        user_id = int(usr.chat_id)
                        user_name = usr.first_name
                        break
                    if check_is_black_list(user_id):
                        return
                    await event.client.send_message(
                        Config.OWNER_ID,
                        f"⬆️ **ये मैसेज यूजर ने डिलीट किया है** {_format.mentionuser(user_name , user_id)}.",
                        reply_to=reply_msg,
                    )
            except Exception as e:
                LOGS.error(str(e))


@legend.bot_cmd(pattern="^/uinfo$", from_users=Config.OWNER_ID)
async def bot_start(event):
    reply_to = await reply_id(event)
    if not reply_to:
        return await event.reply("Reply to a message to get message info")
    info_msg = await event.client.send_message(
        event.chat_id,
        "`🔎 सर्च कर रहा हु टेलीग्राम डाटाब्स में ...`",
        reply_to=reply_to,
    )
    users = get_user_id(reply_to)
    if users is None:
        return await info_msg.edit(
            "**एरर:** \n`सॉरी मैं उससे भी ढूंढ पाया पूरे डाटाब्से में से !, :(`"
        )
    for usr in users:
        user_id = int(usr.chat_id)
        user_name = usr.first_name
        break
    if user_id is None:
        return await info_msg.edit(
            "**एरर:** \n`सॉरी मैं उससे भी ढूंढ पाया पूरे डाटाब्से में से !, :(`"
        )
    uinfo = f"यह मैसेज भेजा है - 👤 {_format.mentionuser(user_name , user_id)}\
            \n**पहला नाम:** {user_name}\
            \n**यूजर आईडी:** `{user_id}`"
    await info_msg.edit(uinfo)


async def send_flood_alert(user_) -> None:
    # sourcery no-metrics
    buttons = [
        (
            Button.inline("🚫 बैन", data=f"bot_pm_ban_{user_.id}"),
            Button.inline(
                "बोट एंटीफ्लूड [ऑफ]",
                data="toggle_bot-antiflood_off",
            ),
        )
    ]
    found = False
    if FloodConfig.ALERT and (user_.id in FloodConfig.ALERT.keys()):
        found = True
        try:
            FloodConfig.ALERT[user_.id]["count"] += 1
        except KeyError:
            found = False
            FloodConfig.ALERT[user_.id]["count"] = 1
        except Exception as e:
            if BOTLOG:
                await legend.tgbot.send_message(
                    BOTLOG_CHATID,
                    f"**एरोर:**\nजब मैं आपका एंटीफ्लुड अपडेट कर रहा हु तो\n`{e}`",
                )

        flood_count = FloodConfig.ALERT[user_.id]["count"]
    else:
        flood_count = FloodConfig.ALERT[user_.id]["count"] = 1

    flood_msg = (
        r"⚠️ **#फ्लूड वार्निंग**"
        "\n\n"
        f"  आईडी: `{user_.id}`\n"
        f"  नाम: {get_display_name(user_)}\n"
        f"  👤 यूजर: {_format.mentionuser(get_display_name(user_), user_.id)}"
        f"\n\n**स्पैम कर रहा है। !** ->  [ Flood rate ({flood_count}) ]\n"
        "__क्विक एक्शन__: बोट से कनैक्शन टूट गया है।."
    )

    if found:
        if flood_count >= FloodConfig.AUTOBAN:
            if user_.id in Config.SUDO_USERS:
                sudo_spam = (
                    f"**सूडो यूजर** {_format.mentionuser(user_.first_name , user_.id)}:\n  ID: {user_.id}\n\n"
                    "फ्लूडिंग कर रहा है। !, Check `.help delsudo` to remove the user from Sudo."
                )
                if BOTLOG:
                    await legend.tgbot.send_message(BOTLOG_CHATID, sudo_spam)
            else:
                await ban_user_from_bot(
                    user_,
                    f"ऑटोमैटिक ब्लॉक्ड [exceeded flood rate of ({FloodConfig.AUTOBAN})]",
                )
                FloodConfig.USERS[user_.id].clear()
                FloodConfig.ALERT[user_.id].clear()
                FloodConfig.BANNED_USERS.remove(user_.id)
            return
        fa_id = FloodConfig.ALERT[user_.id].get("fa_id")
        if not fa_id:
            return
        try:
            msg_ = await legend.tgbot.get_messages(BOTLOG_CHATID, fa_id)
            if msg_.text != flood_msg:
                await msg_.edit(flood_msg, buttons=buttons)
        except Exception as fa_id_err:
            LOGS.debug(fa_id_err)
            return
    else:
        if BOTLOG:
            fa_msg = await legend.tgbot.send_message(
                BOTLOG_CHATID,
                flood_msg,
                buttons=buttons,
            )
        try:
            chat = await legend.tgbot.get_entity(BOTLOG_CHATID)
            await legend.tgbot.send_message(
                Config.OWNER_ID,
                f"⚠️  **[बोट फ्लड वार्निंग !](https://t.me/c/{chat.id}/{fa_msg.id})**",
            )
        except UserIsBlockedError:
            if BOTLOG:
                await legend.tgbot.send_message(
                    BOTLOG_CHATID, "**अनब्लॉक् करो आपका बोट !**"
                )
    if FloodConfig.ALERT[user_.id].get("fa_id") is None and fa_msg:
        FloodConfig.ALERT[user_.id]["fa_id"] = fa_msg.id


@legend.tgbot.on(CallbackQuery(data=re.compile(b"bot_pm_ban_([0-9]+)")))
@check_owner
async def bot_pm_ban_cb(c_q: CallbackQuery):
    user_id = int(c_q.pattern_match.group(1))
    try:
        user = await legend.get_entity(user_id)
    except Exception as e:
        await c_q.answer(f"एरर:\n{e}")
    else:
        await c_q.answer(f"बैनिंग यूजर -> {user_id} ...", alert=False)
        await ban_user_from_bot(user, "Spamming Bot")
        await c_q.edit(f"✅ **बैन हो गया**  यूजर आईडी: {user_id}")


def time_now() -> Union[float, int]:
    return datetime.timestamp(datetime.now())


@pool.run_in_thread
def is_flood(uid: int) -> Optional[bool]:
    """Checks if a user is flooding"""
    FloodConfig.USERS[uid].append(time_now())
    if (
        len(
            list(
                filter(
                    lambda x: time_now() - int(x) < FloodConfig.SECONDS,
                    FloodConfig.USERS[uid],
                )
            )
        )
        > FloodConfig.MESSAGES
    ):
        FloodConfig.USERS[uid] = list(
            filter(
                lambda x: time_now() - int(x) < FloodConfig.SECONDS,
                FloodConfig.USERS[uid],
            )
        )
        return True


@legend.tgbot.on(CallbackQuery(data=re.compile(b"toggle_bot-antiflood_off$")))
@check_owner
async def settings_toggle(c_q: CallbackQuery):
    if gvarstatus("bot_antif") is None:
        return await c_q.answer("बोट एंटीफ्लूड पहले से बंद है।.", alert=False)
    delgvar("bot_antif")
    await c_q.answer("बोट एंटीफ्लूड ऑफ हो गया ।.", alert=False)
    await c_q.edit("बोट एंटीफ्लूड ऑफ हो गया !")


@legend.bot_cmd(incoming=True, func=lambda e: e.is_private)
@legend.bot_cmd(edited=True, func=lambda e: e.is_private)
async def antif_on_msg(event):
    if gvarstatus("bot_antif") is None:
        return
    chat = await event.get_chat()
    if chat.id == Config.OWNER_ID:
        return
    user_id = chat.id
    if check_is_black_list(user_id):
        raise StopPropagation
    if await is_flood(user_id):
        await send_flood_alert(chat)
        FloodConfig.BANNED_USERS.add(user_id)
        raise StopPropagation
    if user_id in FloodConfig.BANNED_USERS:
        FloodConfig.BANNED_USERS.remove(user_id)
