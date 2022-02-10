import random

from userbot import legend

from ..core.managers import eor
from . import catmemes

menu_category = "fun"


@legend.legend_cmd(
    pattern="congo$",
    command=("congo", menu_category),
    info={
        "header": " Congratulate the people..",
        "usage": "{tr}congo",
    },
)
async def _(e):
    "Congratulate the people."
    txt = random.choice(catmemes.CONGOREACTS)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="shg$",
    command=("shg", menu_category),
    info={
        "header": "Shrug at it !!",
        "usage": "{tr}shg",
    },
)
async def shrugger(e):
    "Shrug at it !!"
    txt = random.choice(catmemes.SHGS)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="runs$",
    command=("runs", menu_category),
    info={
        "header": "Run, run, RUNNN!.",
        "usage": "{tr}runs",
    },
)
async def runner_lol(e):
    "Run, run, RUNNN!"
    txt = random.choice(catmemes.RUNSREACTS)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="noob$",
    command=("noob", menu_category),
    info={
        "header": "Whadya want to know? Are you a NOOB?",
        "usage": "{tr}noob",
    },
)
async def metoo(e):
    "Whadya want to know? Are you a NOOB?"
    txt = random.choice(catmemes.NOOBSTR)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="insult$",
    command=("insult", menu_category),
    info={
        "header": "insult someone.",
        "usage": "{tr}insult",
    },
)
async def insult(e):
    "insult someone."
    txt = random.choice(catmemes.INSULT_STRINGS)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="love$",
    command=("love", menu_category),
    info={
        "header": "Chutiyappa suru",
        "usage": "{tr}love",
    },
)
async def suru(chutiyappa):
    "Chutiyappa suru"
    txt = random.choice(catmemes.LOVESTR)
    await eor(chutiyappa, txt)


@legend.legend_cmd(
    pattern="dhoka$",
    command=("dhoka", menu_category),
    info={
        "header": "Dhokha kha gya",
        "usage": "{tr}dhoka",
    },
)
async def katgya(chutiya):
    "Dhokha kha gya"
    txt = random.choice(catmemes.DHOKA)
    await eor(chutiya, txt)


@legend.legend_cmd(
    pattern="hey$",
    command=("hey", menu_category),
    info={
        "header": "start a conversation with people",
        "usage": "{tr}hey",
    },
)
async def hoi(e):
    "start a conversation with people."
    txt = random.choice(catmemes.HELLOSTR)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="pro$",
    command=("pro", menu_category),
    info={
        "header": "If you think you're pro, try this.",
        "usage": "{tr}pro",
    },
)
async def proo(e):
    "If you think you're pro, try this."
    txt = random.choice(catmemes.PRO_STRINGS)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="react ?([\s\S]*)",
    command=("react", menu_category),
    info={
        "header": "Make your userbot react",
        "types": [
            "happy",
            "think",
            "wave",
            "wtf",
            "love",
            "confused",
            "dead",
            "sad",
            "dog",
        ],
        "usage": ["{tr}react <type>", "{tr}react"],
    },
)
async def _(e):
    "Make your userbot react."
    input_str = e.pattern_match.group(1)
    if input_str in "happy":
        emoticons = catmemes.FACEREACTS[0]
    elif input_str in "think":
        emoticons = catmemes.FACEREACTS[1]
    elif input_str in "wave":
        emoticons = catmemes.FACEREACTS[2]
    elif input_str in "wtf":
        emoticons = catmemes.FACEREACTS[3]
    elif input_str in "love":
        emoticons = catmemes.FACEREACTS[4]
    elif input_str in "confused":
        emoticons = catmemes.FACEREACTS[5]
    elif input_str in "dead":
        emoticons = catmemes.FACEREACTS[6]
    elif input_str in "sad":
        emoticons = catmemes.FACEREACTS[7]
    elif input_str in "dog":
        emoticons = catmemes.FACEREACTS[8]
    else:
        emoticons = catmemes.FACEREACTS[9]
    txt = random.choice(emoticons)
    await eor(e, txt)


@legend.legend_cmd(
    pattern="10iq$",
    command=("10iq", menu_category),
    info={
        "header": "You retard !!",
        "usage": "{tr}10iq",
    },
)
async def iqless(e):
    "You retard !!"
    await eor(e, "♿")


@legend.legend_cmd(
    pattern="fp$",
    command=("fp", menu_category),
    info={
        "header": "send you face pam emoji!",
        "usage": "{tr}fp",
    },
)
async def facepalm(e):
    "send you face pam emoji!"
    await eor(e, "🤦‍♂")


@legend.legend_cmd(
    pattern="bt$",
    command=("bt", menu_category),
    info={
        "header": "Believe me, you will find this useful.",
        "usage": "{tr}bt",
    },
    groups_only=True,
)
async def bluetext(e):
    """Believe me, you will find this useful."""
    await eor(
        e,
        "/BLUETEXT /MUST /CLICK.\n"
        "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?",
    )


@legend.legend_cmd(
    pattern="session$",
    command=("session", menu_category),
    info={
        "header": "telethon session error code(fun)",
        "usage": "{tr}session",
    },
)
async def _(event):
    "telethon session error code(fun)."
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await eor(event, mentions)
