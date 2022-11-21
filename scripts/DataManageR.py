#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from redis import StrictRedis
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def bot_redis(redis_number: int) -> StrictRedis:
    try:
        BOTREDIS = StrictRedis(host = '127.0.0.1', port = 6379, db = redis_number, decode_responses = True) 
        BOTREDIS.set('plagueDr','aref')
    except Exception as e:
        print('\x1b[91m×  cannot connect to redis !\n╰─>\x1b[0m', e)
        quit()
    else:
        return BOTREDIS
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class DataBase:
    ignore_message = 'DonTCare2MsG'
    mute_private_user = 'plMutePVUsEr'
    mute_group_user = 'plMut3UserInPG'
    group_manager = 'plAddGroPSettinGZ'
    lastname_timer = 'plSetTimENow'
    biotime = 'plBioTimENow'
    bio = 'plFuckinBio'
    users_is_bot_private = 'plUserInApiBoT'
    logo = 'plSetMyFuckingLogo'
    is_forward_messages = 'plForWardSendOrno'
    users_in_private = 'plAcUserInPV'
    user_bot_in_private = 'plAcBoTInPV'
    voices = 'plVoiCESaVE'
    files = 'plFuCKInGFilESaVE'
    antitabchi = 'AnTITABCiE'
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def userisbot(clir, event):
    if str(event.sender_id) in clir.lrange(DataBase.users_in_private,0 ,-1):
        return False
    elif str(event.sender_id) in clir.lrange(DataBase.user_bot_in_private,0 ,-1):
        return True
    else:
        user = await event.get_sender()
        if user.username == None:
            clir.lpush(DataBase.users_in_private, user.id)
            return False
        elif user.username.lower().endswith('bot') or user.username in ['BotFather', 'Stickers', 'gamee', 'like', 'pic', 'bing', 'music']:
            clir.lpush(DataBase.user_bot_in_private, user.id) 
            return True
        else:
            clir.lpush(DataBase.users_in_private, user.id)
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
