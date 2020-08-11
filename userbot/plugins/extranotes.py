from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"BF"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("`Main tera BoyFriend thu Meri GirlFriend!`")      
