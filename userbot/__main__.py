import sys

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import legend
from .start import killer, legends
from .utils import (
    add_bot_to_logger_group,
    hekp,
    ipchange,
    load_plugins,
    setup_bot,
    spams,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("LegendUserBot")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.HANDLER


try:
    LOGS.info("Starting Userbot")
    legend.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class LegendCheck:
    def __init__(self):
        self.sucess = True


Legendcheck = LegendCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Legendcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await killer()
    await spams()
    print("----------------")
    print("Starting Bot Mode!")
    print("⚜ LegendBot Has Been Deployed Successfully ⚜")
    print("----------------")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    await legends()
    Legendcheck.sucess = True
    return


legend.loop.run_until_complete(startup_process())
legend.loop.create_task(hekp())

if len(sys.argv) not in (1, 3, 4):
    legend.disconnect()
elif not Legendcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        legend.run_until_disconnected()
    except ConnectionError:
        pass
