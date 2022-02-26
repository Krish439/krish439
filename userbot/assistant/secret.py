import json
import os
import re

from telethon.events import CallbackQuery

from userbot import legend


@legend.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./userbot/secrets.txt"):
        jsondata = json.load(open("./userbot/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, legend.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "तुम इस बकवास को क्यों देख रहे थे, जाओ और अपना काम करो, बेवकूफ"
        except KeyError:
            reply_pop_up_alert = "यह संदेश अब लेजेंड सर्वर में मौजूद नहीं है।"
    else:
        reply_pop_up_alert = "यह संदेश अब लेजेंड सर्वर में मौजूद नहीं है।"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
