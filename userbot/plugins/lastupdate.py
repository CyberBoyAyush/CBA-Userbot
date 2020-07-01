# Base by @Sur_Vivor And Idea And Created By @StarkxD
from telethon import events
from datetime import datetime
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd
from userbot.__init__ import Lastupdate
import time



@borg.on(admin_cmd(pattern="lastupdate"))
async def _(event):
    if event.fwd_from:
        return
    updatedtime = get_readable_time((time.time() - Lastupdate))
    await event.edit(f"🔼Last Updated or Restarted!\nOn : {updatedtime}")
