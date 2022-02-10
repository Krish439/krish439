import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import eor
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        legendevent = await eor(event, "`Transfiguration Time! Converting to ....`")

    else:
        legendevent = event
    legendmedia = None
    catfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(catfile):
        os.remove(catfile)
    if mediatype == "Photo":
        legendmedia = await reply.download_media(file="./temp")
        im = Image.open(legendmedia)
        im.save(catfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, catfile, thumb=-1)
    elif mediatype == "Sticker":
        legendmedia = await reply.download_media(file="./temp")
        if legendmedia.endswith(".tgs"):
            catcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{legendmedia}' '{catfile}'"
            stdout, stderr = (await runcmd(catcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif legendmedia.endswith(".webp"):
            im = Image.open(legendmedia)
            im.save(catfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, catfile, thumb=-1)
        if not os.path.exists(catfile):
            legendmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(catfile, 0.1)
            except Exception:
                clip = clip.save_frame(catfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            legendmedia = await reply.download_media(file="./temp")
            im = Image.open(legendmedia)
            im.save(catfile)
    if legendmedia and os.path.lexists(legendmedia):
        os.remove(legendmedia)
    if os.path.lexists(catfile):
        return legendevent, catfile, mediatype
    return legendevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
