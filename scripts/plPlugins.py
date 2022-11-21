#                   [   Plague Dr.  ]
import os, random, re
from speedtest import Speedtest
import speech_recognition as sr 
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
CoDMORsE = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..", 'e' : ".", 'f' : "..-.", 'g' : "--.", 'h' : "....", 'i' : "..", 'j' : ".--", 'k' : "-.-", 'l' : ".-..", 'm' : "--", 'n' : "-.", 'o' : "---", 'p' : ".--.", 'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-", 'u' : "..-", 'v' : "...-", 'w' : ".--", 'x' : "-..-", 'y' : "-.--", 'z' : "--..", ' ' : ' ', '1':  ".---", '2':  "..---", '3': "...--", '4':  "....-",'5': ".....", '6':  "-....", '7': "--...", '8':  "---..", '9':  "----.", '0': "-----", '۱':  ".---", '۲':  "..---", '۳': "...--", '۴':  "....-", '۵': ".....", '۶':  "-....", '۷': "--...", '۸':  "---..", '۹':  "----.", '۰': "-----", 'آ' : '.-', 'ا' : '.-', 'ب' : '-...', 'پ' : '.--.', 'ت' : '-', 'ث' : '-.-.', 'ج' : '.---', 'چ' : '---.', 'ح' : '....', 'خ' : '-..-', 'د' : '-..', 'ذ' : '...-', 'ر' : '.-.', 'ز' : '--..', 'ژ' : '--.', 'س' : '...', 'ش' : '----', 'ص' : '.-.-', 'ض' : '..-..', 'ط' : '..-', 'ظ' : '-.--', 'ع' : '---', 'غ' : '..--', 'ف' : '..--', 'ق' : '..-.', 'ک' : '-.-', 'گ' : '--.-', 'ل' : '.-..', 'م' : '--', 'ن' : '.-', 'و' : '.--', 'ه' : '.', 'ی' : '..', '\n':'\n'}
# - - - - - - - - - - - -FuncTioN- - - - - - - - - - - #
async def myexec(code, event, Client): # a memento from my friend, Andy =D
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
def get_cmds(event, prefix, lower: bool = True):
    cmd = event.raw_text.lower().split() if lower else event.raw_text.split()
    cmd[0] = cmd[0][1:] if cmd[0][0] in prefix else cmd[0]
    len_cmd = len(cmd)
    return [cmd, len_cmd]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class Counter:
    def __init__(self):
        self.number = 0
    def get_num(self):
        self.number += 1
        return self.number
    def clear(self):
        self.number = 0
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class Base:
    def __init__(self, s, b):
        self.ns = Base.base(self, s, b)
    def charbase(self, n, base):
        s = '0123456789ABCDEF'
        if n < base:
            return s[n]
        else:
            return self.charbase(n//base , base) + s[ n % base]
    def base(self, s, base):
        ns = ''
        for ch in s:
            ns += self.charbase(ord(ch),base)+' '
        return ns
    def result(self):
        return self.ns
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def send_sudo_msg(event, message, Account):
    return await event.edit(message) if event.sender_id in Account else await event.reply(message)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def dict_speedtest() -> dict:
    st = Speedtest()
    st.get_servers()
    st.get_best_server()
    st.download()
    st.upload()
    return st.results.dict()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def check_user_id(text: str):
    try:
        if text[0] == '-':
            return {'group':int(text),'get':int(text)}
        elif text[0] == '@':
            return {'addid':text,'get':text}
        elif text.isdigit():
            return {'user':int(text),'get':int(text)}
    except:pass
    return None
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
BOT_GROUP_DATABASE = {
    'link':False,'unknown':False, 'photo':False,'sticker':False,'gif':False,
    'service':False,'game':False,'button':False,'voice':False,'forward':False,
    'video':False,'via':False,'music':False,'file':False,'bot':False,
    'location':False,'contact':False,'caption':False,'contact':False,'caption':False,
}
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def empty_async(event):
    return True
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def voice_to_str(AudioSegment, file, language = 'fa-IR'):
    voice = AudioSegment.from_ogg(file)
    filename = file[:file.rfind('.')] + '.wav'
    AudioSegment.export(voice, filename, 'wav')
    with sr.AudioFile(filename) as source:
        r = sr.Recognizer()
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language=language)
    os.remove(file)
    os.remove(filename)
    return text
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def setup_data(database: dict, key, clir, js, event, panel):
    if database.get(key, None) != None:
        database[key] = not database[key]
        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
        return await panel(event)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def run_interpreter_code(run, file, lang_cmd, code, TimeoutExpired, event, Account):
    if lang_cmd and file:
        edit_source_run(code, file)
        try:code = run([lang_cmd, file], capture_output=True, text=True, timeout=5)
        except TimeoutExpired: await send_sudo_msg(event, '**› timeout error !**', Account)
        else:await send_sudo_msg(event, '› **error:**\n\n`'+code.stderr+'`' if code.stderr else '› **result:**\n\n`'+code.stdout+'`', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def check_data_dir():
    if not os.path.isdir('data'): os.mkdir('data')
    for dirs in ['code', 'photos', 'SeSioNS', 'voice', 'temp']:
        if not os.path.isdir('data/' + dirs): os.mkdir('data/' + dirs)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #

