import asyncio
import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, legend, legendversion

from ..Config import Config
from ..core.managers import eor
from ..helpers.functions import check_data_base_heal_th, get_readable_time, legendalive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

menu_category = "utils"


@legend.legend_cmd(
    pattern="legend$",
    command=("legend", menu_category),
    info={
        "header": "बॉट की जीवित स्थिति की जांच करने के लिए",
        "options": "इस कमांड में मीडिया दिखाने के लिए आपको मीडिया लिंक के साथ ALIVE_PIC सेट करना होगा, मीडिया को .tgm द्वारा जवाब देकर इसे प्राप्त करो",
        "usage": [
            "{tr}legend",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    legendevent = await eor(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    LOL_TEXT = gvarstatus("ALIVE_TEXT") or "**⚜ लीजेंडबॉट ऑनलाइन है ⚜**"
    LEGEND_IMG = (
        gvarstatus("IALIVE_PIC") or "https://telegra.ph/file/144d8ea74fef8ca12253c.jpg"
    )
    lal = [x for x in EMOJI.split()]
    EMOTES = random.choice(lal)
    tick = [x for x in LOL_TEXT.split(", ")]
    ALIVE_TEXT = random.choice(tick)
    hell_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = hell_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        legendver=legendversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if LEGEND_IMG:
        legend = [x for x in LEGEND_IMG.split()]
        IPIC = random.choice(legend)
        try:
            await event.client.send_file(
                event.chat_id, IPIC, caption=caption, reply_to=reply_to_id
            )
            await legendevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await eor(
                legendevent,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__इस लिंक से मीडिया नहीं मिल सकता :-**__ `{PIC}`",
            )
    else:
        await eor(
            legendevent,
            caption,
        )


temp = """{ALIVE_TEXT}
{EMOTES} मास्टर: {mention}
{EMOTES} अपटाइम : `{uptime}`
{EMOTES} टेलीथों वर्जन : `{telever}`
{EMOTES} लेजेंडुजरबोट वर्जन : `{legendver}`
{EMOTES} पायथन वर्जन : `{pyver}`
{EMOTES} डेटाबेस : `{dbhealth}`"""


@legend.legend_cmd(
    pattern="alive$",
    command=("alive", menu_category),
    info={
        "header": "इनलाइन मोड के माध्यम से बॉट की जीवित स्थिति की जांच करने के लिए",
        "options": "इस सीएमडी में मीडिया दिखाने के लिए आपको मीडिया लिंक के साथ ALIVE_PIC सेट करना होगा, मीडिया को .tgm द्वारा जवाब देकर इसे प्राप्त करें।",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "आपके इनलाइन बॉट द्वारा बॉट विवरण दिखाने का एक प्रकार"
    reply_to_id = await reply_id(event)
    a = gvarstatus("ALIVE_EMOJI") or "✥"
    Legend = [x for x in a.split()]
    EMOJI = random.choice(Legend)
    get_bot = await legend.tgbot.get_me()
    bot_name = get_bot.first_name
    bot_id = get_bot.id
    bmention = f"[{bot_name}](tg://user?id={bot_id})"
    legend_caption = "लीजेंडबॉट ऑनलाइन है\n"
    legend_caption += f"{EMOJI} टेलीथॉन वर्जन : `{version.__version__}\n`"
    legend_caption += f"{EMOJI} लीजेंडयूज़रबोट वर्जन : `{legendversion}`\n"
    legend_caption += f"{EMOJI} पायथन वर्जन : `{python_version()}\n`"
    legend_caption += f"{EMOJI} मेरा सेवक : {bmention}\n"
    legend_caption += f"{EMOJI} गुरु: {mention}\n"
    results = await event.client.inline_query(Config.BOT_USERNAME, legend_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


edit_time = 12
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/2426eab17330c6e6310ea.mp4"
file2 = "https://te.legra.ph/file/11ec9dd576ee5536125b2.jpg"
file3 = "https://te.legra.ph/file/d2a5265abdc4e73af1f94.jpg"
file4 = "https://telegra.ph/file/b6f0c65a337b1f2609d07.jpg"
file5 = "https://telegra.ph/file/af51de2749a4506d3eb43.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"**लीजेंडबॉट् इज अप**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{mention}』«««\n"
pm_caption += f"┣लेजेंडबोट ~ {legendversion}\n"
pm_caption += f"┣लेजेंड  ~ [ऑनर](https://t.me/Legend_K_Boy)\n"
pm_caption += f"┣सपोर्ट ~ [ग्रुप](https://t.me/Legend_K_Usebnot)\n"
pm_caption += f"┣रेपो    ~ [रेपो](https://github.com/LEGEND-AI/LEGENDBOT)\n"
pm_caption += f"**╰────────────**\n"


@legend.legend_cmd(
    pattern="about$",
    command=("about", menu_category),
    info={
        "header": "बॉट की जीवित स्थिति की जांच करने के लिए ",
        "options": "रैंडम मीडिया स्वचालित रूप से इसे प्राप्त करें",
        "usage": [
            "{tr}about",
        ],
    },
)
async def amireallyalive(yes):
    await yes.get_chat()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)
    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)
    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


@legend.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await legendalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
