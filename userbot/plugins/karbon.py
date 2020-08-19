"""Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .kar1 //as a reply to any text message
usage: .kar2 //as a reply to any text message
usage: .kar3 //as a reply to any text message
usage: .kar4 //as a reply to any text message
usage: .rgbk2//as a reply to any text message
usage: .kargb //as a reply to any text message
usage: .karpp //your profile pic will be setted
Thanks to @r4v4n4 for vars"""

from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from telethon import events
from urllib.parse import quote_plus
from urllib.error import HTTPError
from time import sleep
import asyncio
import os
import random
from datetime import datetime
from telethon.tl import functions
from userbot.utils import admin_cmd
import shutil
from PIL import Image, ImageDraw, ImageFont
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@borg.on(admin_cmd(pattern=f"kar1", outgoing=True))
async def carbon_api(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("🔲🔲🔲🔲🔲")
        CARBON = 'https://carbon.now.sh/?bg=rgba(249%2C237%2C212%2C0)&t=synthwave-84&wt=none&l=application%2Fjson&ds=true&dsyoff=20px&dsblur=0px&wc=true&wa=true&pv=56px&ph=0px&ln=false&fl=1&fm=IBM%20Plex%20Mono&fs=14.5px&lh=153%25&si=false&es=4x&wm=false&code={code}'
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option('prefs', prefs)
        await e.edit("🔳🔳🔲🔲🔲")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        download_path = './'
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_path}}
        command_result = driver.execute("send_command", params)

        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        sleep(3)  # this might take a bit.
       # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
       # sleep(5)
       # await e.edit("🔳🔳🔳🔲🔲")
    #  driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(3)  # Waiting for downloading

        await e.edit("🔳🔳🔳🔳🔳")
        file = './carbon.png'
        await e.edit("☣️Karbon1 Completed, Uploading Karbon☣️")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=f"Here's your Karbon1 ",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove('./carbon.png')
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


@borg.on(admin_cmd(pattern=f"kar2", outgoing=True))
async def carbon_api(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("📛📛📛📛📛")
        CARBON = 'https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}'
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option('prefs', prefs)
        await e.edit("🔘🔘📛📛📛")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        download_path = './'
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_path}}
        command_result = driver.execute("send_command", params)

        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        sleep(5)  # this might take a bit.
       # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
        # sleep(5)
        await e.edit("🔘🔘🔘📛📛")
        # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(5)  # Waiting for downloading

        await e.edit("🔘🔘🔘🔘🔘")
        file = './carbon.png'
        await e.edit("☣️Karbon2 Completed, Uploading Karbon☣️")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=f"Here's your Karbon2",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove('./carbon.png')
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


@borg.on(admin_cmd(pattern=f"kar3", outgoing=True))
async def carbon_api(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("🎛🎛🎛🎛🎛")
        CARBON = 'https://carbon.now.sh/?bg=rgba(74%2C144%2C226%2C1)&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option('prefs', prefs)
        await e.edit("🔵🔵🎛🎛🎛")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        download_path = './'
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_path}}
        command_result = driver.execute("send_command", params)

        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        sleep(5)  # this might take a bit.
       # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
        # sleep(5)
        await e.edit("🔵🔵🔵🎛🎛")
       # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(5)  # Waiting for downloading

        await e.edit("🔵🔵🔵🔵🔵")
        file = './carbon.png'
        await e.edit("☣️Karbon3 Completed, Uploading Karbon⬆️")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=f"Here's your Karbon3",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove('./carbon.png')
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


@borg.on(admin_cmd(pattern=f"kar4", outgoing=True))
async def carbon_api(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("🌚🌚🌚🌚🌚")
        CARBON = 'https://carbon.now.sh/?bg=rgba(29%2C40%2C104%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}'
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option('prefs', prefs)
        await e.edit("🌝🌝🌚🌚🌚")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        download_path = './'
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_path}}
        command_result = driver.execute("send_command", params)

        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        sleep(5)  # this might take a bit.
        # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
       # sleep(5)
        await e.edit("🌝🌝🌝🌚🌚")
        # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(5)  # Waiting for downloading

        await e.edit("🌝🌝🌝🌝🌝")
        file = './carbon.png'
        await e.edit("✅Karbon4 Completed, Uploading Karbon✅")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=f"Here's your Karbon4 ",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )

        os.remove('./carbon.png')
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


@borg.on(admin_cmd(pattern=f"rgbk2", outgoing=True))
async def carbon_api(e):
    RED = random.randint(0, 256)
    GREEN = random.randint(0, 256)
    BLUE = random.randint(0, 256)
    OPC = random.random()
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("⬜⬜⬜⬜⬜")
        CARBON = 'https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C{O})&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, R=RED, G=GREEN,
                            B=BLUE, O=OPC, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option('prefs', prefs)
        await e.edit("⬛⬛⬜⬜⬜")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        download_path = './'
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_path}}
        command_result = driver.execute("send_command", params)

        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        sleep(5)  # this might take a bit.
       # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
        # sleep(5)
        await e.edit("⬛⬛⬛⬜⬜")
        # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(5)  # Waiting for downloading

        await e.edit("⬛⬛⬛⬛⬛")
        file = './carbon.png'
        await e.edit("✅RGB Karbon 2.0 Completed, Uploading Karbon✅")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=f"Here's your karbonrgb",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )
        os.remove('./carbon.png')
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


@borg.on(admin_cmd(pattern=f"kargb", outgoing=True))
async def carbon_api(e):
    RED = random.randint(0, 256)
    GREEN = random.randint(0, 256)
    BLUE = random.randint(0, 256)
    THEME = ["3024-night",
             "a11y-dark",
             "blackboard",
             "base16-dark",
             "base16-light",
             "cobalt",
             "dracula",
             "duotone-dark",
             "hopscotch",
             "lucario",
             "material",
             "monokai",
             "night-owl",
             "nord",
             "oceanic-next",
             "one-light",
             "one-dark",
             "panda-syntax",
             "paraiso-dark",
             "seti",
             "shades-of-purple",
             "solarized",
             "solarized%20light",
             "synthwave-84",
             "twilight",
             "verminal",
             "vscode",
             "yeti",
             "zenburn",
             ]

    CUNTHE = random.randint(0, len(THEME) - 1)
    The = THEME[CUNTHE]

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("⬜⬜⬜⬜⬜")
        CARBON = 'https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C1)&t={T}&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
        CARBONLANG = "en"
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        url = CARBON.format(code=code, R=RED, G=GREEN,
                            B=BLUE, T=The, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option('prefs', prefs)
        await e.edit("⬛⬛⬜⬜⬜")

        driver = webdriver.Chrome(
            executable_path=Config.CHROME_DRIVER, options=chrome_options)
        driver.get(url)
        download_path = './'
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_path}}
        command_result = driver.execute("send_command", params)

        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        sleep(5)  # this might take a bit.
    #  driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
       # sleep(5)
        await e.edit("⬛⬛⬛⬜⬜")
        # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
        sleep(5)  # Waiting for downloading

        await e.edit("⬛⬛⬛⬛⬛")
        file = './carbon.png'
        await e.edit("✅RGB Karbon Completed, Uploading Karbon✅")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=f"Here's your karbonrgb",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )
        os.remove('./carbon.png')
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg


"""
@borg.on(admin_cmd(pattern=f"karpp", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.karpp", outgoing=True))
async def carbon_api(e):
 while True:
   kpp= 'karbonpp.png'
   RED = random.randint(0,256)
   GREEN = random.randint(0,256)
   BLUE = random.randint(0,256)
   THEME= [         "3024-night",
                    "a11y-dark",
                    "blackboard",
                    "base16-dark",
                    "base16-light",
                    "cobalt",
                    "dracula",
                    "duotone-dark",
                    "hopscotch",
                    "lucario",
                    "material",
                    "monokai",
                    "night-owl",
                    "nord",
                    "oceanic-next",
                    "one-light",
                    "one-dark",
                    "panda-syntax",
                    "paraiso-dark",
                    "seti",
                    "shades-of-purple",
                    "solarized",
                    "solarized%20light",
                    "synthwave-84",
                    "twilight",
                    "verminal",
                    "vscode",
                    "yeti",
                    "zenburn",
]

   CUNTHE = random.randint(0, len(THEME) - 1)
   The = THEME[CUNTHE]


   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
 
   #await e.edit("⬜⬜⬜⬜⬜")
     CARBON = 'https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C1)&t={T}&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
     CARBONLANG = "en"
     textx = datetime.now().strftime(" {DEFAULTUSER} \n  ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡\n      Time: %H¦%M¦%S \n      Date: %d/%m/%y")
     pcode = e.text
     if pcode[8:]:
           pcode = str(pcode[8:])
     elif textx:
           pcode = str(textx) # Importing message to module
     code = quote_plus(pcode) # Converting to urlencoded
     url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, T=The, lang=CARBONLANG)
     chrome_options = Options()
     chrome_options.add_argument("--headless")
     chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
     chrome_options.add_argument("--window-size=1920x1080")
     chrome_options.add_argument("--disable-dev-shm-usage")
     chrome_options.add_argument("--no-sandbox")
     chrome_options.add_argument('--disable-gpu')
     prefs = {'download.default_directory' : './'}
     chrome_options.add_experimental_option('prefs', prefs)

     driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER, options=chrome_options)
     driver.get(url)
     download_path = './'
     driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
     params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
     command_result = driver.execute("send_command", params)

     driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
     sleep(5) # this might take a bit.
     driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
     sleep(5)
     driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
     sleep(5) #Waiting for downloading

     file = './carbon.png'
     photo = Image.open(file)
     photo.save(kpp)
     ppic = await e.client.upload_file(kpp)
     await e.client(functions.photos.UploadProfilePhotoRequest(
           ppic
           ))
   
     os.remove(kpp)
     os.remove(file)
     await asyncio.sleep(45)
"""
