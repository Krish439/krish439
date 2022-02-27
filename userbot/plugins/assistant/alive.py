from telethon import events

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『लीजेंडबोट』ऑनलाइन है⚜ \n\n"
pm_caption += f"मालिक ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣टेलेथोंन ~ `1.15.0` \n"
pm_caption += f"┣『लीजेंडबोट』~ `{LEGENDversion}` \n"
pm_caption += f"┣चैनल ~ [चैनल](https://t.me/Official_K_LegendBot)\n"
pm_caption += f"┣**लाइसेंस** ~ [लाइसेंस ३.०](https://github.com/ITS-LEGENDBOT/LEGENDBOT/blob/master/LICENSE)\n"
pm_caption += f"┣कॉपीराइट ~ By [लीजेंडबोट』 ](https://t.me/Legend_K_Userbot)\n"
pm_caption += f"┣असिटेंट ~  [『लीजेंडबॉय』 ](https://t.me/LegendBoy_XD)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『लीजेंडबोट』](https://t.me/Legend_K_Userbot) «««"

from telethon import events


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
