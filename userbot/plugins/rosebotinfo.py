import asyncio
import datetime
import time

from telethon import events
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

naam = str(ALIVE_NAME)

bot = "@MissRose_bot"


@borg.on(admin_cmd("roseinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                response = await conv.get_response()
                await conv.send_message("/info")
                audio = await conv.get_response()
                final = (
                    "If you would like to know more about this user, use /info <userid/username> in RoseBot.",
                    "",
                )
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_bot `and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                response = await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                final = (
                    "If you would like to know more about this user, use /info <username/userid> in RoseBot.",
                    "",
                )
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                response = await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                final = (
                    "If you would like to know more about this user go to PM hahahah.",
                    "",
                )
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
