import asyncio
import requests 
import os 
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import BOTLOG, BOTLOG_CHATID, legend

from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers.utils import _format, get_user_from_event, reply_id
from ..sql_helper.global_collectionjson import add_collection, get_collection


@legend.legend_cmd(
    pattern="fpic(?:\s|$)([\s\S]*)",
    command=("fpic", menu_category),
    info={
        "header": "Fake Pic Generation",
        "description": "Fake Pic Generation From UserBot.",
        "usage": "{tr}fpic",
    },
)
async def _(event):
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
        with open("LEGENDBOT.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By LEGENDBOT."
    fole = "LEGENDBOT.jpg"
    await event.client.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/LEGENDBOT.jpg ")
