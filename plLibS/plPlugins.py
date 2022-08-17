#                   [   Plague Dr.  ]
import os, random, re
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
CoDMORsE = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..", 'e' : ".", 'f' : "..-.", 'g' : "--.", 'h' : "....", 'i' : "..", 'j' : ".--", 'k' : "-.-", 'l' : ".-..", 'm' : "--", 'n' : "-.", 'o' : "---", 'p' : ".--.", 'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-", 'u' : "..-", 'v' : "...-", 'w' : ".--", 'x' : "-..-", 'y' : "-.--", 'z' : "--..", ' ' : ' ', '1':  ".---", '2':  "..---", '3': "...--", '4':  "....-",'5': ".....", '6':  "-....", '7': "--...", '8':  "---..", '9':  "----.", '0': "-----", '۱':  ".---", '۲':  "..---", '۳': "...--", '۴':  "....-", '۵': ".....", '۶':  "-....", '۷': "--...", '۸':  "---..", '۹':  "----.", '۰': "-----", 'آ' : '.-', 'ا' : '.-', 'ب' : '-...', 'پ' : '.--.', 'ت' : '-', 'ث' : '-.-.', 'ج' : '.---', 'چ' : '---.', 'ح' : '....', 'خ' : '-..-', 'د' : '-..', 'ذ' : '...-', 'ر' : '.-.', 'ز' : '--..', 'ژ' : '--.', 'س' : '...', 'ش' : '----', 'ص' : '.-.-', 'ض' : '..-..', 'ط' : '..-', 'ظ' : '-.--', 'ع' : '---', 'غ' : '..--', 'ف' : '..--', 'ق' : '..-.', 'ک' : '-.-', 'گ' : '--.-', 'ل' : '.-..', 'م' : '--', 'ن' : '.-', 'و' : '.--', 'ه' : '.', 'ی' : '..', '\n':'\n'}
# - - - - - - - - - - - -FuncTioN- - - - - - - - - - - #
async def _exec(code, event, Client): # a memento from my friend, Andy =D
    exec(f"async def __exec(event, Client): " + "".join(f"\n {x}" for x in code.split("\n")))
    return await locals()["__exec"](event, Client)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def fileindir(pattern: str, dirlist: os.listdir) -> list: 
    return [FilE for FilE in dirlist if FilE.startswith(pattern)]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def findfile(filename, dir):    
    for root, dirs, files in os.walk(dir):
        for file in files: 
            if file.startswith(filename):
                return (str(file))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def check_insta(instaobj, *, session, username, passwd):
    print('\t- insta : ', end='')
    if findfile(session, os.getcwd()+'/data/SeSioNS'):
        instaobj.load_session_from_file(username, os.getcwd()+'/data/SeSioNS/'+session)
    else:
        instaobj.login(username, passwd)
        instaobj.save_session_to_file(os.getcwd()+'/data/SeSioNS/'+session)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def checklist4insta(pattern: str) -> bool:
    if pattern.endswith('xz') or pattern.endswith('txt') or pattern.endswith('json'):
        return False
    return True
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def switch(search: object, sdict: dict, default: object):
    return sdict.get(search, default)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def isexistList(inli: list, index: int) -> bool:
    try:
        inli[index]
        return True
    except:
        return False
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def create_rend_name(num: int) -> str:
    return str().join(chr(random.randint(97, 122)) for _ in range(num))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def check_link(link: str, *, ptrn): # l s
    if ptrn == 'l':
        return 'https://t.me/joinchat/'+link[link.rfind('/')+2:] if link[link.rfind('/')+1] == '+' else link
    elif ptrn == 's':
        if '/+' in link or re.search('joinchat/', link):
            return True
        return False
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def check_msg_link(msg: str) -> bool: 
    if re.search("https", msg) or re.search("http", msg) or re.search("t.me", msg) or re.search("www", msg):
        return True
    return False  
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def user_in_channel(bot, chat, user, UserNotParticipantError) -> bool:
    try:
        await bot.get_permissions(chat, user)
        return True
    except UserNotParticipantError:
        return False
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def is_ASCII(msg: str) -> bool:
    for ch in msg:
        c = ord(ch)
        if c >= 97 and c <= 122:
            return True
    return False
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def edit_source_run(code: str, file: str):
    with open(file, 'w') as f:
        f.write(code)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def get_cmds(event):
    cmd = event.raw_text.lower().split()
    len_cmd = len(cmd)
    return [cmd, len_cmd]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def send_sudo_msg(event, message, Account):
    return await event.edit(message) if event.sender_id in Account else await event.reply(message)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #