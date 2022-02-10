import nekos

from userbot import legend

from ..core.managers import eor

menu_category = "fun"


@legend.legend_cmd(
    pattern="tcat$",
    command=("tcat", menu_category),
    info={
        "header": "Some random cat facial text art",
        "usage": "{tr}tcat",
    },
)
async def hmm(legend):
    "Some random cat facial text art"
    nekos.textcat()
    await eor(cat, reactcat)


@legend.legend_cmd(
    pattern="why$",
    command=("why", menu_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(legend):
    "Some random Funny questions"
    nekos.why()
    await eor(cat, whycat)


@legend.legend_cmd(
    pattern="fact$",
    command=("fact", menu_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(legend):
    "Some random facts"
    nekos.fact()
    await eor(cat, factcat)
