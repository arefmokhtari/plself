
# PlSelF [ Plague Dr ]

> A Telegram UserBot based on [Telethon](https://github.com/LonamiWebs/Telethon)

 The instructions can be found in the `help` command

▸ Note: This script must be run in a Linux environment


## Requirements

You're gonna need to get the following programs and services installed on your PC or server.

* python3
* pip
* redis
* ffmpeg
* git
* nodejs (version >= 15.0.0)(needed for voice chat player)
* screen (optional but recommended)


#### Debian/Ubuntu/Linux Mint
```
sudo apt update
sudo apt install python3 python3-pip screen redis ffmpeg git
```

### Arch Linux
```
sudo pacman -Syyu
sudo pacman -S python3 python-pip screen redis ffmpeg git
```

To install the latest version of [nodejs](https://github.com/nvm-sh/nvm#installing-and-updating), enter this commands in your terminal
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
nvm install node && nvm use node
```

#### › Fill the 'config.env' file with the required information


### Config vars:

* API_ID & API_HASH : Get this from [me.telegram.org/apps](me.telegram.org/apps)
  <details>

    > You need an API_ID & API_HASH to use this UserBot.
    >
    > Get the APP ID and API Hash at [my.telegram.org](https://my.telegram.org/apps)
    >
    > If you need help, [read this](https://telegra.ph/How-to-get-Telegram-APP-ID--API-HASH-02-08)
  </details>
* acc_sudo: The UserBot ID (and chat id if you want to chat as a channel or chat Anonymously)
* main_sudo: Other accounts you want to have full access to the Userbot
* sudoS: Access to some commands, all these options can be set in the script ...
* CHANNEL_FOR_FWD: Create a channel and pass its id to this variable
  ###### Inline API Bot
    > search @botfather in telegram <br>
    > send /newbot <br>
    > then enter bot name like plague Dr <br>
    > enter bot username like plselfbot <br>
    > then you will get bot token <br>
    > type /mybots and send <br>
    > choose your bot <br>
    > click Bot Settings <br>
    > then click Inline Mode <br>
    > The button should appear as Turn On <br>
    > click it, it will show Turn Off (means its turned on) <br>
    > Done, copy the bot token and username!! 
 
* BOT_TOKEN: The token you copied from bot father
* BOT_USERNAME:  the username you copied from bot father
* INSTAGRAM:  Your instagram account username and password (example: `["AnyName", "username", "password"]`)
* REDIS_NUMBER: If you don't know what this is, just enter a random number between 1 and 15
* SESSION_AC_NAME: Your account session will be saved with this name
* SESSION_API_NAME :  Your inline bot session will be saved with this name

## Installation and Deployment
```
git clone https://github.com/arefmokhtari/plself.git
cd plself

# - optional -
virtualenv venv
source venv/bin/activate
# - optional -

pip3 install -r requirements.txt

# Fill the 'config.env' file with the required information and then run this command
mv config.env .env

sudo chmod 700 launch.sh
screen ./launch.sh

```

<hr>

* database manager: `python3 scripts/databaseManager.py`
* account manager: `python3 scripts/manager.py`
