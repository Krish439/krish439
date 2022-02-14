import random

from . import eor, legend

menu_category = "fun"


# $$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢

GENDER = [
    "u is mard",
    "u is man",
    "u is legendt",
    "u is woman",
    "u is gey",
    "u is chakka",
]

EMOTICONS = [
    "(҂⌣̀_⌣́)",
    "（；¬＿¬)",
    "(-｡-;",
    "┌[ O ʖ̯ O ]┐",
    "〳 ͡° Ĺ̯ ͡° 〵",
]

WAVING = [
    "(ノ^∇^)",
    "(;-_-)/",
    "@(o・ェ・)@ノ",
    "ヾ(＾-＾)ノ",
    "ヾ(◍’౪◍)ﾉﾞ♡",
    "(ό‿ὸ)ﾉ",
    "(ヾ(´・ω・｀)",
]

WTF = [
    "༎ຶ‿༎ຶ",
    "(‿ˠ‿)",
    "╰U╯☜(◉ɷ◉ )",
    "(;´༎ຶ益༎ຶ)♡",
    "╭∩╮(︶ε︶*)chu",
    "( ＾◡＾)っ (‿|‿)",
]

LOB = [
    "乂❤‿❤乂",
    "(｡♥‿♥｡)",
    "( ͡~ ͜ʖ ͡°)",
    "໒( ♥ ◡ ♥ )७",
    "༼♥ل͜♥༽",
]

CONFUSED = [
    "(・_・ヾ",
    "｢(ﾟﾍﾟ)",
    "﴾͡๏̯͡๏﴿",
    "(￣■￣;)!?",
    "▐ ˵ ͠° (oo) °͠ ˵ ▐",
    "(-_-)ゞ゛",
]

DEAD = [
    "(✖╭╮✖)",
    "✖‿✖",
    "(+_+)",
    "(✖﹏✖)",
    "∑(✘Д✘๑)",
]

SED = [
    "(＠´＿｀＠)",
    "⊙︿⊙",
    "(▰˘︹˘▰)",
    "●︿●",
    "(　´_ﾉ` )",
    "彡(-_-;)彡",
]

DOG = [
    "-ᄒᴥᄒ-",
    "◖⚆ᴥ⚆◗",
]

SHRUG = [
    "( ͡° ͜ʖ ͡°)",
    "¯\_(ツ)_/¯",
    "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "ʕ•ᴥ•ʔ",
    "(▀ Ĺ̯▀   )",
    "(ง ͠° ͟ل͜ ͡°)ง",
    "༼ つ ◕_◕ ༽つ",
    "ಠ_ಠ",
    "(☞ ͡° ͜ʖ ͡°)☞",
    "¯\_༼ ି ~ ି ༽_/¯",
    "c༼ ͡° ͜ʖ ͡° ༽⊃",
]

# ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓


@legend.legend_cmd(
    pattern="gender ([\s\S]*)",
    command=("gender", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}gender",
    },
)
async def metoo(e):
    txt = random.choice(GENDER)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="shrug ([\s\S]*)",
    command=("shrug", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}shrug",
    },
)
async def metoo(e):
    txt = random.choice(SHRUG)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="dome ([\s\S]*)",
    command=("dome", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}dome",
    },
)
async def metoo(e):
    txt = random.choice(DOG)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="mesed ([\s\S]*)",
    command=("mesed", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}mesed",
    },
)
async def metoo(e):
    txt = random.choice(SED)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="medead ([\s\S]*)",
    command=("medead", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}medead",
    },
)
async def metoo(e):
    txt = random.choice(DEAD)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="confused ([\s\S]*)",
    command=("confused", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}confused",
    },
)
async def metoo(e):
    txt = random.choice(CONFUSED)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="lobb ([\s\S]*)",
    command=("lobb", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}lobb",
    },
)
async def metoo(e):
    txt = random.choice(LOB)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="wut ([\s\S]*)",
    command=("wut", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}wut",
    },
)
async def metoo(e):
    txt = random.choice(WTF)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="wave ([\s\S]*)",
    command=("wave", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}wave",
    },
)
async def metoo(e):
    txt = random.choice(WAVING)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="hehe ([\s\S]*)",
    command=("hehe", menu_category),
    info={
        "header": "try out yourself to see",
        "usage": "{tr}hehe",
    },
)
async def metoo(e):
    txt = random.choice(EMOTICONS)
    await eor(e, txt)
