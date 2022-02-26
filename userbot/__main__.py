import sys

import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import legend
from .start import killer, legends
from .utils import (
    add_bot_to_logger_group,
    hekp,
    load_plugins,
    setup_bot,
    spams,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("लीजेंड्यूजर बोट")

print(userbot.__copyright__)
print("लिसन। अंडर द टर्मे ऑफ द " + userbot.__license__)

cmdhr = Config.HANDLER


try:
    LOGS.info("स्टार्टिंग यूजरबोट")
    legend.loop.run_until_complete(setup_bot())
    LOGS.info("टेलीग्राम बोट स्टार्टअप सक्सेसफुल")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await killer()
    await spams()
    print("----------------")
    print("स्टार्टिंग बोट मोड!")
    print("⚜ लीजेंडबोट डिप्लॉय हो गया h ⚜")
    print("----------------")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    await legends()
    return


legend.loop.run_until_complete(startup_process())
legend.loop.create_task(hekp())

if len(sys.argv) not in (1, 3, 4):
    legend.disconnect()
else:
    try:
        legend.run_until_disconnected()
    except ConnectionError:
        pass
