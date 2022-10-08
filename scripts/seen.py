#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetMessagesViewsRequest
from plConfig import Conf
from Color import Color
import os
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
print(f'{Color.BLACK}\n{Color.BG_RED}# ------------- [   Plague Dr.  ] ------------- #{Color.RESET}\n') 
api_id = Conf.API_ID
api_hash = Conf.API_HASH
print(Color.BLUE,'* '*10,Color.RED)
for m in os.listdir(Conf.SESSION_DIR):
    print(m[:m.rfind('.')])
print(Color.BLUE,'* '*10,Color.RESET)
chats = input(Color.GRAY+'- enter sessions = '+Color.RESET).split()
ch = input(Color.GRAY+'- enter chat = '+Color.RESET)
i = int(input(Color.GRAY+'- msgs (int) ? '+Color.RESET))
print(Color.BLUE,'* '*10,Color.RESET)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def main(peer):
    bot = TelegramClient(peer, api_id, api_hash)
    bot.connect()
    print(f'{Color.BLUE}[ + ] {Color.RED}connect to {peer} account!{Color.RESET}')
    msg_id = [msg.id for msg in bot.iter_messages(ch, i)]
    bot(GetMessagesViewsRequest(ch,msg_id, increment=True))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == '__main__':
    for chat in chats:
        main(Conf.SESSION_DIR+chat)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #