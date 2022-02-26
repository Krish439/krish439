import re

from telethon import Button
from telethon.errors import MessageNotModifiedError
from telethon.events import CallbackQuery

from userbot import legend

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


@legend.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_true")))
async def age_verification_true(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "यह देखते हुए कि यह एक मूर्खतापूर्ण निर्णय है, मैंने इसे अनदेखा करने के लिए चुना है.",
            alert=True,
        )
    await event.answer("हाँ मैं 18+ का हूँ", alert=False)
    buttons = [
        Button.inline(
            text="अनिश्चित / निर्णय में परिवर्तन ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="इस प्लगइन को एक्सेस करने के लिए डेटाबेस वर्र्स में `ALLOW_NSFW` = True सेट करें",
            file="https://telegra.ph/file/85f3071c31279bcc280ef.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@legend.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_false")))
async def age_verification_false(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "यह देखते हुए कि यह एक मूर्खतापूर्ण निर्णय है, मैंने इसे अनदेखा करने के लिए चुना है.",
            alert=True,
        )
    await event.answer("नहीं, मैं नहीं हूँ", alert=False)
    buttons = [
        Button.inline(
            text="अनिश्चित / निर्णय में परिवर्तन ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="बच्चे चले जाओ !",
            file="https://telegra.ph/file/1140f16a883d35224e6a1.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@legend.tgbot.on(CallbackQuery(data=re.compile(r"^chg_of_decision_")))
async def chg_of_decision_(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "यह देखते हुए कि यह एक मूर्खतापूर्ण निर्णय है, मैंने इसे अनदेखा करने के लिए चुना है।",
            alert=True,
        )
    await event.answer("Unsure", alert=False)
    buttons = [
        (
            Button.inline(text="हाँ मैं 18+ का हूँ", data="age_verification_true"),
            Button.inline(text="नहीं, मैं नहीं हूँ", data="age_verification_false"),
        )
    ]
    try:
        await event.edit(
            text="**क्या आप इसके लिए काफी उम्रदराज हैं? ?**",
            file="https://telegra.ph/file/238f2c55930640e0e8c56.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass
