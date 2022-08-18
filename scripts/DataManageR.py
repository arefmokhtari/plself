#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from .Color import Color
from redis import StrictRedis
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def bot_redis(redis_number: int) -> StrictRedis:
    try:
        BOTREDIS = StrictRedis(host = '127.0.0.1', port = 6379, db = redis_number, decode_responses = True) 
        BOTREDIS.set('plagueDr','aref')
    except Exception as e:
        print(f'{Color.RED}×  cannot connect to redis !\n╰─>{Color.RESET}', e)
        quit()
    else:
        return BOTREDIS
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
