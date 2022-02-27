from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from ..helpers.functions import age_verification
from ..helpers.nsfw import unsave_gif
from ..helpers.utils import _legendutils, reply_id
from . import useless
from ..helpers.nsfw import unsave_gif
from . import legend

menu_category = "useless"


@legend.legend_cmd(
    pattern="hpic ([\s\S]*)",
    command=("hpic", menu_category),
    info={
        "header": "This Is 18+ Plugin",
        "usage": "{tr}hpic",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Lolis")
            response = await resp
        except YouBlockedUserError:
            await event.reply("```unblock @LoliHeavenBot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐 I Cant Find It")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hfutanari ([\s\S]*)",
    command=("hfutanari", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hfutanari",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Futanari")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐 I Cant Find that")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hshota ([\s\S]*)",
    command=("hshota", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hshota",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Shota")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hvideo ([\s\S]*)",
    command=("hvideo ", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hvideo",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Hentai Videos")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hoppai ([\s\S]*)",
    command=("hoppai", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hoppai",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Oppai")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="htrap ([\s\S]*)",
    command=("htrap", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}htrap",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Trap")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hbdsm ([\s\S]*)",
    command=("hbdsm", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hbdsm",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "BDSM")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hfurry ([\s\S]*)",
    command=("hfurry", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hfurry",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Furry")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hgif ([\s\S]*)",
    command=("hgif", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hgif",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "GIF Hentai")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])


@legend.legend_cmd(
    pattern="hcosplay ([\s\S]*)",
    command=("hcosplay", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hcosplay",
    },
)
async def _(event):
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            lol = await event.client.send_message(chat, "Cosplay")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(xxxx)
        await event.client.delete_message(conv.chat_id, [resp.id, lol.id])
