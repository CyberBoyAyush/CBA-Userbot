import asyncio
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern="purl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("**Reply to any document.**")
       return
    reply_message = await event.get_reply_message() 
    chat = "@FiletolinkTGbot"
    sender = reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1011636686))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@FiletolinkTGbot) u Nigga```")
              return
          await event.delete()
          await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)

@borg.on(admin_cmd(pattern="sgm ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("**Reply to an user message.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("**Reply to a message.**")
       return
    chat = "@sangmatainfo_bot"
    sender = reply_message.sender
    await event.edit("**Getting user's name history..**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@SangMataInfo_bot) u Nigga```")
              return
          await event.delete()
          await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)

@borg.on(admin_cmd(pattern="reader ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("**Reply to a URL.**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("**Reply to a url message.**")
       return
    chat = "@chotamreaderbot"
    sender = reply_message.sender
    await event.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=272572121))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@chotamreaderbot) u Nigga```")
              return
          await event.delete()
          await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)
        
        
@borg.on(admin_cmd(pattern="ad ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to media message```")
       return
    chat = "@audiotubebot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=507379365))
              await borg.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @AudioTubeBot and try again```")
              return
          await event.delete()
          await borg.send_file(event.chat_id, response.message.media)


""" tiktok downloaded plugin creted by @mrconfused and @sandy1709 
idea by @IMperialxx """

@borg.on(admin_cmd("tti ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")
    bot = "@HK_tiktok_BOT"
    
    async with borg.conversation("@HK_tiktok_BOT") as conv:
          try:
                await conv.send_message(d_link)
                cat1 = await conv.get_response()
                details = await conv.get_response()
                if details.text.startswith("Sorry"):
                     await borg.send_message(event.chat_id , "sorry . something went wrong" )
                     return
                cat2 = await conv.get_response()
                cat3 = await conv.get_response()
                await borg.send_file(event.chat_id, details, caption = details.text)
                await event.delete()
          except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")
            

@borg.on(admin_cmd("ttv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")
    bot = "@HK_tiktok_BOT"
    
    async with borg.conversation("@HK_tiktok_BOT") as conv:
          try:
                await conv.send_message(d_link)
                cat1 = await conv.get_response()
                details = await conv.get_response()
                if details.text.startswith("Sorry"):
                     await borg.send_message(event.chat_id , "sorry . something went wrong" )
                     return
                cat2 = await conv.get_response()
                cat3 = await conv.get_response()
                await borg.send_file(event.chat_id, cat3)
                await event.delete()
          except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")
            

@borg.on(admin_cmd("wttv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
        return
    else:
        await event.edit("doownloading your video")
    bot = "@HK_tiktok_BOT"
    
    async with borg.conversation("@HK_tiktok_BOT") as conv:
          try:
                await conv.send_message(d_link)
                cat1 = await conv.get_response()
                details = await conv.get_response()
                if details.text.startswith("Sorry"):
                     await borg.send_message(event.chat_id , "sorry . something went wrong" )
                     return
                cat2 = await conv.get_response()
                cat3 = await conv.get_response()
                await borg.send_file(event.chat_id, cat2)
                await event.delete()
          except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")   
            
@borg.on(sudo_cmd(pattern = "tti ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    await event.delete()
    if ".com" not in d_link:
        await event.reply("` I need a link to download something pro.`**(._.)**")
        return
    else:
        sandy =await event.reply("doownloading your video")
    bot = "@HK_tiktok_BOT"
    
    async with borg.conversation("@HK_tiktok_BOT") as conv:
          try:
                await conv.send_message(d_link)
                cat1 = await conv.get_response()
                details = await conv.get_response()
                if details.text.startswith("Sorry"):
                     await borg.send_message(event.chat_id , "sorry . something went wrong" )
                     return
                cat2 = await conv.get_response()
                cat3 = await conv.get_response()
                await borg.send_file(event.chat_id, details, caption = details.text)
                await sandy.delete()
          except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")
            

@borg.on(sudo_cmd(pattern = "ttv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    await event.delete()
    if ".com" not in d_link:
        await event.reply("` I need a link to download something pro.`**(._.)**")
        return
    else:
        sandy = await event.reply("doownloading your video")
    bot = "@HK_tiktok_BOT"
    
    async with borg.conversation("@HK_tiktok_BOT") as conv:
          try:
                await conv.send_message(d_link)
                cat1 = await conv.get_response()
                details = await conv.get_response()
                if details.text.startswith("Sorry"):
                     await borg.send_message(event.chat_id , "sorry . something went wrong" )
                     return
                cat2 = await conv.get_response()
                cat3 = await conv.get_response()
                await borg.send_file(event.chat_id, cat3)
                await sandy.delete()
          except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")
            

@borg.on(sudo_cmd(pattern = "wttv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    await event.delete()
    if ".com" not in d_link:
        await event.reply("` I need a link to download something pro.`**(._.)**")
        return
    else:
        sandy = await event.reply("doownloading your video")
    bot = "@HK_tiktok_BOT"
    
    async with borg.conversation("@HK_tiktok_BOT") as conv:
          try:
                await conv.send_message(d_link)
                cat1 = await conv.get_response()
                details = await conv.get_response()
                if details.text.startswith("Sorry"):
                     await borg.send_message(event.chat_id , "sorry . something went wrong" )
                     return
                cat2 = await conv.get_response()
                cat3 = await conv.get_response()
                await borg.send_file(event.chat_id, cat2)
                await sandy.delete()
          except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @HK_tiktok_BOT `and retry!`")   
            
CMD_HELP.update({"tiktok": "`.tti` <link> :\
      \nUSAGE: Shows you the information of the given tiktok video link.\
      \n\n `.ttv `<link>\
      \nUSAGE: Sends you the tiktok video of the given link without watermark\
      \n\n `.wttv `<link>\
      \n\nUSAGE: Sends you the tiktok video of the given link with watermark\
      "
})             


@borg.on(admin_cmd(pattern="connecter ?(.*)", allow_sudo=True))
async def _(event):
  if event.fwd_from:
    return
  if event.is_private:
    return
  chat_id = event.chat_id
  await event.client.send_message('missrose_bot', '/connect {}'.format(chat_id))
  await event.edit("[Connected](https://t.me/missrose_bot)")
  await asyncio.sleep(3)
  await event.delete()



