#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from redis import StrictRedis
from .DataManageR import bot_redis
from .Color import Color
from .plConfig import botc
import json as js
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def show():
    print(f'''{Color.CYAN}- - - - - - - - - - - - - - - - - - - - -
卐 Enter the manual code : {Color.GREEN}[{Color.RESET} 1 {Color.GREEN}]{Color.CYAN}
卐 ShoW PlSelf-Database : {Color.GREEN}[{Color.RESET} 2 {Color.GREEN}]{Color.CYAN}
卐 DeLeTeD A DaTa : {Color.GREEN}[{Color.RESET} 3 {Color.GREEN}]{Color.CYAN}
卐 get data backup : {Color.GREEN}[{Color.RESET} 4 {Color.GREEN}]{Color.CYAN}
卐 ExiT : {Color.GREEN}[{Color.RESET} 0 {Color.GREEN}]{Color.CYAN}
''')
    cmd = input(f'{Color.GREEN}┌──({Color.CYAN}EnteR㉿plagueDr{Color.GREEN})-[{Color.RESET}~/plself{Color.GREEN}]\n└─${Color.RESET} ')
    if cmd == '1':
        print('- REDIS obj Name = clir| TO EXIT, enter done && 2 reset \n')
        text = ''
        while True:
            t = input('| ')
            if t == 'done':
                try:
                    print(text)
                    exec(text)
                except Exception as e:
                    print('ErroR :', e)
                break
            elif t == 'reset':
                text = ''
                print('\nCoD# Reseted !\n')
            else:
                text += t+'\n'
    elif cmd == '2':
        print('---------------')
        print('DonTCare2MsG =', clir.lrange('DonTCare2MsG', 0, -1))
        print('plMutePVUsEr =',clir.lrange('plMutePVUsEr', 0, -1))
        print('plMut3UserInPG =',clir.hgetall('plMut3UserInPG'))
        print('plAddGroPSettinGZ =',clir.hgetall('plAddGroPSettinGZ'))
        print('plSetTimENow =', clir.get('plSetTimENow'))
        print('plBioTimENow =', clir.get('plBioTimENow'))
        print('plFuckinBio =', clir.get('plFuckinBio'))
        print('plSetrandnameNow =', clir.get('plSetrandnameNow'))
        print('plUserInApiBoT =', clir.lrange('plUserInApiBoT', 0, -1))
        print()
        print('plForWardSendOrno =', clir.get('plForWardSendOrno'))
        print('plKoSKhOLAApL =', clir.lrange('plKoSKhOLAApL', 0, -1))
        print('plAcUserInPV =', clir.lrange('plAcUserInPV',0 ,-1))
        print('plAcBoTInPV =', clir.lrange('plAcBoTInPV',0 ,-1)) 
        print('plVoiCESaVE =', clir.hgetall('plVoiCESaVE')) 
        print('plFuCKInGFilESaVE =', clir.hgetall('plFuCKInGFilESaVE')) 
        print('AnTITABCiE =',clir.hgetall('AnTITABCiE'))
        print('---------------')
        for ads in clir.keys('acdontsave:*'):
            print(ads, '=', clir.get(ads))
        print('---------------')
    elif cmd == '3':
        try:
            clir.delete(input('- enter key 2 delete : '))
        except Exception as e:
            print(e)
    elif cmd == '4':
        _4backup = {
            'DonTCare2MsG':clir.lrange('DonTCare2MsG', 0, -1),
            'plMutePVUsEr':clir.lrange('plMutePVUsEr', 0, -1),
            'plMut3UserInPG':clir.hgetall('plMut3UserInPG'),
            'plAddGroPSettinGZ':clir.hgetall('plAddGroPSettinGZ'),
            'plSetTimENow':clir.get('plSetTimENow'),
            'plBioTimENow':clir.get('plBioTimENow'),
            'plFuckinBio':clir.get('plFuckinBio'),
            'plSetrandnameNow':clir.get('plSetrandnameNow'),
            'plUserInApiBoT':clir.lrange('plUserInApiBoT', 0, -1),
            'plForWardSendOrno':clir.get('plForWardSendOrno'),
            'plAcUserInPV':clir.lrange('plAcUserInPV',0 ,-1),
            'plAcBoTInPV':clir.lrange('plAcBoTInPV',0 ,-1),
            'plVoiCESaVE':clir.hgetall('plVoiCESaVE'),
            'plFuCKInGFilESaVE':clir.hgetall('plFuCKInGFilESaVE'),
            'AnTITABCiE':clir.hgetall('AnTITABCiE')
        }
        with open( f'data/backup{botc.REDIS_NUMBER}.json', 'w',  encoding='utf-8') as f:
            js.dump(_4backup, f)
        print(f'\n- done ! \nth backup saved in "data/backup{botc.REDIS_NUMBER}.json"')
    elif cmd == '5':
        print('\n- Under Construction !')
    elif cmd == '0':
        exit(0)
    else:
        print('\n- 404 !\n\a')
    show()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
if __name__ == '__main__':
    print(f'\n\t\t{Color.BLACK} {Color.BACKGROUND_RED}㉿ [   Plague Dr.  ] ㉿{Color.RESET}')
    clir = bot_redis(StrictRedis, botc.REDIS_NUMBER)
    print(Color.RED ,'\n\t• Redis PlSelf-Database Management System !')
    print(f'\t- Connected to RediS Number {Color.YELLOW} {botc.REDIS_NUMBER} {Color.RED}!')
    print('\t• Please select one of the following:\n', Color.RESET)
    show()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
