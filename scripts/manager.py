#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from telethon.sync import TelegramClient, events
from plConfig import botc
from Color import Color
from plPlugins import switch
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class MyCli(TelegramClient):
    def __init__(self, session, api_id, api_hash):
        super().__init__(session, api_id, api_hash)
        self.connect()
        if not self.is_user_authorized():
            print(f'{Color.RED}- cannot connect to {session} session !{Color.RESET}')
        else:
            print(f'\n\n{Color.GRAY}- connect to {session} account !{Color.RESET}\n\n')
            self.me = self.get_me()
            self.start_showing_menu()
    def start_showing_menu(self):
        print(f'{Color.BLUE}- - - - - - - - - - - - - - - - - - - - - - - - -{Color.RESET}')
        print(f'{Color.GRAY}- show all chat id {Color.BLUE}[{Color.YELLOW} 1 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- show me {Color.BLUE}[{Color.YELLOW} 2 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- get account profile {Color.BLUE}[{Color.YELLOW} 3 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- get any account profile {Color.BLUE}[{Color.YELLOW} 4 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- get a media chat {Color.BLUE}[{Color.YELLOW} 5 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- show msgs in chat id {Color.BLUE}[{Color.YELLOW} 6 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- run codes in program {Color.BLUE}[{Color.YELLOW} 7 {Color.BLUE}]{Color.RESET}')
        print(f'{Color.GRAY}- exit {Color.BLUE}[{Color.YELLOW} 0 {Color.BLUE}]{Color.RESET}')

        cmd = input(f'\n{Color.BLUE}- enter = {Color.RESET}')
        switch(cmd, {
            '0':exit,
            '1':self.show_all_chat_id,
            '2':lambda:print(self.me.stringify()),
            '3':self.get_acc_profile,
            '4':self.get_profiles,
            '5':self.show_get_media,
            '6':self.show_msg_chat_id,
            '7':self.run_code
        }, lambda:print(f'{Color.RED}- error !{Color.RESET}'))()
        return self.start_showing_menu()
    
    def show_all_chat_id(self):
        for dialog in self.iter_dialogs():
            print(f'{Color.BLUE}[{Color.YELLOW} + {Color.BLUE}]{Color.GRAY} {dialog.name} {Color.CYAN}->{Color.LIGHT_BLUE} {dialog.id}{Color.RESET}')
    def run_code(self):
        print(f'{Color.RED}---- this is start code, to use var code: "self", to exit enter "exit" ! ----{Color.RESET}')
        while True:
            cmd = input('>>> ')
            if cmd == 'exit': break
            try:
                exec(cmd)
            except Exception as er:
                print(f'{Color.RED}{er}{Color.RESET}')
    
    def show_msg_chat_id(self):
        user_id = MyCli.checkchat(input(f'{Color.RED}- enter chat id = {Color.RESET}'))
        start = MyCli.getint(f'{Color.RED}- start msg id = {Color.RESET}')
        end = MyCli.getint(f'{Color.RED}- end = {Color.RESET}') or None
        for msg in self.iter_messages(user_id, end, offset_id=start):
            print(f'{Color.GRAY}- {"me" if msg.sender_id == self.me.id else msg.sender_id}:msgid={msg.id}{Color.RESET}\n', msg.raw_text, '\n- media !' if msg.media else '', sep='')

    def show_get_media(self):
        user_id = MyCli.checkchat(input(f'{Color.RED}- enter chat id = {Color.RESET}'))
        for msg in self.iter_messages(user_id):
            if msg.media:
                print(f'{Color.GRAY}- {"me" if msg.sender_id == self.me.id else msg.sender_id}::msgid={msg.id}{Color.RESET}')
                print(msg.media.stringify())
                cmd = input(f'- {Color.GRAY}- downlaod/break (y/n/b) ={Color.RESET} = ')
                if cmd == 'break':
                    break
                elif cmd == 'y':
                    print(f'{Color.BLUE}- wait !{Color.RESET}')
                    self.download_media(msg.media)
    
    def get_acc_profile(self):
        for photo in self.iter_profile_photos(self.me.id):
            self.download_media(photo)
    
    def get_profiles(self):
        user_id = MyCli.checkchat(input(f'{Color.RED}- enter chat id = {Color.RESET}'))
        for photo in self.iter_profile_photos(user_id):
            self.download_media(photo)
    
    def checkchat(chat: str):
        if chat[0] == '-' or chat.isdigit():
            return int(chat)
        return chat
    def getint(msg: str, er: str = f'{Color.RED}- enter an integer !{Color.RESET}'):
        try:
            print(msg,end='')
            return int(input())
        except ValueError:
            print(er)
            return MyCli.getint(msg, er)
# - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
if __name__ == '__main__':
    print(f'{Color.BLACK}\n{Color.BACKGROUND_RED}# ------------- [   Plague Dr.  ] ------------- #{Color.RESET}\n'+Color.DARK_GRAY)
    session_name = input(f'{Color.CYAN}- enter session name = {Color.RESET}')
    MyCli(botc.SESSION_DIR+session_name, botc.API_ID, botc.API_HASH)
else:
    print(f'{Color.BLACK}\n{Color.BACKGROUND_RED}# ------------- [   Plague Dr.  ] ------------- #{Color.RESET}\n'+Color.DARK_GRAY)
    print('\n\n- this is a test script to handle some functionality !')
    print('\n- to run, go to "plself" dir and enter cmd: "python3 scripts/manager.py" !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #