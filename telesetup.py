from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print(""" To Friday String Generator By StarkGang""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = '1754367'
API_HASH = "231b8cc6cca12ee51a85cf543321f476"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` And Visit @FridayOT For Any Help !")
      print("You telegramString session successfully stored in your telegram, please check your Telegram Saved Messages ")
      print("Store it safe !!")
  except:
   print ("")
   print ("Wrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry")
   print ("")
   continue
  break
    
= 
