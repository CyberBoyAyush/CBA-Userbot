"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
FRIDAY_IS_ALIVE = ("**F.R.I.D.A.Y** IS AT YOUR SERVICE❗\n\n"
                   "**💻Currently Status💻** : `No Issue Found`\n"
                   "**🌐Current Branch🌐** : `master`\n"
                   "**🐍Python Version🐍** : `3.8`\n"
                   "**Friday Os** : `2.0`\n"
                   f"**❤️My Boss❤️** : {DEFAULTUSER} \n"
                   "**❗Updates❗** : [Check Here](t.me/fridaysupportofficial)\n"
                   " [⚡Deploy Friday Userbot⚡](https://telegra.ph/FRIDAY-06-15)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, FRIDAY_IS_ALIVE) 
