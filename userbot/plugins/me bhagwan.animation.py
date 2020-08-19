# (c) @UniBorg
import asyncio
from collections import deque

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.me animation", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list(" ꧁༒☆ ✞ b♥h♥a♥g♥w♥a♥n♥✞ ☆༒꧂  "))
    for _ in range(35):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(5)
