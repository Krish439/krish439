import asyncio
from datetime import datetime

from telethon.tl import functions, types

from userbot import legend

from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers.tools import media_type
from ..helpers.utils import _format
from ..sql_helper.globals import gvarstatus
from . import BOTLOG, BOTLOG_CHATID

menu_category = "utils"

LOGS = logging.getLogger(__name__)


class AFK:
    def __init__(self):
        self.USERAFK_ON = {}
        self.afk_time = None
        self.last_afk_message = {}
        self.afk_star = {}
        self.afk_end = {}
        self.reason = None
        self.msg_link = False
        self.afk_type = None
        self.media_afk = None
        self.afk_on = False


AFK_ = AFK()


@legend.legend_cmd(outgoing=True, edited=False)
async def set_not_afk(event):
    if AFK_.afk_on is False:
        return
    back_alive = datetime.now()
    AFK_.afk_end = back_alive.replace(microsecond=0)
    if AFK_.afk_star != {}:
        total_afk_time = AFK_.afk_end - AFK_.afk_star
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message = event.message.message
    if (("afk" not in current_message) or ("#afk" not in current_message)) and (
        "on" in AFK_.USERAFK_ON
    ):
        shite = await event.client.send_message(
            event.chat_id,
            "`वापस जिंदा! अब और नहीं AFK.\nइतने टाइम के लिए AFK था " + endtime + "`",
        )
        AFK_.USERAFK_ON = {}
        AFK_.afk_time = None
        await asyncio.sleep(5)
        await shite.delete()
        AFK_.afk_on = False
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#AFKFALSE \n`Set AFK mode to False\n"
                + "वापस जिंदा!अब और नही afk.\nइतने टाइम के लिए AFK था "
                + endtime
                + "`",
            )


@legend.legend_cmd(
    incoming=True, func=lambda e: bool(e.mentioned or e.is_private), edited=False
)
async def on_afk(event):  # sourcery no-metrics
    if AFK_.afk_on is False:
        return
    back_alivee = datetime.now()
    AFK_.afk_end = back_alivee.replace(microsecond=0)
    if AFK_.afk_star != {}:
        total_afk_time = AFK_.afk_end - AFK_.afk_star
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text or "#afk" in current_message_text:
        return False
    if not await event.get_sender():
        return
    if AFK_.USERAFK_ON and not (await event.get_sender()).bot:
        msg = None
        if AFK_.afk_type == "media":
            if AFK_.reason:
                message_to_reply = (
                    f"`में AFK हु .\n\nइतने टाइम से {endtime}\nकारण : {AFK_.reason}`"
                )
            else:
                message_to_reply = (
                    f"`में AFK हु.\n\nइतने टाइम से {endtime}\nकारण : नही पता ( ಠ ʖ̯ ಠ)`"
                )
            if event.chat_id:
                msg = await event.reply(message_to_reply, file=AFK_.media_afk.media)
        elif AFK_.afk_type == "text":
            if AFK_.msg_link and AFK_.reason:
                message_to_reply = (
                    f"**में AFK हु .\n\nइतने टाइम से {endtime}\nकारण : **{AFK_.reason}"
                )
            elif AFK_.reason:
                message_to_reply = (
                    f"`में AFK हु.\n\nइतने टाइम से {endtime}\nकारण : {AFK_.reason}`"
                )
            else:
                message_to_reply = f"`में AFK हु .\n\nइतने टाइम से {endtime}\nकारण : नही पता ( ಠ ʖ̯ ಠ)`"
            if event.chat_id:
                msg = await event.reply(message_to_reply)
        if event.chat_id in AFK_.last_afk_message:
            await AFK_.last_afk_message[event.chat_id].delete()
        AFK_.last_afk_message[event.chat_id] = msg
        if event.is_private:
            return
        hmm = await event.get_chat()
        if gvarstatus("AFKFWD") is None:
            return False
        if gvarstatus("AFKFWD") == "OFF":
            return False
        full = None
        try:
            full = await event.client.get_entity(event.message.from_id)
        except Exception as e:
            LOGS.info(str(e))
        messaget = media_type(event)
        resalt = f"#AFK_TAGS \n<b>ग्रुप : </b><code>{hmm.title}</code>"
        if full is not None:
            resalt += f"\n<b>फ्रॉम : </b> 👤{_format.htmlmentionuser(full.first_name , full.id)}"
        if messaget is not None:
            resalt += f"\n<b>मैसेज टाइप : </b><code>{messaget}</code>"
        else:
            resalt += f"\n<b>मैसेज : </b>{event.message.message}"
        resalt += f"\n<b>मैसेज लिंक: </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>"
        if not event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                resalt,
                parse_mode="html",
                link_preview=False,
            )


@legend.legend_cmd(
    pattern="afk(?:\s|$)([\s\S]*)",
    command=("afk", menu_category),
    info={
        "header": "आपके खाते के लिए afk सक्षम करता है",
        "description": "जब आप afk में होते हैं, यदि कोई आपको टैग करता है तो आपका बॉट उत्तर देगा क्योंकि वह ऑफ़लाइन है.\
        AFK का मतलब कीबोर्ड से दूर होता है.",
        "options": "यदि आप हाइपरलिंक उपयोग के साथ AFK कारण चाहते हैं [ ; ] कारण के बाद, मीडिया लिंक पेस्ट करें.",
        "usage": [
            "{tr}afk <कारण>",
            "{tr}afk <कारण> ; <लिंक>",
        ],
        "examples": "{tr}afk Let Me Sleep",
        "note": "जब आप कुछ भी, कहीं भी वापस टाइप करते हैं, तो AFK को बंद कर देता है। आप बिना तोड़े afk में जारी रखने के लिए संदेश में #afk का उपयोग कर सकते हैं",
    },
)
async def _(event):
    "खुद को afk यानी कीबोर्ड से दूर के रूप में चिह्नित करने के लिए"
    AFK_.USERAFK_ON = {}
    AFK_.afk_time = None
    AFK_.last_afk_message = {}
    AFK_.afk_end = {}
    AFK_.afk_type = "text"
    start_1 = datetime.now()
    AFK_.afk_on = True
    AFK_.afk_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        if ";" in input_str:
            msg, mlink = input_str.split(";", 1)
            AFK_.reason = f"[{msg.strip()}]({mlink.strip()})"
            AFK_.msg_link = True
        else:
            AFK_.reason = input_str
            AFK_.msg_link = False
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.afk_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await eod(event, f"`मैं afk जा रहा हूँ! इसलिये ~` {AFK_.reason}", 5)
        else:
            await eod(event, "`मैं अफकी जा रहा हूँ! `", 5)
        if BOTLOG:
            if AFK_.reason:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#AFKTRUE \nSet AFK mode to True, and Reason is {AFK_.reason}",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#AFKTRUE \nSet AFK mode to True, and Reason is Not Mentioned",
                )


@legend.legend_cmd(
    pattern="mafk(?:\s|$)([\s\S]*)",
    command=("mafk", menu_category),
    info={
        "header": "Afk चालू करने के लिए",
        "description": "जब आप afk में होते हैं, यदि कोई आपको टैग करता है तो आपका बॉट उत्तर देगा क्योंकि वह ऑफ़लाइन है.\
         AFK का मतलब कीबोर्ड से दूर होता है। यहाँ यह afk कमांड के विपरीत मीडिया का समर्थन करता है",
        "options": "यदि आप हाइपरलिंक उपयोग के साथ AFK कारण चाहते हैं [ ; ] कारण के बाद, मीडिया लिंक पेस्ट करें।",
        "usage": [
            "{tr}mafk <reason> मीडिया को रिप्लाई करके",
        ],
        "examples": "{tr}mafk में ऑफलाइन हु।",
        "नोट": "AFK बंद हो जाता है जब आप कुछ भी टाइप करोगे कही पर भी। उसे चालू रखने के लिए अपने मैसेज में #afk लिखे",
    },
)
async def _(event):
    "अपने आप को ऑफलाइन घोषित करने के लिए मतलब Away from keyboard (मीडिया सपोर्टेड है)"
    reply = await event.get_reply_message()
    media_t = media_type(reply)
    if media_t == "Sticker" or not media_t:
        return await eor(event, "`तुमने मीडिया को रिप्लाई नही किया। Afk ऑन नही हुआ`")
    if not BOTLOG:
        return await eor(
            event,
            "`मीडिया afk उसे करने के लिए ये PRIVATE_GROUP_BOT_API_ID Config सेट करो`",
        )
    AFK_.USERAFK_ON = {}
    AFK_.afk_time = None
    AFK_.last_afk_message = {}
    AFK_.afk_end = {}
    AFK_.media_afk = None
    AFK_.afk_type = "media"
    start_1 = datetime.now()
    AFK_.afk_on = True
    AFK_.afk_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        AFK_.reason = input_str
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.afk_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await eod(event, f"`में AFK जा रहा हु क्युकी ~` {AFK_.reason}", 5)
        else:
            await eod(event, "`मैं AFK जा रहा हूँ! `", 5)
        AFK_.media_afk = await reply.forward_to(BOTLOG_CHATID)
        if AFK_.reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#AFKTRUE \nआफ ऑन हो गया, और कारण है {AFK_.reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#AFKTRUE \nAFK मोड ऑन हो गया, और कारण नही पता।",
            )
