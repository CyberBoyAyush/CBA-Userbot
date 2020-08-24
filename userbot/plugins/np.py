"""Emoji
Available Commands:
.nope
Credits to @mariodevs
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("nope"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "nope":
    await event.edit("nope")
    animation_chars = [
            "No",
            "Problem",
            "Bsdk",
            "Yeah ! No problem Bsdk",
            "No Problem Bsdk.lol",
            "No Problem Bsdk😇.Lol",
            "No Problem Bsdk😇.Gaand Maraa🖕"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
