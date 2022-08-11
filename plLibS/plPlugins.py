#                   [   Plague Dr.  ]
import os, random, re
from math import ceil
from . import coinmarketcap
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
Coin = coinmarketcap
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def crtiktok(numbers: list) -> list:
    c = 0
    num = []
    for i in numbers:
        if c > 7: break
        for j in numbers:
            num.append(i+j)
        c += 1
    return num
num = crtiktok('⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹'.split())
version = 0.6
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
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
CoDMORsE = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..", 'e' : ".", 'f' : "..-.", 'g' : "--.", 'h' : "....", 'i' : "..", 'j' : ".--", 'k' : "-.-", 'l' : ".-..", 'm' : "--", 'n' : "-.", 'o' : "---", 'p' : ".--.", 'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-", 'u' : "..-", 'v' : "...-", 'w' : ".--", 'x' : "-..-", 'y' : "-.--", 'z' : "--..", ' ' : ' ', '1':  ".---", '2':  "..---", '3': "...--", '4':  "....-",'5': ".....", '6':  "-....", '7': "--...", '8':  "---..", '9':  "----.", '0': "-----", '۱':  ".---", '۲':  "..---", '۳': "...--", '۴':  "....-", '۵': ".....", '۶':  "-....", '۷': "--...", '۸':  "---..", '۹':  "----.", '۰': "-----", 'آ' : '.-', 'ا' : '.-', 'ب' : '-...', 'پ' : '.--.', 'ت' : '-', 'ث' : '-.-.', 'ج' : '.---', 'چ' : '---.', 'ح' : '....', 'خ' : '-..-', 'د' : '-..', 'ذ' : '...-', 'ر' : '.-.', 'ز' : '--..', 'ژ' : '--.', 'س' : '...', 'ش' : '----', 'ص' : '.-.-', 'ض' : '..-..', 'ط' : '..-', 'ظ' : '-.--', 'ع' : '---', 'غ' : '..--', 'ف' : '..--', 'ق' : '..-.', 'ک' : '-.-', 'گ' : '--.-', 'ل' : '.-..', 'م' : '--', 'ن' : '.-', 'و' : '.--', 'ه' : '.', 'ی' : '..', '\n':'\n'}
KOS_FoSH = [] # add msgs to floot spam !
# - - - - - - - - - - - -FuncTioN- - - - - - - - - - - #
def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if (gm > 2):
        gy2 = gy + 1
    else:
        gy2 = gy
    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if (days > 365):
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if (days < 186):
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return [jy, jm, jd]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class Color:
    RESET = '\x1b[0m'
    RED = '\x1b[91m'
    GRAY = '\x1b[90m'
    MAGENTA = '\x1b[35m'
    CYAN = '\x1b[96m'
    YELLOW = '\x1b[93m'
    BLUE = '\x1b[94m'
    BLACK = '\x1b[30m'
    GREEN = '\x1b[92m'
    LIGHT_GRAY = '\x1b[37m'
    DARK_GRAY = '\x1b[90m'
    LIGHT_RED = '\x1b[91m'
    LIGHT_GREEN = '\x1b[92m'
    LIGHT_YELLOW = '\x1b[93m'
    LIGHT_BLUE = '\x1b[94m'
    LIGHT_MAGENTA = '\x1b[95m'
    LIGHT_CYAN = '\x1b[96m'
    #
    BACKGROUND_RED = '\x1b[41m'
    BACKGROUND_GRAY = '\x1b[100m'
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def _exec(code, event, Client): # a memento from my friend, Andy =D
    exec(f"async def __exec(event, Client): " + "".join(f"\n {x}" for x in code.split("\n")))
    return await locals()["__exec"](event, Client)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def bot_redis(StrictRedis, redis_number):
    try:
        BOTREDIS = StrictRedis(host = '127.0.0.1', port = 6379, db = redis_number, decode_responses = True) 
        BOTREDIS.set('plagueDr','aref')
    except Exception as e:
        print(f'{Color.RED}×  cannot connect to redis !\n╰─>{Color.RESET}', e)
        quit()
    else:
        return BOTREDIS
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def fileindir(pattern: str, dirlist: os.listdir) -> list: 
    return [FilE for FilE in dirlist if FilE.startswith(pattern)]
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
async def userisbot(clir, event):
    if str(event.sender_id) in clir.lrange('plAcUserInPV',0 ,-1):
        return False
    elif str(event.sender_id) in clir.lrange('plAcBoTInPV',0 ,-1):
        return True
    else:
        user = await event.get_sender()
        if user.username == None:
            clir.lpush('plAcUserInPV', user.id)
            return False
        elif user.username.lower().endswith('bot') or user.username in ['BotFather', 'Stickers', 'gamee', 'like', 'pic', 'bing', 'music']:
            clir.lpush('plAcBoTInPV', user.id) 
            return True
        else:
            clir.lpush('plAcUserInPV', user.id)
            return False
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def switch(search: object, sdict: list, default: object):
    return sdict.get(search, default)
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
def isexistList(inli: list, index: int) -> bool:
    try:
        inli[index]
        return True
    except:
        return False
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def adduserinMuteGp2hset(clir, key: str, field: str, val: str):
    if field not in list(clir.hgetall(key).keys()):
        clir.hset(key, field, val)
    else:
        liRE = clir.hget(key, field).split()
        liRE.append(val)
        clir.hset(key, field, ' '.join(liRE))
def deluserinMuteGp2hset(clir, key: str, field: str, val: str):
    if field not in list(clir.hgetall(key).keys()):
        return 
    elif clir.hget(key, field) == '':
        clir.hdel(key, field)
    else:
        liRE = clir.hget(key, field).split()
        liRE.remove(val)
        if len(liRE) == 0:
            clir.hdel(key, field)
            return
        else:
            clir.hset(key, field, ' '.join(liRE))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def crtime(hour: int, minute: int) -> str: 
    return '﹕'.join([num[hour], num[minute]])
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def crbiotime(hour: int) -> str:
    return ' - { '+['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'][hour]+' }'
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def findfile(filename, dir):    
    for root, dirs, files in os.walk(dir):
        for file in files: 
            if file.startswith(filename):
                return (str(file))
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
class Counter:
    def __init__(self):
        self.number = 0
    def get_num(self):
        self.number += 1
        return self.number
    def clear(self):
        self.number = 0
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def split_coins(coins: Coin.getCoin | dict, num: int = 60) -> list:
    pms = []
    cntr = Counter()
    c = 0
    iterator = coins.get_dict().items() if type(coins) is Coin.getCoin else coins.items()
    for i, v in iterator:
        index = cntr.get_num()
        if index%num==0:c+=1
        if (c+1) >= len(pms): pms.append('')
        pms[c] += f'{index} - {i}: `{v:,}$`\n'
    while pms.count(''): pms.remove('')
    return pms
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def user_in_channel(bot, chat, user, UserNotParticipantError):
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
def jdmonthname(month: int) -> str:
    return ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman','Esfand'][month-1]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def send_seasons(month: int, ptn: str = 'm') -> str:
    return ['Spring', 'Summer', 'Fall', 'winter'][(ceil(month/3))-1] if ptn == 'm' else ['Bahar', 'Tabestan', 'Paiiz', 'Zemeston'][(ceil(month/3))-1]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def send_weekday(day: int):
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def edit_source_run(code: str, file: str):
    with open(file, 'w') as f:
        f.write(code)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #