import asyncio
from datetime import datetime

from telethon.errors import BadRequestError, FloodWaitError, ForbiddenError

from userbot import legend

from ..Config import Config
from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers import reply_id, time_formatter
from ..helpers.utils import _format
from ..sql_helper.bot_blacklists import check_is_black_list, get_all_bl_users
from ..sql_helper.bot_starters import del_starter_from_db, get_all_starters
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from .botmanagers import (
    ban_user_from_bot,
    get_user_and_reason,
    progress_str,
    unban_user_from_bot,
)

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME
cmhd = Config.HANDLER


@legend.bot_cmd(pattern="^/help$", from_users=Config.OWNER_ID)
async def bot_help(event):
    await event.reply(
        f"""बोट में कमांड है।:
**नोट : **__यह कमांड सिर्फ इसी बोट में काम करेगा__ {botusername}
• **कमांड : **/uinfo <किसी यूजर को रिप्लाई करके>
• **इंफॉर्मेशन : **__आपने देखा है कि फॉरवर्ड किए गए स्टिकर्स/इमोजी में फॉरवर्ड टैग नहीं होता है, इसलिए आप उस यूजर की पहचान कर सकते हैं जिसने इस कमांड द्वारा मैसेज भेजे हैं।.__
• **नोट : **__यह सभी फॉरवर्ड किए गए संदेशों के लिए काम करता है। यहां तक ​​​​कि उन उपयोगकर्ताओं के लिए भी जिनकी अनुमति है संदेश अग्रेषित करें कोई नहीं.__
• **कमांड : **/ban <कारण> or /ban <यूजरनेम/यूजर आईडी> <कारण>
• **इंफॉर्मेशन : **__एक उपयोगकर्ता संदेश का कारण के साथ उत्तर दें ताकि उसे सूचित किया जाएगा क्योंकि आपने बॉट से प्रतिबंधित कर दिया है और उसके संदेश आपको आगे नहीं भेजे जाएंगे.__
• **नोट : **__कारण जरूरी है। अकारण यह काम नहीं करेगा. __
• **कमांड : **/unban <कारण(ऐच्छिक)> or /unban <यूजरनेम/यूजर आईडी>
• **इंफॉर्मेशन : **__उपयोगकर्ता संदेश का उत्तर दें या बॉट से प्रतिबंध हटाने के लिए उपयोगकर्ता नाम/उपयोगकर्ता आईडी प्रदान करें.__
• **नोट : **__प्रतिबंधित उपयोगकर्ताओं की सूची उपयोग की जांच करने के लिए__ `{cmhd}bblist`.
• **कमांड : **/broadcast
• **इंफॉर्मेशन : **__आपके बॉट को शुरू करने वाले प्रत्येक उपयोगकर्ता को प्रसारित करने के लिए एक संदेश का उत्तर दें। उपयोगकर्ताओं की सूची प्राप्त करने के लिए उपयोग करें__ `{cmhd}bot_users`.
• **नोट: **__यदि उपयोगकर्ता ने बॉट को रोक दिया/अवरुद्ध कर दिया तो उसे आपके डेटाबेस से हटा दिया जाएगा यानी वह bot_starters सूची से मिटा दिया जाएगा.__
"""
    )


@legend.bot_cmd(pattern="^/broadcast$", from_users=Config.OWNER_ID)
async def bot_broadcast(event):
    replied = await event.get_reply_message()
    if not replied:
        return await event.reply("Reply to a message for Broadcasting First !")
    start_ = datetime.now()
    br_cast = await replied.reply("ब्रॉडकास्टिंग।..")
    blocked_users = []
    count = 0
    bot_users_count = len(get_all_starters())
    if bot_users_count == 0:
        return await event.reply("`किसी ने आपका बॉट शुरू नहीं किया.`")
    users = get_all_starters()
    if users is None:
        return await event.reply("`उपयोगकर्ताओं की सूची लाते समय त्रुटियां हुईं.`")
    for user in users:
        try:
            await event.client.send_message(
                int(user.user_id), "🔊 आपको एक **नया** प्रसारण प्राप्त हुआ."
            )
            await event.client.send_message(int(user.user_id), replied)
            await asyncio.sleep(0.8)
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
        except (BadRequestError, ValueError, ForbiddenError):
            del_starter_from_db(int(user.user_id))
        except Exception as e:
            LOGS.error(str(e))
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID, f"**प्रसारण करते समय त्रुटि**\n`{e}`"
                )
        else:
            count += 1
            if count % 5 == 0:
                try:
                    prog_ = (
                        "🔊 ब्रॉडकास्टिंग ...\n\n"
                        + progress_str(
                            total=bot_users_count,
                            current=count + len(blocked_users),
                        )
                        + f"\n\n• ✔️ **सफलता** :  `{count}`\n"
                        + f"• ✖️ **फेल्ड** :  `{len(blocked_users)}`"
                    )
                    await br_cast.edit(prog_)
                except FloodWaitError as e:
                    await asyncio.sleep(e.seconds)
    end_ = datetime.now()
    b_info = f"🔊संदेश को सफलतापूर्वक प्रसारित किया गया ➜  <b>{count} यूजर्स.</b>"
    if len(blocked_users) != 0:
        b_info += f"\n🚫  <b>{len(blocked_users)} यूजर्स</b> आपके बॉट को हाल ही में ब्लॉक किया है, इसलिए हटा दिया गया है।."
    b_info += (
        f"\n⏳  <code>प्रक्रिया ली: {time_formatter((end_ - start_).seconds)}</code>."
    )
    await br_cast.edit(b_info, parse_mode="html")


@legend.legend_cmd(
    pattern="bot_users$",
    command=("bot_users", menu_category),
    info={
        "header": "उपयोगकर्ताओं की सूची प्राप्त करने के लिए जिन्होंने बॉट शुरू किया.",
        "description": "आपका बॉट शुरू करने वाले उपयोगकर्ताओं की पूरी सूची प्राप्त करने के लिए",
        "usage": "{tr}bot_users",
    },
)
async def ban_starters(event):
    "बोट को शुरू करने वाले उपयोगकर्ताओं की सूची प्राप्त करने के लिए"
    ulist = get_all_starters()
    if len(ulist) == 0:
        return await eod(event, "`अभी तक किसी ने आपका बॉट शुरू नहीं किया.`")
    msg = "**आपके बॉट को शुरू करने वाले उपयोगकर्ताओं की सूची है :\n\n**"
    for user in ulist:
        msg += f"• 👤 {_format.mentionuser(user.first_name , user.user_id)}\n**ID:** `{user.user_id}`\n**यूजरनेम:** @{user.username}\n**तारीख: **__{user.date}__\n\n"
    await eor(event, msg)


@legend.bot_cmd(pattern="^/ban\\s+([\\s\\S]*)", from_users=Config.OWNER_ID)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id,
            "`मुझे प्रतिबंध लगाने के लिए उपयोगकर्ता नहीं मिल रहा है .`",
            reply_to=reply_to,
        )
    if not reason:
        return await event.client.send_message(
            event.chat_id,
            "`उपयोगकर्ता को प्रतिबंधित करने के लिए पहले कारण बताएं`",
            reply_to=reply_to,
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**एरर:**\n`{e}`")
    if user_id == Config.OWNER_ID:
        return await event.reply("मैं आप पर प्रतिबंध नहीं लगा सकता मास्टर")
    check = check_is_black_list(user.id)
    if check:
        return await event.client.send_message(
            event.chat_id,
            f"#बैन\
            \nउपयोगकर्ता मेरी प्रतिबंधित उपयोगकर्ता सूची में पहले से मौजूद है.\
            \n**बैन का कारण:** `{check.reason}`\
            \n**तारीख:** `{check.date}`.",
        )
    msg = await ban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@legend.bot_cmd(pattern="^/unban(?:\\s|$)([\\s\\S]*)", from_users=Config.OWNER_ID)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id,
            "`मुझे प्रतिबंध हटाने के लिए उपयोगकर्ता नहीं मिल रहा है`",
            reply_to=reply_to,
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**एरर:**\n`{e}`")
    check = check_is_black_list(user.id)
    if not check:
        return await event.client.send_message(
            event.chat_id,
            f"#User_Not_Banned\
            \n👤 {_format.mentionuser(user.first_name , user.id)} मेरी प्रतिबंधित उपयोगकर्ता सूची में मौजूद नहीं है",
        )
    msg = await unban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@legend.legend_cmd(
    pattern="bblist$",
    command=("bblist", menu_category),
    info={
        "header": "उन उपयोगकर्ताओं की सूची प्राप्त करने के लिए जिन्हें बोट में प्रतिबंधित किया गया है.",
        "description": "में प्रतिबंधित उपयोगकर्ताओं की सूची प्राप्त करने के लिए",
        "usage": "{tr}bblist",
    },
)
async def ban_starters(event):
    "में प्रतिबंधित उपयोगकर्ताओं की सूची प्राप्त करने के लिए."
    ulist = get_all_bl_users()
    if len(ulist) == 0:
        return await eod(
            event, "`आपके बॉट में अभी तक किसी को भी प्रतिबंधित नहीं किया गया है.`"
        )
    msg = "**आपके बॉट में प्रतिबंधित उपयोगकर्ताओं की सूची है:\n\n**"
    for user in ulist:
        msg += f"• 👤 {_format.mentionuser(user.first_name , user.chat_id)}\n**आईडी:** `{user.chat_id}`\n**यूजरनेम:** @{user.username}\n**तारीख: **__{user.date}__\n**कारण:** __{user.reason}__\n\n"
    await eor(event, msg)


@legend.legend_cmd(
    pattern="bot_antif (on|off)$",
    command=("bot_antif", menu_category),
    info={
        "header": "बॉट एंटीफ्लड को सक्षम या अक्षम करने के लिए.",
        "description": "अगर इसे चालू किया गया था तो कम समय में 10 संदेशों या समान संदेशों के 10 संपादन के बाद आपका बॉट ऑटो उन्हें लॉक कर देता है.",
        "usage": [
            "{tr}bot_antif on",
            "{tr}bot_antif off",
        ],
    },
)
async def ban_antiflood(event):
    "बॉट एंटीफ्लड को सक्षम या अक्षम करने के लिए."
    input_str = event.pattern_match.group(1)
    if input_str == "on":
        if gvarstatus("bot_antif") is not None:
            return await eod(event, "`बॉट एंटीफ्लड पहले से ही सक्षम था।`")
        addgvar("bot_antif", True)
        await eod(event, "`बॉट एंटीफ्लड सक्षम.`")
    elif input_str == "off":
        if gvarstatus("bot_antif") is None:
            return await eod(event, "`बॉट एंटिफ्लूड पहले से ही अक्षम था.`")
        delgvar("bot_antif")
        await eod(event, "`बॉट एंटीफ्लूड डिसेबल्ड.`")
