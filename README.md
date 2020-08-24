# FRIDAY-USERBOT

<p align="center">
<img src="https://telegra.ph/file/fc3aef09eb9b82d244f97.jpg" alt="CBA Userbot">


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



*Best User Bot To Manage Your Telegram Account🔥 *
## Most PowerFul And Better And Secure

## This Repo Owned By🔥
* [@CYBERBOYAYUSH](https://telegram.dog/CyberBoyAyush)
* [@XHACKERZKALI](https://telegram.dog/XHACKERZKALI)

## We Are Not Responsible For Any Banning Of Acc So Deploy On Your Own Risk😒

### Host CBA - Userbot In Heroku (On Your Own Risk)

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/CyberBoyAyush/CBA-Userbot)

## Online Telegram-String Generator

[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://cba-userbot.cyberboyayush.repl.run)


### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/starkGang/Fridayuserbot
cd FridayUserbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```


### UniBorg Configuration


The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

## Credits😎
* [CyberBoyAyush](https://Telegram.dog/CyberBoyAyush) Onwer Of This Repo🔥
* [XHackerzKali](https://telegram.dog/Xhackerzkali) Helping Me😎
* [StarkXD](https://telegram.dog/StarkXD) For FRIDAY Repo🙏
