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
KOS_FoSH = ['هار میشم میام مادرتو میگاما خارکونی', 'مادرجنده دکل ایرانسلو چپ میکنم تو چوچول صورتی مادرت ببینی دنیا دست کیه', 'ای بیناموس ولدگوه باز که کیرمو کردی تو کص مامانت', 'بی شرف چموش داری حالمو بهم میزنی با این بی غیرتیت', 'مادرمُرده چرا اینقدر کثیفی که از مادر بیچارت دفاع نمیکنی حقیر زاده', 'هار میشم میام مادرتو میگاما خارکونی', 'کس ناموس اینقد رقت انگیزی ک عوقم میگیره باهات چت بدم شاش ناموس کیرمم نمیکنم تو کص مادرت', 'کیرمو چنان فرو میکنم تو واژن مادرت که نفت ازش بزنه بیرون عنونه ناموس', 'موتور سیکلت تو کص خار و ناموصت شه اخه چراجلو من چت میدی', 'کصخولی تو خب داش کص مادرت بشه بالا تا ناموصتو به شدت عجیبی کتک بزنم تو به کص مادرت خندیدی', 'مگ نمیگم بالا باش؟ چرا اینقدر از فرمان اربابت سرپیچی میکنی کص مامانتو میخام با پارو پاره کنم د تند تند به کص مامانت پارو', 'بزنم میفهمی؟ میخام کص مامانتو محلی برای قایق رانی و مسابقات قایق سواری کنم کیری مادر میخام ضربه', 'ای به مادرت با کیرم وارد کنم که اون سرش ناپیدا باشه و اون موقع به درد ضربه ی کیر من پی میبری بیناموص ممبرک تو اصلا چرا شاخی', 'بیناموص غیرتتو ازت گرفتم کص نصلت مادر چموش چرا ریدی تو کص مامانت اخه خار بیناموص بدبخت در میری الان ؟ چرا داری مث کصخولا نگاه میکنی منو', 'کص نوامیست کص اجدادت کیر من فق ابشو به کص مامانت میده هنوزم لابد میخای تک بدی بدبخت', 'ابلح زاده تو سگ کی باشی که جلو ما قد علم کنی بهت میگم از جات جم بخوری نسلتو میگام تو هم مث موش میشینی یه گوشه تماشا میکنی منم از گردن پدرت', 'میگیرم کشان کشان میکونمش رو اسفالت داغ میخابونمش وسط جاده درست رو اسفالت سوزان ک کمر پدرتو بسوزونه', 'لوله تفنگمو میگیرم طرف پدر بی ناموصت از نافش شرو میکنم ب شیلک کردن با خط مسقیم میام ب طرف بالا خون بپاشه ب', 'اصراف بد یهو تفنگو میگیرم سرش مخ پر از گوهشو منهدم میکنم جورری ۶۰ تا تیرو رو پدرت خالی میکنم ک بدنش از وسط دو نیم', 'شه یه تیکه از بدنشو بر میدارم میندازم قسمت رفت اومد ماشینا له لوردش کنن نمیه دیگشو میکشم رو اسفالت میبرم وسط', 'بیابون بنزین میریزم روش اتیشش میزنم جنازه کثیف الوده به گوهشو میسوزونم خاکستر بجا موندشو روونه باد میکنم بی', 'میام مجبورت میکنم بری تو این همه شلوغی ازدهامماشینا از روی اسفالت جم کنی یهو ماشین از راه میرسه با مادرت بیناموس', 'میدم به کص مامانت خنیدی بیناموص تو افیم تکست میدی مادرتو گاییدم کون ابجیتو جلو رو خودت کباب', 'کس مامانت شه بیناموس دفه اخرت یاشه قد علم میکنی مادرتو سگ بگاد', 'کس نسلت بشه داشم بالا باش میخوام قبر ناموستو از جاش در بیارم', 'سمور زاده بی غیرت مادر تخفیفچی مادرتو گایدم ناموستو با عن خر یکی کنم', 'غیرتت کو داشم شاشیدم تو شرفه مامانت بیناموس گوه تو نسلو نوامیست', 'کس کش مامانت گاییدم الان دیگه حامله شده یه خواهر برات میاره اونم میکنم یه بچه بیاره کس اجداد خرت تخمی', 'رییدم رو قبر پدربزرگت تخم سگ کیرم تو زنده هات', 'از عروسک به دست تا عسا به دستت گائیدم تخم گراز', 'متاسم که مامانت ترو با شیر سگ بزرگ کرده کیر سگ ها تو ممه های مامانت خایه مال جنده', 'کس کش تو نمردی انقد واسه خامنه ای مالیدی خایه مال کس لیس کیرم تو دماغ کج مامانت', 'تخم مرغ خرس پدرسگ دزد مامانت جندگی کرده تو به دنیا اومدی کیر خور پدرتم کیرش واسه مامانت بلند نشده رفته جاکش و بکن اورده مامانت کردن', 'بابات با نون دزدی مامانتو سیر کرده توام دزد به دنیا اومدی مطمئنم مادرتو دزدگی کرده تو به دنیا اومدی کس اجداد خرت', 'یه شب مامانتو دزدیدم بردم گاییدمش بعد چن وقت زنگ زد گفت من ازت حامله ام گفتم باید بچمو ببینم گفت نه نمیزارم اما هروقت بزرگ شد میفرستمش تل بهت فهش بده و واست شاخ شه', 'میدونی اگه مامانتو ول کنم چیه میشه؟ هیچی نمیشه میرم سراغ خوار جندت پدرسگ بی خایه', 'بی خایه فرار نکن تازه کیرم روغنی کردم باید بدون حامله کردن مامانت نمیرم', 'کس نگو کسکش قهبه زنتو گاییدم کیرم تو ناموس هرکی که به تو زن داده و بده بچه هاتم مثل خودت فلج مغزی و کس دست میشن', 'کس خالت بی غیرت شاشدم تو کس مامانت زود بالا باش باید کرده بشی', 'کیرم تو شاشدون مامانت پدرسگ مادر شاشو اوبی بیا کیرم دهن کل خاندانت', 'استخون مرده هات تو کون زنده هات تخم جن بی خایه فراری کصلیس', 'مامانت کیر میدزده بگو نکنه ما به کیرمون جهت گاییدن خاندانت نیاز داریم', 'کیر هرچی نانوایی تو کس مامانت و خواهرت', 'کیر هرچی برنامه نویس و کافینت ها تو کس ابجیت پدرخرس', 'مامانت معروفه بره هر جنده خونه ای بدون پول کونش میزارن همه مرامی و مشتی ان باهاش بی رودروایسی ابشونو میپاشن توش', 'الوار نجار ها وسط کس مامانت تخم جن بی خانواده مادر حمومی', 'مادر ویندوزی کس عمتو میشورم برق میندازم میدم سگ بکنتش', 'مادر اینتر زن مادر اسپیسی کیر خامنه ای تو دستای مامانت', 'کیر جکی جان تو دستای ترک خورده بابات توله سگ بی مادر', 'کیرم تو دهن مادر دو جنسه ات که با پدرت همش در حال گی کردن هست', 'مادر گیتار زن سنتو تو کس ابجیت و خالت کیر محسن چاوشی که مثل صداش کلفته تو کس مامانت تخم خر', 'مامانت میگوزه کره زمینو تعطیل میکنه پدرتم بهش افتخار میکنه اما من دوتاشونو گاییدم', 'جانی توی خاطراتش خیلی از مامانت نام برده کس مادر سگت تخم جن جانی سلام میرسونه', 'تمام محصولات دیجی کالا تو کس تک تک اعضای خانوادت بی ناموس اوکی', 'کیر همه ربات های تلگرام تو کس مامانت همشون مامانتو با کیر اهنیشون کردن', 'روزی صد تا کسکش و پدرسگ مثل ترو سر کیرم میچرخونم الان تو فک کردی میتونی کیرم بخوری', 'کسسسس مرده هات کص عزیزت کس ناموست کسس خواهرت و زنت', 'کیر شهید چمران تو چشمای مامانت خخخ کس مامانتو گایید یادته', 'خیلی به طور رزمی کس مامانت گذاشتم همون طور که میکردمش و استخوناش مشکست مو هاشم میکشیدم', 'جوری مامانت کردم که نزدیک بود کمرش بشکنه اما این اتفاق نیوفتاد فقط استوخونای دور بر کصش شکست', 'مامانت جنده محله خخ همچین کردمش پزشک قانونی تشخیص نداد انسان کرده یا خر', 'کاغذ لوله کردم کردم تو کس مامانت خخخ اونم فقط می نالید بعد سیخ داغ کردم رو کسش رو امضا کردم تا خیانت نکنه اما اون جنده شد', 'مامانت همرو نگران کرده چرا چن وقتی پیداش نیس کیرمون سیخ شده بگو بیاد بکنیمش', 'کس مادر فراری دیلدو تو کس مامانت بالا باش', 'فرزندم کس نگو خودت همیشه میدونستی از تخم منی', 'بی پدر مادر زود تایپ بده بی مادر فرار نکن ابجیت گاییدم', 'من خواهر ندارم اما در عوض کیر شیش تا داداشم تو کس مادر حرم زاده ات', 'هفت کتوله همون طور که مامانت گاییدن خواهرتم میگان ب صاحاب خرررر', 'بچگیا با مامانت دکتر بازی میکردم همون موقع بود فهمیدم در اینده توی خارکصه به دنیا میای', 'مامانت در گوشم گفت من به سگ ها کون میدم بعد قرص میخورم تا توله به دنیا نیارم اما یبار یادم رفت یه بچه به دنیا اوردم در اینده میاد برات شاخ میشه منم بوسیدمشو بردم با چاقو کسش رو گشاد کردم تا دیگه سگ ها هم نکننش', 'مامانت یه زن بازاری بیچارست که هرچی بچه کونیه افتادن دنبالش که مکان جور کنن و خوب مثل سگ بگانش', 'چوب دارچین تو کس مامانت خانوادت گاییدم هفت جدت گاییدم', 'کس نگو بی مادر شاخ مجازی نگاییدم حجی بی شرف', 'بی شرف بی خایه غیرتت کو دارم مامانت میکنم جوابی نداری شرفت انداختم تو پارچ ابلیمو', 'مادر هزار تومنی مامانت تا دیروز در خونتون اعلامیه میزد شبی 120 الان تو برا من شاخ شدی کص میگی اخه میمیری کص نگی؟', 'کص نگو بی ناموس خودتو رفیقاتو مامانتو دینتو همرو یجا مثل گراز گائیدم بی خایه', 'خایه مال خایه هامو بمال تخم گربه کولر و شوفاژ تو کس مادر سگ و بیچارت', 'از ممد مدد کند کیر در کس مامانت کند', 'کیر کل گپ تو دهن اول تا خرت کیر پاول دروف هم تو پدربزرگت', 'کیر دولت و تمام شبکه های صدا و سیما وسط قیافه کیری مامانت همش رژ لب میزنه', 'الان دستمو تا جایی که امکان داره میکنم ط مای التهتان مادرت به اندام بیکینی مادرت دسترسی پیدا میکنم و یه کاری از اون داخل انجام میدم تا منجلب بدبختی و خاک بر سری پدرت بشه', 'اهنگ افسانم انگا جومونگم خلسه رو میزارم فاز جومونگ میگیرم سوار مادرت میشم پیتکو پیتکو میکنم با شمشیر معبد شائولین گردن خارتو میزنم', ' اهنگ جانم باش ارون افشارو میزارم با مادرت ی سکس رمانتیک بکنیم تا مادرت وابستم ش باباتو ول کنه', 'آب گرم حموم باز میکنم وان حموم پر آب داغ شه یه گالون وایتکس پر میکنم تو وان هموم کله مادرتو میچپونم تو وان حموم. میگوزم تو وان با گوز من و مایع قاطی شه در حموم میبندم مادرت داخل حموم از ترکیب وایتکس با آب گرم خفه شه', 'رعیت زاده دارم با ماشین میرم دنبال مادره فاحشت با یه اشاره مخشو میزنم مییرمش ط ارامگاه پدر کم غیرتت یه دل سیر بهش تجاوز میکنم و وقتی که ننگ جدیدی برای نوامیصت به وجود اومد پدرت در فشار روحی اعظیمی قرار بگیره', 'مادرت فک ميکرد مازراتي دارم و بعضي وقتا پورش بعضيو وقتا امريکايي بازم واسه همين شمارشو داد گفتش که اگه دوست داري باهم بيشتر اشنا شيم و من قبول کردم ولي يه روز که مامانت گفت بيا دنبالم با وانت رفتم دنبالش و همونجا يهويي غش کرد و پس افتاد پس نتيجه ميگيريم که مادرت اهن پرستي بيش نيست و فقط پول ميخاد تا بره باش ساپورت تنگ بخره', 'این چه وضع تایپ کردنه بی ناموص فلک زده مگه داری با تبلت دانش اموزی ۲۰۰ تومنی کار میکنی که این همه لرز میدی؟']
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