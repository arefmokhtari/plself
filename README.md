*lastest out of version 1.0, now version 0.7 !*

# ** plSelF - [ plague Dr .] **

> A Telegram UserBot based on [Telethon](https://github.com/LonamiWebs/Telethon)

### bot commands are available in the help cmd !

*note: This script must be run in a Linux environment (to access and Scriptlibraries)*

*note: to use 'pytgcalls' in version 0.7 project, python3 version must be < 3.10*

## Tutorial

<details>

> You need an API_ID & API_HASH to generate a telethon session. get the APP ID and API Hash
> at [my.telegram.org](https://my.telegram.org)


</details>

## Requirements

You're gonna need to get the following programs and services installed on your server.

```
apt install python3
apt install screen
apt install python3-pip
apt install redis
apt install ffmpeg
apt install nodejs
```

## - first, fill '.env' to set the complete config

# config:

* API_ID && API_HASH :  set ur API
* acc_sudo :  user_ids, account like channel account to chat group or ...
* main_sudo :  full account access in the form of a sudo, not an account !
* sudoS :  access to some commands, all these options can be set in the script ...
* CHANNEL_FOR_FWD :  sometimes the script needs a chat_id for forwarding or sending a message or data!
* BOT_TOKEN && BOT_USERNAME :  set ur API bot(need a inline)
* INSTAGRAM :  set ur or any instagram account
* REDIS_NUMBER : number os redis BataBase
* SESSION_AC_NAME && SESSION_API_NAME :  ur|API session name

# install libs:

```pip3 install -U -r requirements.txt```

*- database manager: run 'python3 scripts/databaseManager.py' !*

# RUN shell script:

```screen ./launch.sh```

# Other provisions will definitely be added to this section
