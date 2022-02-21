import asyncio
import io
import os

import requests
from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from userbot import legend

from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers.tools import media_type
from ..helpers.yt_helper import *
from . import mention

menu_category = "utils"
LOGS = logging.getLogger(__name__)


try:

    from youtubesearchpython import *

except:
    os.system("pip install pip install youtube-search-python")


# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..! I am finding your song....</code>"
SONG_NOT_FOUND = "<code>Sorry !I am unable to find any song like that</code>"
SONG_SENDING_STRING = "<code>yeah..! i found something wi8..🥰...</code>"
SONGBOT_BLOCKED_STRING = "<code>Please unblock @songdl_bot and try again</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@legend.legend_cmd(
    pattern="lyrics(?:\s|$)([\s\S]*)",
    command=("lyrics", menu_category),
    info={
        "header": "Lyrics Of Song",
        "usage": "{tr}lyrics",
    },
)
async def nope(aura):
    KANNADIGA = aura.pattern_match.group(1)
    if not KANNADIGA:
        if aura.is_reply:
            (await aura.get_reply_message()).message
        else:
            await aura.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("iLyricsBot", f"{(deEmojify(KANNADIGA))}")

    await troll[0].click(
        aura.chat_id,
        reply_to=aura.reply_to_msg_id,
        silent=True if aura.is_reply else False,
        hide_via=True,
    )

    await aura.delete()


@legend.legend_cmd(
    pattern="song(?:\s|$)([\s\S]*)",
    command=("song", menu_category),
    info={
        "header": "Search Song",
        "usage": "{tr}song",
    },
)
async def _(event):
    query = event.text[6:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    hell = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f"thumb.jpg"
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, "wb").write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await event.edit("**Fetching Song**")
        with YoutubeDL(song_opts) as somg:
            hell_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(hell, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(hell, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(
            hell,
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await eor(hell, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(hell, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(hell, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eor(hell, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(hell, "`There was an error during info extraction.`")
    c_time = time.time()
    await event.edit(
        f"**🎶 Preparing to upload song 🎶 :** \n\n{hell_data['title']} \n**By :** {hell_data['uploader']}"
    )
    await event.client.send_file(
        event.chat_id,
        f"{hell_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**✘ Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {mention}",
        thumb=thumb_name,
        attributes=[
            DocumentAttributeAudio(
                duration=int(hell_data["duration"]),
                title=str(hell_data["title"]),
                performer=perf,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{hell_data['title']}.mp3")
        ),
    )
    await event.delete()
    os.remove(f"{hell_data['id']}.mp3")


@legend.legend_cmd(
    pattern="vsong(?:\s|$)([\s\S]*)",
    command=("vsong", menu_category),
    info={
        "header": "Search Song",
        "usage": "{tr}vsong",
    },
)
async def _(event):
    query = event.text[7:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    hell = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f"thumb.jpg"
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, "wb").write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await event.edit("**Fetching Video**")
        with YoutubeDL(video_opts) as somg:
            hell_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(hell, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(hell, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(
            hell,
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await eor(hell, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(hell, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(hell, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eor(hell, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(hell, "`There was an error during info extraction.`")
    except Exception as e:
        return await eor(hell, e)
    c_time = time.time()
    await event.edit(
        f"**📺 Preparing to upload video 📺 :** \n\n{hell_data['title']}\n**By :** {hell_data['uploader']}"
    )
    await event.client.send_file(
        event.chat_id,
        f"{hell_data['id']}.mp4",
        supports_streaming=True,
        caption=f"**✘ Video :** `{title}` \n\n**✘ By :** {mention}",
        thumb=thumb_name,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{hell_data['title']}.mp4")
        ),
    )
    await event.delete()
    os.remove(f"{hell_data['id']}.mp4")


@legend.legend_cmd(
    pattern="shazam$",
    command=("shazam", menu_category),
    info={
        "header": "To reverse search song.",
        "description": "Reverse search audio file using shazam api",
        "usage": "{tr}shazam <reply to voice/audio>",
    },
)
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await eod(
            event, "__Reply to Voice clip or Audio clip to reverse search that song.__"
        )
    legendevent = await eor(event, "__Downloading the audio clip...__")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await eod(
            legendevent, f"**Error while reverse searching song:**\n__{e}__"
        )

    image = track["images"]["background"]
    song = track["share"]["subject"]
    await event.client.send_file(
        event.chat_id, image, caption=f"**Song:** `{song}`", reply_to=reply
    )
    await legendevent.delete()


# reverse search by  @Lal_bakthan
@legend.legend_cmd(
    pattern="szm$",
    command=("szm", menu_category),
    info={
        "header": "To reverse search music file.",
        "description": "music file lenght must be around 10 sec so use ffmpeg plugin to trim it.",
        "usage": "{tr}szm",
    },
)
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await eod(event, "```Reply to an audio message.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    legendevent = await eor(event, "```Identifying the song```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await legendevent.edit(
                    "An error while identifying the song. Try to use a 5-10s long audio message."
                )
            await legendevent.edit("Wait just a sec...")
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await legendevent.edit("```Please unblock (@auddbot) and try again```")
            return
    namem = f"**Song Name : **`{result.text.splitlines()[0]}`\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await legendevent.edit(namem)
