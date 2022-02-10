# Made By @The_LegendBoy Keep Credits If You Are Goanna Kang This Lol

# And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

# Usage .actressdp Im Not Responsible For Any Ban caused By This
import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from . import legend

menu_category = "tools"

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
ACTION_MEDIA_LINKS = [
    "https://te.legra.ph/file/329cff91cfe957c848cc7.jpg",
    "https://te.legra.ph/file/7b9bac130967ab536838f.jpg",
    "https://te.legra.ph/file/bfdf1d167f3307ec5c671.jpg",
    "https://te.legra.ph/file/7512e973572f1acb08ccf.jpg",
    "https://te.legra.ph/file/0332de0c88c21ff4cbfdf.jpg",
    "https://te.legra.ph/file/10fd063123687d6ee0d54.jpg",
    "https://te.legra.ph/file/af2143f656222a0f3c3d7.jpg",
    "https://te.legra.ph/file/51f819a0635a9840fbdda.jpg",
    "https://te.legra.ph/file/95a216dc8f10763d33171.jpg",
    "https://telegra.ph/file/ee86d2765ac896d77936c.jpg",
    "https://telegra.ph/file/e82256da1955896dc1917.jpg",
    "https://telegra.ph/file/0cb7c850fe5a585e4870a.jpg",
    "https://telegra.ph/file/a43ad4676ebb6be79f145.jpg",
    "https://telegra.ph/file/a2adfc8a99ea12d9eee35.jpg",
    "https://telegra.ph/file/7edeb9f1cb2ab091493e2.jpg",
]


@legend.legend_cmd(
    pattern="actiondp(?:\s|$)([\s\S]*)",
    command=("actiondp", menu_category),
    info={
        "header": "Random Action Dp Upload",
        "usage": [
            "{tr}actiondp",
        ],
    },
)
async def autopic(event):
    while True:
        piclink = random.randint(0, len(ACTION_MEDIA_LINKS) - 1)
        AUTOPP = ACTION_MEDIA_LINKS[piclink]
        downloaded_file_name = "./downloads/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass
        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            await eor(event, "Profile Pic Uploaded Successfully")
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return


OP_LINKS = [
    "https://telegra.ph/file/3a7d12118c87e2cec15a4.jpg",
    "https://telegra.ph/file/c5b6fe8cb74e71be92118.jpg",
    "https://telegra.ph/file/df8727bce8fcc6fb2d99c.jpg",
    "https://telegra.ph/file/53d72a8529ff2ed5c81ab.jpg",
    "https://telegra.ph/file/f53939fdcee68d667ede4.jpg",
    "https://telegra.ph/file/e709a2bf87ab3a4a21e27.jpg",
    "https://telegra.ph/file/5785fa3215385ac54af75.jpg",
    "https://telegra.ph/file/79845a027e210653c2c25.jpg",
    "https://telegra.ph/file/b3ac1619f80ca4d7c5f11.jpg",
    "https://telegra.ph/file/044f5606262ec574bf6bf.jpg",
    "https://telegra.ph/file/a9c2076aeb10e1c1aee4f.jpg",
    "https://telegra.ph/file/750727efa42616c50a62d.jpg",
    "https://telegra.ph/file/d1b01482dd985c1df57fb.jpg",
    "https://telegra.ph/file/69fff5f1b891b4674d0eb.jpg",
    "https://telegra.ph/file/166de20ff96242d655863.jpg",
]


@legend.legend_cmd(
    pattern="actressdp(?:\s|$)([\s\S]*)",
    command=("actressdp", menu_category),
    info={
        "header": "Start Random Pic Upload Of Actress",
        "usage": [
            "{tr}actressdp",
        ],
    },
)
async def autopic(event):
    while True:
        piclink = random.randint(0, len(OP_LINKS) - 1)
        AUTOPP = OP_LINKS[piclink]
        downloaded_file_name = "./downloads/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            await eor(event, "Profile Pic Uploaded Successfully")
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return


PUBG_LINKS = [
    "https://telegra.ph/file/e46bb59069494b67c6206.jpg",
    "https://telegra.ph/file/46d4065e3cbe3dbca84c6.jpg",
    "https://telegra.ph/file/fcaf6b0a5f59f46b8315a.jpg",
    "https://telegra.ph/file/a2700b01534043e7dd89a.jpg",
    "https://telegra.ph/file/33da99040875995ef0acf.jpg",
    "https://telegra.ph/file/fd419fac3884be4a798ac.jpg",
    "https://telegra.ph/file/5b50ffee9720c870ba36d.jpg",
    "https://telegra.ph/file/b49cefeabb1b8dc23473c.jpg",
    "https://telegra.ph/file/8b340699c555884e0bfba.jpg",
    "https://telegra.ph/file/66a0089849def5c4678b8.jpg",
]


@legend.legend_cmd(
    pattern="pubgdp(?:\s|$)([\s\S]*)",
    command=("pubgdp", menu_category),
    info={
        "header": "Start Random Pic Upload Of Pubg",
        "usage": [
            "{tr}pubgdp",
        ],
    },
)
async def autopic(event):
    while True:
        piclink = random.randint(0, len(PUBG_LINKS) - 1)
        AUTOPP = PUBG_LINKS[piclink]
        downloaded_file_name = "./downloads/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            await eor(event, "Profile Pic Uploaded Successfully")
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return
