import random

from userbot import legend

from ..core.managers import eor
from . import fonts

menu_category = "extra"


@legend.legend_cmd(
    pattern="fmusical(?:\s|$)([\s\S]*)",
    command=("fmusical", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}fmusical <text>",
            "{tr}fmusical reply this command to text message",
        ],
        "examples": "{tr}fmusical LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            musicalcharacter = fonts.musicalfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, musicalcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="ancient(?:\s|$)([\s\S]*)",
    command=("ancient", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}ancient <text>",
            "{tr}ancient reply this command to text message",
        ],
        "examples": "{tr}ancient LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            ancientcharacter = fonts.ancientfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, ancientcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="vapor(?:\s|$)([\s\S]*)",
    command=("vapor", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}vapor <text>", "{tr}vapor reply this command to text message"],
        "examples": "{tr}vapor LegendUserBot",
    },
)
async def vapor(event):
    "Changes font style of the given text"
    reply_text = []
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await eor(event, "`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await eor(event, "".join(reply_text))


@legend.legend_cmd(
    pattern="smallcaps(?:\s|$)([\s\S]*)",
    command=("smallcaps", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}smallcaps <text>",
            "{tr}smallcaps reply this command to text message",
        ],
        "examples": "{tr}smallcaps LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="blackbf(?:\s|$)([\s\S]*)",
    command=("blackbf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}blackbf <text>",
            "{tr}blackbf reply this command to text message",
        ],
        "examples": "{tr}blackbf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="bubbles(?:\s|$)([\s\S]*)",
    command=("bubbles", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}bubbles <text>",
            "{tr}bubbles reply this command to text message",
        ],
        "examples": "{tr}bubbles LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="tanf(?:\s|$)([\s\S]*)",
    command=("tanf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}tanf <text>", "{tr}tanf reply this command to text message"],
        "examples": "{tr}tanf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            tantextcharacter = fonts.tantextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="boxf(?:\s|$)([\s\S]*)",
    command=("boxf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}boxf <text>", "{tr}boxf reply this command to text message"],
        "examples": "{tr}boxf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            littleboxtextcharacter = fonts.littleboxtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="smothtext(?:\s|$)([\s\S]*)",
    command=("smothtext", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}smothtext <text>",
            "{tr}smothtext reply this command to text message",
        ],
        "examples": "{tr}smothtext LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smothtextcharacter = fonts.smothtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smothtextcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="egyptf(?:\s|$)([\s\S]*)",
    command=("egyptf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}egyptf <text>", "{tr}egyptf reply this command to text message"],
        "examples": "{tr}egyptf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            egyptfontcharacter = fonts.egyptfontfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, egyptfontcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="maref(?:\s|$)([\s\S]*)",
    command=("maref", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}maref <text>", "{tr}maref reply this command to text message"],
        "examples": "{tr}maref LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            nightmarecharacter = fonts.nightmarefont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, nightmarecharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="handcf(?:\s|$)([\s\S]*)",
    command=("handcf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}handcf <text>", "{tr}handcf reply this command to text message"],
        "examples": "{tr}handcf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwcapitalcharacter = fonts.hwcapitalfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, hwcapitalcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="doublef(?:\s|$)([\s\S]*)",
    command=("doublef", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}doublef <text>",
            "{tr}doublef reply this command to text message",
        ],
        "examples": "{tr}doublef LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            doubletextcharacter = fonts.doubletextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, doubletextcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="mock(?:\s|$)([\s\S]*)",
    command=("mock", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}mock <text>", "{tr}mock reply this command to text message"],
        "examples": "{tr}mock LegendUserBot",
    },
)
async def spongemocktext(mock):
    "Changes font style of the given text"
    reply_text = []
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await eor(mock, "`gIvE sOMEtHInG tO MoCk!`")
        return

    for charac in message:
        if charac.isalpha() and random.randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await eor(mock, "".join(reply_text))


@legend.legend_cmd(
    pattern="ghostf(?:\s|$)([\s\S]*)",
    command=("ghostf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}ghostf <text>", "{tr}ghostf reply this command to text message"],
        "examples": "{tr}ghostf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            ghostfontcharacter = fonts.ghostfontfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, ghostfontcharacter)
    await eor(event, string)


@legend.legend_cmd(
    pattern="handsf(?:\s|$)([\s\S]*)",
    command=("handsf", menu_category),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}handsf <text>", "{tr}handsf reply this command to text message"],
        "examples": "{tr}handsf LegendUserBot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwslcharacter = fonts.hwslfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, hwslcharacter)
    await eor(event, string)
