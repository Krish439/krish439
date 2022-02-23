from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions

from .. import legend
from ..core.managers import eod, eor

telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")


menu_category = "tools"


@legend.legend_cmd(
    pattern="recognize(?:\s|$)([\s\S]*)",
    command=("recognize", menu_category),
    info={
        "header": "To Recognize the img.",
        "description": "Suppose U Have To Find Text In Img.Then Use this cmd with reply to pic,",
        "usage": [
            "{tr}recognize <reply to pic>",
        ],
        "examples": "{tr}recognize <reply to pic>",
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user's media File")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Rekognition_Bot"))
            await eod("Unblocked Successfully Now try again")
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            oye = response.message.message
            await eod(oye)
            return
        else:
            await eod("sorry, I couldnt find it")


@legend.legend_cmd(
    pattern="history(?:\s|$)([\s\S]*)",
    command=("history", menu_category),
    info={
        "header": "To Get History Of Any User.",
        "description": "If User Change The Name Then This Cmd Is Best To Use Get History Of Anyone User,",
        "usage": [
            "{tr}history <reply to user>",
        ],
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await eod(event, "`Please Reply To A User To Get This Module Work`")
        return
    reply_message = await event.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(event, "Need actual users. Not Bots")
        return
    lol = await eor(event, "Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Sangmatainfo_bot"))
            await eod(event, "Done Unblocked @Sangmatainfo_bot & Now Try Again")
            return
        if response1.text.startswith("Name History"):
            await lol.edit(response1.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id]
            )
        elif response2.text.startswith("Name History"):
            await lol.edit(response2.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id]
            )
        else:
            await lol.edit("No Records Found !")


@legend.legend_cmd(
    pattern="uhistory(?:\s|$)([\s\S]*)",
    command=("uhistory", menu_category),
    info={
        "header": "To Get History Of Username Of Any User.",
        "usage": "{tr}uhistory reply to message",
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await eod(event, "`Please Reply To A User To Get This Cmd Work`")
        return
    reply_message = await event.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(event, "Need actual users. Not Bots")
        return
    lol = await eor(event, "Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
            response3 = await conv.get_response()
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Sangmatainfo_bot"))
            await eod(event, "Done Unblocked @Sangmatainfo_bot & Now Try Again")
            return
        if response1.text.startswith("Username History"):
            await lol.edit(response1.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        elif response2.text.startswith("Username History"):
            await lol.edit(response2.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        else:
            await lol.edit("No Records Found !")


@legend.legend_cmd(
    pattern="limit(?:\s|$)([\s\S]*)",
    command=("limit", menu_category),
    info={
        "header": "To Get Ur Account Is Limited Or Not",
        "description": "If Ur Account Is Limited Then U Cant dm Anyone Until Ur Limited Open This Bot Help.To Find Ur Account Is Limited Or Not,",
        "usage": [
            "{tr}limit",
        ],
    },
)
async def _(event):
    bot = "@SpamBot"
    await eor(event, "Processing....")
    async with event.client.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            yup = await conv.get_response()
            sweetie = yup.text
            if sweetie.startswith("Good"):
                await conv.send_message("Cool, thanks")
                await eod(event, "Congratulations, No Limits Are Apply")
            elif "automatically" in sweetie:
                await conv.send_message("I was wrong, please release me now")
                await eor(
                    event, f"Ur Account Is Limited [Click Here](https://t.me/spambot)"
                )
            else:
                await eor(event, sweetie)
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@spambot"))
            await eod("**Unblocked @spambot and Now try Again")
            return
