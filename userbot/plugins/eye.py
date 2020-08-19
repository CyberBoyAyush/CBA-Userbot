"""COMMAND : .eye"""

import asyncio

from telethon import events

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="eye"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    # input_str = event.pattern_match.group(1)

    # if input_str == "eye":

    await event.edit("👁👁")

    animation_chars = [
        "👁👁\n  👄  =====> Gays",
        "👁👁\n  👅  =====> Lesbos",
        "👁👁\n  💋  =====> Crakers",
        "👁👁\n  👄  =====> Jokers",
        "👁👁\n  👅  =====> Fools",
        "👁👁\n  💋  =====> Idiots",
        "👁👁\n  👄  =====> Stupids",
        "👁👁\n  👅  =====> Harami Creatures",
        "👁👁\n  💋  =====> Crazys",
        "👁👁\n  👄  =====> Hi All🧚🏻💚, How Are You All🧚🏻💚...",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
