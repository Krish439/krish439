from telethon import functions

from userbot import legend

from ..Config import Config
from ..core import CMD_INFO, GRP_INFO, PLG_INFO
from ..core.managers import eod, eor
from ..helpers.utils import reply_id

cmdprefix = Config.HANDLER

menu_category = "tools"

hemojis = {
    "एडमिन": "👮‍♂️",
    "बोट": "🤖",
    "फन": "🎨",
    "मिस्क": "🧩",
    "टूल्स": "🧰",
    "यूटिलस": "🗂",
    "एक्स्ट्रा": "➕",
    "यूजलेस": "⚰️",
}


def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None


async def cmdinfo(input_str, event, plugin=False):
    if input_str[0] == cmdprefix:
        input_str = input_str[1:]
    try:
        about = CMD_INFO[input_str]
    except KeyError:
        if plugin:
            await eod(
                event,
                f"आपके बॉट में `{input_str}` के रूप में कोई प्लगइन या कमांड नहीं है.",
            )
            return None
        await eod(event, f"आपके बॉट में `{input_str}` जैसी कोई कमांड नहीं है।")
        return None
    except Exception as e:
        await eod(event, f"**Error**\n`{e}`")
        return None
    outstr = f"**🕹कमांड :** `{cmdprefix}{input_str}`\n"
    plugin = get_key(input_str)
    if plugin is not None:
        outstr += f"**🔰प्लगइन :** `{plugin}`\n"
        category = getkey(plugin)
        if category is not None:
            outstr += f"**📍 कैटेगरी :** `{category}`\n\n"
    outstr += f"**📜 इंट्रो :**\n{about[0]}"
    return outstr


async def plugininfo(input_str, event, type):
    try:
        cmds = PLG_INFO[input_str]
    except KeyError:
        outstr = await cmdinfo(input_str, event, plugin=True)
        return outstr
    except Exception as e:
        await eod(event, f"एरर\n`{e}`")
        return None
    if len(cmds) == 1 and (type is None or (type and type != "-p")):
        outstr = await cmdinfo(cmds[0], event, plugin=False)
        return outstr
    outstr = f"प्लगइन : `{input_str}`\n"
    outstr += f"कमांड्स अवेलेबल: `{len(cmds)}`\n"
    category = getkey(input_str)
    if category is not None:
        outstr += f"📍कैटेगरी : `{category}`\n\n"
    for cmd in sorted(cmds):
        outstr += f"**🕹कमांड :** `{cmdprefix}{cmd}`\n"
        try:
            outstr += f"**📜इंफॉर्मेशन :** __{CMD_INFO[cmd][1]}__\n\n"
        except IndexError:
            outstr += "**📜इंफॉर्मेशन :** `None`\n\n"
    outstr += f"**👨‍💻 यूसेज : ** `{cmdprefix}help <command name>`\
        \nनोट : यदि कमांड का नाम प्लगइन नाम के समान है तो इसका उपयोग करें `{cmdprefix}help -l <command name>`."
    return outstr


async def grpinfo():
    outstr = "प्लगइंस इन द लीजेंडबॉट्:\n\n"
    outstr += f"**👨‍💻 यूसेज : ** `{cmdprefix}help <plugin name>`\n\n"
    category = ["admin", "bot", "fun", "misc", "tools", "utils", "extra", "useless"]
    for legend in category:
        plugins = GRP_INFO[legend]
        outstr += f"**{hemojis[legend]} {legend.title()} **({len(plugins)})\n"
        for plugin in plugins:
            outstr += f"`{plugin}`  "
        outstr += "\n\n"
    return outstr


async def cmdlist():
    outstr = "आपके लीजेंडबॉट में कमांड की कुल सूची है :\n\n"
    category = ["admin", "bot", "fun", "misc", "tools", "utils", "extra"]
    for legend in category:
        plugins = GRP_INFO[legend]
        outstr += f"**{hemojis[legend]} {legend.title()} ** - {len(plugins)}\n\n"
        for plugin in plugins:
            cmds = PLG_INFO[plugin]
            outstr += f"• **{plugin.title()} has {len(cmds)} commands**\n"
            for cmd in sorted(cmds):
                outstr += f"  - `{cmdprefix}{cmd}`\n"
            outstr += "\n"
    outstr += f"**👨‍💻 यूसेज : ** `{cmdprefix}help -l <command name>`"
    return outstr


@legend.legend_cmd(
    pattern="help ?(-l|-p|-t)? ?([\s\S]*)?",
    command=("help", menu_category),
    info={
        "header": "लीजेंडबोट के लिए गाइड पाने के लिए.",
        "description": "कमांड या प्लगइन के लिए जानकारी या गाइड प्राप्त करने के लिए",
        "note": "यदि कमांड का नाम और प्लगइन का नाम समान है तो आपको प्लगइन के लिए गाइड मिलता है। तो इस प्रकार का उपयोग करने से आपको कमांड गाइड मिलती है",
        "flags": {
            "l": "कमांड की जानकारी प्राप्त करने के लिए.",
            "p": "प्लगइन की जानकारी प्राप्त करने के लिए.",
            "t": "सभी प्लगइन्स को टेक्स्ट फॉर्मेट में प्राप्त करने के लिए.",
        },
        "usage": [
            "{tr}help (plugin/command name)",
            "{tr}help -l (command name)",
        ],
        "examples": ["{tr}help help", "{tr}help -l help"],
    },
)
async def _(event):
    "लीजेंडबोट के लिए गाइड पाने के लिए."
    type = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if type and type == "-l" and input_str:
        outstr = await cmdinfo(input_str, event)
        if outstr is None:
            return
    elif input_str:
        outstr = await plugininfo(input_str, event, type)
        if outstr is None:
            return
    elif type == "-t":
        outstr = await grpinfo()
    else:
        results = await event.client.inline_query(Config.BOT_USERNAME, "help")
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
        return
    await eor(event, outstr)


@legend.legend_cmd(
    pattern="cmds(?:\s|$)([\s\S]*)",
    command=("cmds", menu_category),
    info={
        "header": "To show list of cmds.",
        "description": "if no input is given then will show list of all commands.",
        "usage": [
            "{tr}cmds for all cmds",
            "{tr}cmds <plugin name> for paticular plugin",
        ],
    },
)
async def _(event):
    "To get list of commands."
    input_str = event.pattern_match.group(1)
    if not input_str:
        outstr = await cmdlist()
    else:
        try:
            cmds = PLG_INFO[input_str]
        except KeyError:
            return await eod(event, "__Invalid plugin name recheck it.__")
        except Exception as e:
            return await eod(event, f"**Error**\n`{e}`")
        outstr = f"**📜 {input_str.title()} has {len(cmds)} commands**\n"
        for cmd in cmds:
            outstr += f"  - `{cmdprefix}{cmd}`\n"
        outstr += f"**👨‍💻  यूसेज : ** `{cmdprefix}help -l <command name>`"
    await eor(event, outstr, aslink=True, linktext="Total Commands of LegendBot are :")


@legend.legend_cmd(
    pattern="dc$",
    command=("dc", menu_category),
    info={
        "header": "To show dc of your account.",
        "description": "Dc of your account and list of dc's will be showed",
        "usage": "{tr}dc",
    },
)
async def _(event):
    "To get dc of your bot"
    result = await event.client(functions.help.GetNearestDcRequest())
    result = f"**📜Dc details of your account:**\
              \n**Country :** {result.country}\
              \n**Current Dc :** {result.this_dc}\
              \n**Nearest Dc :** {result.nearest_dc}\
              \n\n**List Of Telegram Data Centres:**\
              \n**DC1 : **Miami FL, USA\
              \n**DC2 :** Amsterdam, NL\
              \n**DC3 :** Miami FL, USA\
              \n**DC4 :** Amsterdam, NL\
              \n**DC5 : **Singapore, SG\
                "
    await eor(event, result)
