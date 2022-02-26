import glob
import os
import sys
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

from userbot import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import legend
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, gvarstatus
from .pluginmanager import load_module, start_spam
from .tools import create_supergroup

LOGS = logging.getLogger("LegendUserBot")
cmdhr = Config.HANDLER


async def setup_bot():
    """
    To set up bot for userbot
    """
    try:
        await legend.connect()
        config = await legend(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == legend.session.server_address:
                if legend.session.dc_id != option.id:
                    LOGS.warning(
                        f"Fixed DC ID in session from {legend.session.dc_id}"
                        f" to {option.id}"
                    )
                legend.session.set_dc(option.id, option.ip_address, option.port)
                legend.session.save()
                break
        bot_details = await legend.tgbot.get_me()
        Config.BOT_USERNAME = f"@{bot_details.username}"
        legend.me = await legend.get_me()
        legend.uid = legend.tgbot.uid = utils.get_peer_id(legend.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(legend.me)
    except Exception as e:
        LOGS.error(f"LEGEND_STRING - {e}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.LEGENDUBLOGO = await legend.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/294b4dbdb74334fb0a8c1.jpg",
                caption="**आपका लीजेंडबॉट सफलतापूर्वक शुरू हो गया है.**",
                buttons=[(Button.url("सपोर्ट", "https://t.me/LEGEND_K_USERBOT"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await legend.check_testcases()
            message = await legend.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**Ok Bot is Back and Alive.**"
            await legend.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await legend.send_message(
                    msg_details[0],
                    f"{cmdhr}ping -a",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await legend.tgbot.get_me()
    lol = bot_details.username
    addgvar("BOT_USERNAME", lol)
    try:
        await legend(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=lol,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await legend(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[lol],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    type = True
                    check = 0
                    while type:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/{folder}/{shortname}.py"))
                LOGS.info(f"unable to load {shortname} because of error {e}")


async def hekp():
    try:
        os.environ[
            "LEGEND_STRING"
        ] = "स्ट्रिंग एक संवेदनशील डेटा है \nइसलिए इसे लेजेंडबॉट द्वारा संरक्षित किया गया है"
    except Exception as e:
        print(str(e))
    try:
        await legend(JoinChannelRequest("@Legend_K_Userbot"))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@Legend_Userbot"))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@Official_LegendBot"))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@catuserbot17"))
    except BaseException:
        pass


spam = os.environ.get("SPAM", None) or "OFF"


async def spams():
    if spam == "ON":
        import glob

        path = "userbot/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")


async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    type = False
    if BOTLOG:
        try:
            entity = await legend.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "निर्दिष्ट के लिए संदेश भेजने के लिए अनुमतियाँ अनुपलब्ध PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "निर्दिष्ट के लिए संदेश भेजने के लिए अनुमतियाँ अनुपलब्ध PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID पाया नहीं जा सकता। सुनिश्चित करें कि यह सही है."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID पाया नहीं जा सकता। सुनिश्चित करें कि यह सही है."
            )
        except Exception as e:
            LOGS.error(
                "सत्यापित करने का प्रयास करने पर एक अपवाद उत्पन्न हुआ PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "इस समूह को न हटाएं या समूह में न बदलें (यदि आप अपने पिछले सभी अंशों को समूह बदलते हैं, तो स्वागत खो जाएगा।),"
        _, groupid = await create_supergroup(
            "लीजेंडबोट्स लग ग्रुप", legend, Config.BOT_USERNAME, descript
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "PRIVATE_GROUP_BOT_API_ID के लिए निजी समूह सफलतापूर्वक बनाया गया और vars में जोड़ा गया."
        )
        type = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await legend.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "निर्दिष्ट PM_LOGGER_GROUP_ID के लिए संदेश भेजने के लिए अनुमतियाँ अनुपलब्ध हैं."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "निर्दिष्ट PM_LOGGER_GROUP_ID के लिए संदेश भेजने के लिए अनुमतियाँ अनुपलब्ध हैं."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID नहीं मिला। सुनिश्चित करें कि यह सही है।")
        except TypeError:
            LOGS.error(
                "PM_LOGGER_GROUP_ID समर्थित नहीं है। सुनिश्चित करें कि यह सही है."
            )
        except Exception as e:
            LOGS.error(
                "PM_LOGGER_GROUP_ID को सत्यापित करने का प्रयास करने पर एक अपवाद उत्पन्न हुआ.\n"
                + str(e)
            )
    if type:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "userbot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)
