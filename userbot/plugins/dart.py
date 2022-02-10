from telethon.tl.types import InputMediaDice

from . import legend

menu_category = "fun"


# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"


@legend.legend_cmd(
    pattern=f"({DART_E_MOJI}|{DICE_E_MOJI}|{BALL_E_MOJI})$",
    command=(f"({DART_E_MOJI}|{DICE_E_MOJI})|{BALL_E_MOJI})", menu_category),
    info={
        "header": "Send Anyone Of These",
        "usage": "{tr}🎯|🎲|🏀",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except:
            pass
