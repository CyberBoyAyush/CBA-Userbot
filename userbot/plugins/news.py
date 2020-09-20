# Copyright (C) By StarkGang [@STARKXD]
# Don't edit credits
# Works On Bases Of Cyberboysumanjay's Inshorts News Api
# Test

import requests
from var import Var
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply

newslog = Var.NEWS_CHANNEL_ID

@borg.on(admin_cmd("news (.*)"))
@borg.on(sudo_cmd("news (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Var.NEWS_CHANNEL_ID is None:
        await edit_or_reply(event, "`Please ADD NEWS_CHANNEL_ID For This Module To Work`")
        return
    infintyvar = event.pattern_match.group(1)
    main_url = f"https://inshortsapi.vercel.app/news?category={infintyvar}"
    await edit_or_reply(event, f"Ok ! Fectching {infintyvar} From inshortsapi Server And Sending To News Channel")
    starknews = requests.get(main_url).json()
    article = starknews["data"]
    results = []
    for ar in article:
            results.append(ar["content"])
            for item in starknews["data"]:
                sedlyf = item["content"]
                img = item["imageUrl"]
                writter = item["author"]
                dateis = item["date"]
                readthis = item["readMoreUrl"]
                titles = item["title"]
                sed1 = img
                sedm = (f"**Title : {titles}** \n{sedlyf} \nDate : {dateis} \nAuthor : {writter} \nReadMore : {readthis}")
                await borg.send_file(newslog, sed1, caption=sedm)
                await edit_or_reply(event, "All News Has Been Sucessfully Send To News Channel")
