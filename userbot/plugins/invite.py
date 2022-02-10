from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import legend

from ..core.managers import eod, eor

menu_category = "utils"


@legend.legend_cmd(
    pattern="add ([\s\S]*)",
    command=("add", menu_category),
    info={
        "header": "Add the given user/users to the group where u used the command.",
        "description": "Adds only mentioned person or bot not all members",
        "usage": "{tr}add <username(s)/userid(s)>",
        "examples": "{tr}add @combot @MissRose_bot",
    },
)
async def _(event):
    "To invite a user to chat."
    to_add_users = event.pattern_match.group(1)
    if not event.is_channel and event.is_group:
        # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                    )
                )
            except Exception as e:
                return await eod(event, f"`{str(e)}`", 5)
    else:
        # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.channels.InviteToChannelRequest(
                        channel=event.chat_id, users=[user_id]
                    )
                )
            except Exception as e:
                return await eod(event, f"`{e}`", 5)

    await eor(event, f"`{to_add_users} is/are Invited Successfully`")


@legend.legend_cmd(
    pattern="inviteall ([\s\S]*)",
    command=("inviteall", menu_category),
    info={
        "header": "Add the given user/users to the group where u used the command.",
        "description": "Adds only mentioned person or bot not all members",
        "usage": "{tr}add <username(s)/userid(s)>",
        "examples": "{tr}add @combot @MissRose_bot",
    },
)
async def get_users(event):
    legen_ = event.text[11:]
    legend_chat = legen_.lower
    restricted = ["@Legend_K_Userbot", "@Official_K_LegendBot"]
    await eor(event, f"**Inviting members from** {legen_}")
    if legend_chat in restricted:
        await event.edit(event, "You can't Invite Members from there.")
        await bot.send_message(
            "@Legend_K_Userbot", "Sorry for inviting members from here."
        )
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        LEGEND = await eor(event, "`processing...`")
    else:
        LEGEND = await eor(event, "`processing...`")
    if event.is_private:
        return await LEGEND.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await LEGEND.edit(
        "**⚜️[Terminal Status](https://t.me/Legend_K_Userbot)**\n\n`👨‍💻Inviting Users.......`"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            tol = f"@{user.username}"
            lol = tol.split("`")
            await legend(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await LEGEND.edit(
                f"🔰 **Inviting Users** 🔰\n\n**📜 Invited :**  `{s}` users \n**📜 Failed to Invite :**  `{f}` users.\n\n**👉 Error :**  `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await LEGEND.edit(
        f"[Terminal Finished](https://t.me/Legend_Userbot) \n\n🔸 Successfully Invited `{s}` ρєορℓє \n⚠️ Failed To Invite`{f}` ρєορℓє"
    )


@legend.legend_cmd(
    pattern="invitesall ([\s\S]*)",
    command=("invitesall", menu_category),
    info={
        "header": "Add the given user/users to the group where u used the command.",
        "description": "Adds only mentioned person or bot not all members",
        "usage": "{tr}add <username(s)/userid(s)>",
        "examples": "{tr}add @combot @MissRose_bot",
    },
)
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        LEGEND = await eor(event, "`processing...`")
    else:
        LEGEND = await eor(event, "`processing...`")
    if event.is_private:
        return await LEGEND.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await LEGEND.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await LEGEND.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            tol = user.id
            await legend(InviteToChannelRequest(channel=event.chat_id, users=[tol]))
            s = s + 1
            await LEGEND.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await LEGEND.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )
