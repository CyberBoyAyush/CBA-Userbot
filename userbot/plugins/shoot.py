# created by Jisan


from telethon import events
import asyncio
import os
import logging
import random
import sys
from userbot import utils
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP
import random
import re
import importlib.util
from collections import deque

DEF = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@borg.on(admin_cmd(pattern="shoot (.*)"))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    animation_interval = 0.7
    animation_ttl = range(0, 12)
    await event.edit(f"**Ready Commando **__{DEF}....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        f"__**Commando **__{DEF}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**Commando **__{DEF}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**Commando **__{DEF}         \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - -\n _/﹋\_\n",
        f"__**Commando **__{DEF}         \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**Commando **__{DEF}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**Commando **__{DEF}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**Commando **__{DEF}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - - {name}\n _/﹋\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])
