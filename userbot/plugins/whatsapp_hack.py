"""just for fun
.whatsapp"""

from telethon import events
import asyncio
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.8

   animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "whatsapp":

        await event.edit(input_str)

        animation_chars = [

             "Looking for WhatsApp databases in targeted person...",

            " User online: True\nTelegram access: True\nRead Storage: True ",

            "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s",

            "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s",

            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder 0/android/data/com.whatsApp`\nETA: 0m, 16s",    

            "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder 0/WhatsApp/Whatsapp Databases`\nETA: 0m, 14s",

            "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s",

            "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",

            "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",

            "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s",

            "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s",

            "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s",

            "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s",

            "Hacking complete!\nUploading file...",

            "Targeted Account Hacked by__ [__Ashmit__](https://t.me/Error404_INSaNE) __...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
