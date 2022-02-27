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
        "header": "आईएमजी को पहचानने के लिए।",
        "description": "मान लीजिए कि यू को आईएमजी में टेक्स्ट ढूंढना है। फिर इस cmd का उपयोग pic . के उत्तर के साथ करें,",
        "usage": [
            "{tr}recognize <reply to pic>",
        ],
        "examples": "{tr}recognize <reply to pic>",
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("किसी भी उपयोगकर्ता की मीडिया फ़ाइल का उत्तर दें")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        await event.edit("वास्तविक उपयोगकर्ता संदेश का उत्तर दें।")
        return
    await event.edit("इस मीडिया को पहचान रहे है।")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Rekognition_Bot"))
            await eod("सफलतापूर्वक अनवरोधित किया गया अब पुन: प्रयास करें")
            return
        if response.text.startswith("अगला संदेश देखें"):
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
        "header": "किसी भी उपयोगकर्ता का इतिहास प्राप्त करने के लिए।",
        "description": "यदि उपयोगकर्ता नाम बदलता है तो यह सीएमडी उपयोग करने के लिए सबसे अच्छा है किसी भी उपयोगकर्ता का इतिहास प्राप्त करें,",
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
        await eod(event, "वास्तविक उपयोगकर्ताओं की आवश्यकता है। बोट्स नहीं")
        return
    lol = await eor(event, "Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Sangmatainfo_bot"))
            await eod(event, "हो गया अनब्लॉक @Sangmatainfo_bot अब पुनः प्रयास करें")
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
        await eod(
            event,
            "`कृपया इस CMD कार्य को प्राप्त करने के लिए किसी उपयोगकर्ता को उत्तर दें`",
        )
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
            await eod(
                event, "अनब्लॉक किया गया @Sangmatainfo_bot और अब पुनः प्रयास करें"
            )
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
        "header": "पाने के लिए आपका खाता सीमित है या नहीं",
        "description": "यदि आपका खाता सीमित है तो आप उर लिमिटेड तक किसी को भी डीएम नहीं कर सकते इस बॉट सहायता को खोलें। पता लगाने के लिए आपका खाता सीमित है या नहीं,",
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
            first = await conv.send_message("/start")
            yup = await conv.get_response()
            sweetie = yup.text
            if sweetie.startswith("Good"):
                response = await conv.send_message("Cool, thanks")
                await eor(event, "बधाई हो, कोई सीमा लागू नहीं है")
                await event.client.delete_messages(
                    conv.chat_id, [first.id, yup.id, response.id]
                )
            elif "automatically" in sweetie:
                await conv.send_message("I was wrong, please release me now")
                await eor(
                    event, f"आपका खाता सीमित है [यह क्लिक करो](https://t.me/spambot)"
                )
            else:
                await eor(event, sweetie)
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@spambot"))
            await eor(event, "**हो गया अनब्लॉक @spambot और अब फिर से प्रयास करें**")
            return
