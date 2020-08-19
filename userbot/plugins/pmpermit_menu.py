# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio
import io
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if not event.is_private:
            return
        Nudas = ("__Please state your gender.__\n"
                 "`1`. 🧟‍♀️Female Homo-Sapien\n"
                 "`2`. 🧟‍♂️Male Homo-Sapien\n"
                 "`3`. 🙈Other\n")
        PM = ("`🧚‍♀️Heyyy🧚‍♀️. You are accessing the availabe menu of my master🧚‍♀️,`"
              f"{DEFAULTUSER}.🧛‍♂️\n"
              "__🧚‍♂️Let's make this smooth and let me know why you are here🧚‍♀️.__\n"
              "**🧚‍♂️Choose one of the following reasons why you are here🧚‍♂️:**\n\n"
              "`1`. 🧜‍♀️To chat with my master🧜‍♀️\n"
              "`2`. 🧜‍♀️To spam my master's inbox.🧜‍♀️\n"
              "`4`. 🧝‍♂️To enquire something🧝‍♂️\n"
              "`5`. 🧝‍♂️MuhfAker girls seeker_pm nibba\n")
        ONE = ("__Okay🧞‍♀️. Your request has been registered🧞‍♀️. Do not spam my master's inbox.You can expect a reply within 24 light years🧞‍♀️. He is a busy man, unlike you probably🧞‍♀️.__\n\n"
               "**⚓🧜‍♀️You will be blocked and reported if you spam nibba.🌪🧞‍♀️⚠️**\n\n"
               "__Use__ `/start` __to go back to the main menu.__")
        TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**So uncool, this is not your home. Go bother someone else. You have been blocked and reported until further notice.**")
        FOUR = ("__Okay. My master has not seen your message yet.He usually responds to people,though idk about retarted ones.__\n __He'll respond when he comes back, if he wants to.There's already a lot of pending messages😶__\n **Please do not spam unless you wish to be blocked and reported.**")
        FIVE = ("`Okay. please have the basic manners as to not bother my master too much. If he wishes to help you, he will respond to you soon.`\n**Do not ask repeatdly else you will be blocked and reported.**")
        LWARN = ("**This is your last warning. DO NOT send another message else you will be blocked and reported. Keep patience. My master will respond you ASAP.**\n__Use__ `/start` __to go back to the main menu.__")

        async with borg.conversation(chat) as conv:
            await borg.send_message(chat, PM)
            chat_id = event.from_id
            response = await conv.get_response(chat)
            y = response.text
            if y == "1":
                await borg.send_message(chat, ONE)
                response = await conv.get_response(chat)
                await event.delete()
                if not response.text == "/start":
                    await response.delete()
                    await borg.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    await event.delete()
                    await response.delete()
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif y == "2":
                await borg.send_message(chat, LWARN)
                response = await conv.get_response(chat)
                if not response.text == "/start":
                    await borg.send_message(chat, TWO)
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat_id))
            elif y == "4":
                await borg.send_message(chat, FOUR)
                response = await conv.get_response(chat)
                await event.delete()
                await response.delete()
                if not response.text == "/start":
                    await borg.send_message(chat, LWARN)
                    await event.delete()
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif y == "5":
                await borg.send_message(chat, FIVE)
                response = await conv.get_response(chat)
                if not response.text == "/start":
                    await borg.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            else:
                await borg.send_message(chat, "`You have entered an invalid command. Please send /start again or do not send another message if you do not wish to be blocked and reported.`")
                response = await conv.get_response(chat)
                z = response.text
                if not z == "/start":
                    await borg.send_message(chat, LWARN)
                    await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
