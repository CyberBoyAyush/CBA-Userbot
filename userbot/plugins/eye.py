"""COMMAND : .eye"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="eye"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "eye":

    await event.edit("👁👁")

    animation_chars = [

            "👁👁\n  👄  =====> Gay & Lesbo",
            "👁👁\n  👅  =====> Muh faker",    
            "👁👁\n  💋  =====> coc sukker",
            "👁👁\n  👄  =====> dick head",
            "👁👁\n  👅  =====> Pussy face",    
            "👁👁\n  💋  =====> dickyfied dude",
            "👁👁\n  👄  =====> homos",
            "👁👁\n  👅  =====> Bhosdk",    
            "👁👁\n  💋  =====> coc & pusy less",
            "👁👁\n  👄  =====> Hi All, How Are You All..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
