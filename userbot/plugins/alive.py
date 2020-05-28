"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY STATUS** \n`FRIDAY➡️: ` **✅ Alive**\n\n"
                     f"`My Boss`: {DEFAULTUSER}\n\n"
                     "`Telethon version:` **6.0.9**\n`Python:` **3.7.4**\n"
                     "`Database Status:` **ALL NORMAL!WORKING FINE 🙂**\n\n`Always with you, my Boss!!\n`"
                     "**Satellite Name:** 🛰️HEROKUSAT-2🛰️\n"
                     "**Satellite Signal Strength:** -92 Db\n"
                     "**Satellite Staus:** ✅ Alive\n\n"
                     "     [❤️Deploy FRIDAY❤️](https://github.com/midhunkm1294-bit/FRIDAY)") 

