# created by Jisan


import asyncio
import importlib.util
import logging
import os
import random
import re
import sys
from collections import deque

from telethon import events

from userbot import ALIVE_NAME, CMD_HELP, utils
from userbot.utils import admin_cmd

DEF = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@borg.on(admin_cmd(pattern="kilr (.*)"))
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
