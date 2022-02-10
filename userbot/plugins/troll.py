"""
Created by @LegendBoy_XD
plugin for Legend_UserBot
☝☝☝
You remove this, you gay.
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import legend

from ..core.managers import eod, eor
from . import reply_id

menu_category = "fun"


async def mememaker(borg, msg, legend, chat_id, reply_to_id):
    async with borg.conversation("@themememakerbot") as conv:
        try:
            msg = await conv.send_message(msg)
            pic = await conv.get_response()
            await borg.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await legend.edit("Please unblock @themememakerbot and try again")
            return
        await borg.send_file(
            chat_id,
            pic,
            reply_to=reply_to_id,
        )
    await borg.delete_messages(conv.chat_id, [msg.id, pic.id])


@legend.legend_cmd(
    pattern="fox ?([\s\S]*)",
    command=("fox", menu_category),
    info={
        "header": "fox meme",
        "description": "Send sneeky fox troll",
        "usage": "{tr}fox <text>",
    },
)
async def legend(event):
    "sneeky fox troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/sf {input_text}"
    await eor(event, "```Fox is on your way...```")
    await mememaker(event.client, msg, legend, event.chat_id, reply_to_id)


@legend.legend_cmd(
    pattern="talkme ?([\s\S]*)",
    command=("talkme", menu_category),
    info={
        "header": "talk to me meme",
        "description": "Send talk to me troll",
        "usage": "{tr}talkme <text>",
    },
)
async def cat(event):
    "talk to me troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/ttm {input_text}"
    await eor(event, "```Wait making your hardcore meme...```")
    await mememaker(event.client, msg, legend, event.chat_id, reply_to_id)


@legend.legend_cmd(
    pattern="slip ?([\s\S]*)",
    command=("slip", menu_category),
    info={
        "header": "brain say meme",
        "description": "Send you a sleeping brain meme.",
        "usage": "{tr}slip <text>",
    },
)
async def legend(event):
    "Sleeping brain meme."
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/bbn {input_text}"
    await eor(event, "```You can't sleep...```")
    await mememaker(event.client, msg, legend, event.chat_id, reply_to_id)


@legend.legend_cmd(
    pattern="sbob ?([\s\S]*)",
    command=("sbob", menu_category),
    info={
        "header": "spongebob meme",
        "description": "Send you spongebob meme.",
        "usage": "{tr}sbob <text>",
    },
)
async def legend(event):
    "spongebob troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/sp {input_text}"
    await eor(event, "```Yaah wait for spongebob...```")
    await mememaker(event.client, msg, legend, event.chat_id, reply_to_id)


@legend.legend_cmd(
    pattern="child ?([\s\S]*)",
    command=("child", menu_category),
    info={
        "header": "child meme",
        "description": "Send you child in trash meme.",
        "usage": "{tr}child <text>",
    },
)
async def legend(event):
    "child troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await eod(event, "`Give me some text to process...`")
    msg = f"/love {input_text}"
    await eor(event, "```Wait for your son......```")
    await mememaker(event.client, msg, legend, event.chat_id, reply_to_id)
