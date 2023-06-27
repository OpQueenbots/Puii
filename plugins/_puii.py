# Puii - UserBot
# Copyright (C) 2021-2022 TeamPuii
#
# This file is a part of < https://github.com/TeamPuii/Puii/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamPuii/Puii/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, puii_cmd

REPOMSG = """
• **SANGRAM USERBOT** •\n

• Addons - [Click Here](https://github.com/OpQueenbots/PuiiAddons)
• Support - @Kalakar_Sangram
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/OpQueenbots/Puii"),
        Button.url("Addons", "https://github.com/OpQueenbots/Puiiaddons"),
    ],
    [Button.url("Support Group", "t.me/Red_Wine_Op")],
]

ULTSTRING = """🎇 **Thanks for Deploying Sangram Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@puii_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@puii_cmd(pattern="puii$")
async def usePuii(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/be5258ef33dfe5d4d9a9a.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
