import time
from datetime import datetime

from telethon import events

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="pong ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    start = datetime.now()
    mone = await event.reply("💜🦄🍭Ping🍭🦄💜")
    end = datetime.now()
    ms = (end - start).microseconds * 0.00001
    await mone.edit("💜🦄Ping  Speed is💜🦄 `{} ms`".format(ms))


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


# @command(pattern="^.ping$")
@borg.on(admin_cmd(pattern="ping$"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("💜🦄🍭Pong💜🦄🍭")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"🦋💙Pong Speed is💙🦋 `{ms}` 💗")
