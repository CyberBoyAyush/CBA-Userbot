"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
FRIDAY_IS_ALIVE = ("**F.R.I.D.A.Y** IS AT YOUR SERVICE❗\n\n"
                   "**I am Always Alive To Help You Boss**\n\n"
                   "**♧︎︎︎Currently Status♧︎︎︎** : `No Issue Found`\n\n"
                   "**♧︎︎︎Current Branch♧︎︎︎** : `master`\n\n"
                   "**♧︎︎︎Python Version♧︎︎︎** : `3.8`\n\n"
                   "**♧︎︎︎Friday OS♧︎︎︎** : `3.0 Snapdragon`\n\n"
                   "**♧︎︎︎Current Sat♧︎︎︎** : `StarkGangSat-2.0`\n\n"
                   f"**♧︎︎︎My Boss♧︎︎︎** : {DEFAULTUSER} \n\n"
                   "**♧︎︎︎Heroku Database♧︎︎︎** : `No Known Error Found`\n\n"
                   "**♧︎︎︎License♧︎︎︎** : [MIT Licence](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n\n"
                   "♧︎︎︎Copyright♧︎︎︎ : By [StarkGang@Github](GitHub.com/StarkGang)\n\n"
                   " [⌨︎Deploy FridayUserbot⌨︎](https://telegra.ph/FRIDAY-06-15)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, FRIDAY_IS_ALIVE) 
