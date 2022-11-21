#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from dotenv import load_dotenv
import os, json as js
load_dotenv()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class Conf:
    API_ID = int(os.getenv('API_ID'))
    API_HASH = os.getenv('API_HASH')
    acc_sudo = js.loads(os.getenv('acc_sudo'))
    main_sudo = js.loads(os.getenv('main_sudo'))
    main_sudo.extend(acc_sudo)
    sudoS = js.loads(os.getenv('sudoS'))
    sudoS.extend(main_sudo)
    CHANNEL_FOR_FWD = int(os.getenv('CHANNEL_FOR_FWD'))
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    BOT_USERNAME = os.getenv('BOT_USERNAME')
    INSTAGRAM = js.loads(os.getenv('INSTAGRAM'))
    REDIS_NUMBER = int(os.getenv('REDIS_NUMBER'))
    SESSION_AC_NAME = os.getenv('SESSION_AC_NAME')
    SESSION_API_NAME = os.getenv('SESSION_API_NAME')
    COMMAND_PREFIX = js.loads(os.getenv('COMMAND_PREFIX'))
    SESSION_DIR = 'data/SeSioNS/'
    DOWNLOAD_DIR = 'data/Downloads/'
    RADIO_STATIONS = {"Iran International": 'https://n09.radiojar.com/dfnrphnr5f0uv',
                      "BOX : Lofi Radio - Chill study & sleep beats": 'https://play.streamafrica.net/lofiradio',
                      "Radio Javan": 'https://rj1.rjstream.com/',
                      "Radio Faaz": 'https://onlineradiobox.com/json/de/faaz/play?platform=web',
                      }
    version = '0.7.8'
    STR_HELP_BOT = f'''**°• WlC 2 Th source help page! | pl-self v.{version} •°
 - Warning: Only sudo account and sudo\'s can use this system.**
• Sudo\'s :
■ `join [LINK]` **// Join Th GrouP**
□ `left [LINK]` **// Join Th GrouP**
■ `id [DEFAULT/REPLY]` **// get the user ID**
□ `reload` **// ReStarT Th PrograM**
■ `tr [fa/en/ru/..] [TEXT]` **// Includes three sections: command, language type and text**
□ `time` **// GeT TIME/DATE**
■ `acdontsave` **// You know what talking about !**
□ `del [REPLY]` **//Delet# a messag3**
■ `mute/unmute [REPLY]` **// In the group, it can be muted/unmuted by replying to a person - \"Only sudo account can mute/unmute someone in private\"**
□ `ban [REPLY]` **// In the group, it can be baned by replying to a person**
■ `ping` **// get ping server in milliseconds**
□ `block/unblock [REPLY]` **// Sudo account can block/unblock someone with this command**
■ `rmsg [NUMBER]` **// delete msg**
□ `lasttime [ON/OFF]`
**#plagueDr**'''
    KOS_FoSH = []  # add msgs to floot spam !
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #