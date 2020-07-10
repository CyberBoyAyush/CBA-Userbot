"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# @starkxD
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_STCR = "CAACAgUAAxkBAAEFV6hfCEIhhQWhfbgzIylxK5js-y8lSAACqgEAAk9GSVQg8HoXyWQxsxoE"
FRIDAY_ALIVE = ("`FRIDAY IS:` **ONLINE**\n\n"
"**SYSTEM STATUS**\n\n"
"`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n\n"
"`DATABASE STATUS:` **Functional**\n\n"
"**Current Branch** : `master`\n\n"
"**Friday OS** : `3.14`\n\n"
"**Current Sat** : `StarkGangSat-2.25`\n\n"
f"**My Boss** : {DEFAULTUSER} \n\n"
"**Heroku Database** : `AWS - Working Properly`\n\n"
"**License** : [MIT Licence](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n\n"
"Copyright By [StarkGang@Github](GitHub.com/StarkGang)\n\n"
"[Deploy FridayUserbot](https://telegra.ph/FRIDAY-06-15)")

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(alive):

    chat = await alive.get_chat()

    await alive.delete()

    """ For .alive command, check if the bot is running.  """

    await borg.send_sticker(chat, ALIVE_STCR)
    await borg.send_message(chat, FRIDAY_ALIVE)
