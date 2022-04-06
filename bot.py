#                   [   Plague Dr.  ]
# - - - - - - - - - - -LIBRarYS- - - - - - - - - - - - #
from telethon import TelegramClient, events, Button, types, __version__ as tver
from telethon.tl.functions.messages import ImportChatInviteRequest, CheckChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest, EditBannedRequest, InviteToChannelRequest, EditPhotoRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import InputPeerChannel, InputPeerUser, ChatBannedRights
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.phone import JoinGroupCallRequest, CreateGroupCallRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.utils import pack_bot_file_id
from googletrans import Translator
import instaloader
from speedtest import Speedtest
import qrcode 
from phonenumbers import geocoder, carrier, parse as FuckingPhone
from whois import whois
from pwd import getpwuid
from plLibS import plPlugins as pl, plConfig as botc
import os, sys, subprocess
import json as js
import random as rand 
from datetime import datetime as dt
from captcha.image import ImageCaptcha 
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
import requests as req
from redis import StrictRedis
# - - - - - - - - - - - ValueS - - - - - - - - - - - - #
Account = botc.acc_sudo 
sudo = botc.sudoS
#phone = '+989360145942'
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
print(f'{pl.Color.BLACK}\n{pl.Color.BACKGROUND_RED}# ------------- [   Plague Dr.  ] ------------- #{pl.Color.RESET}\n'+pl.Color.DARK_GRAY) 
bot = TelegramClient('data/SeSioNS/'+botc.SESSION_API_NAME, botc.API_ID, botc.API_HASH).start(bot_token=botc.BOT_TOKEN)
clir = pl.bot_redis(StrictRedis, botc.REDIS_NUMBER)
insta = instaloader.Instaloader()
pl.check_insta(insta, session = botc.INSTAGRAM[0], username = botc.INSTAGRAM[1], passwd = botc.INSTAGRAM[2])
Client = TelegramClient('data/SeSioNS/'+botc.SESSION_AC_NAME, botc.API_ID, botc.API_HASH)
Client.start()
print('\t- Client && bot is runing ! go FucKyourSelf && Bye.', pl.Color.RESET)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» CheckING MsG SerVic3 In GP:
@Client.on(events.Raw(types.UpdateNewChannelMessage, func=lambda e:type(e.message) is types.MessageService))
async def GetMsGServic3InGP(event: events.Raw):
    if '-100'+str(event.message.peer_id.channel_id) in clir.hgetall('AnTITABCiE').keys():
        if type(event.message.action) == types.MessageActionChatJoinedByLink:
            await Client.edit_permissions(event.message.peer_id.channel_id, event.message.from_id.user_id, 
                view_messages = True,
                send_messages = False,
            )
            image = ImageCaptcha(width = 180, height = 90)
            data = pl.create_rend_name(4) 
            image.generate(data) 
            image.write(data, data+'.jpg')
            result = await Client.inline_query(botc.BOT_USERNAME, 'CkTabchi '+data+' '+str(event.message.from_id.user_id), entity=event.message.peer_id.channel_id)
            await result[0].click() 
        elif type(event.message.action) == types.MessageActionChatAddUser:
            
            for users in event.message.action.users:
                await Client.edit_permissions(event.message.peer_id.channel_id, users, 
                view_messages = True,
                send_messages = False,
                )
                image = ImageCaptcha(width = 180, height = 90)
                data = pl.create_rend_name(4) 
                image.generate(data) 
                image.write(data, data+'.jpg')
                result = await Client.inline_query(botc.BOT_USERNAME, 'CkTabchi '+data+' '+str(users), entity=event.message.peer_id.channel_id)
                await result[0].click() 
    if ('-100'+str(event.message.peer_id.channel_id) in list(clir.hgetall('plAddGroPSettinGZ').keys()) and js.loads(clir.hget('plAddGroPSettinGZ', '-100'+str(event.message.peer_id.channel_id)))['lock_tg']) and'action' in event.message.to_dict() and type(event.message.action) is types.MessageActionChatAddUser:
        pass
        
    if '-100'+str(event.message.peer_id.channel_id) in clir.lrange('plMuteAllGP', 0, -1) or ('-100'+str(event.message.peer_id.channel_id) in list(clir.hgetall('plAddGroPSettinGZ').keys()) and js.loads(clir.hget('plAddGroPSettinGZ', '-100'+str(event.message.peer_id.channel_id)))['lock_tg']):
        await Client.delete_messages(event.message.peer_id.channel_id, event.message.id)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» CheckING ALL Message:
@Client.on(events.NewMessage)
async def check_massag3(event: events.NewMessage.Event):
    if event.is_private and event.sender_id != Account[0] and bool(event.media) and 'ttl_seconds' in event.media.to_dict() and bool(event.media.ttl_seconds):
        cr_file = pl.create_rend_name(10)
        await Client.download_media(event.media, os.getcwd()+'/data/photos/'+cr_file)
        await Client.send_file(botc.CHANNEL_FOR_FWD, os.getcwd()+'/data/photos/'+pl.findfile(cr_file, os.getcwd()+'/data/photos'))
    
    if event.sender_id in sudo: 
        pass
    elif event.is_group:
        if str(event.chat_id) in clir.lrange('plMuteAllGP', 0, -1) or (str(event.chat_id) in list(clir.hgetall('plMut3UserInPG').keys()) and str(event.sender_id) in clir.hget('plMut3UserInPG', str(event.chat_id)).split()):
            await event.delete()
        elif str(event.chat_id) in list(clir.hgetall('plAddGroPSettinGZ').keys()):
            database = js.loads(clir.hget('plAddGroPSettinGZ', str(event.chat_id)))
            if database['lock_link'] and pl.check_msg_link(event.raw_text):
                await event.delete()
            elif  database['lock_forward'] and event.fwd_from:
                await event.delete()
            elif database['gp_Ch'] and event.sender_id and event.sender_id < 0:
                await event.delete()
            elif  database['lock_bot']:pass
    elif event.is_private:
        get_user = None if clir.get('acdontsave:'+str(event.sender_id)+':pl') == None else int(clir.get('acdontsave:'+str(event.sender_id)+':pl'))
        if str(event.sender_id) in clir.lrange('plMutePVUsEr', 0, -1):
            if not await pl.userisbot(clir, event):
                if get_user == None:
                    if clir.get('plForWardSendOrno'):
                        clir.setex('acdontsave:'+str(event.sender_id)+':pl', 86400, 1)
                        await Client.forward_messages(botc.CHANNEL_FOR_FWD, event.message)
                else:
                    if get_user < 15:
                        if clir.get('plForWardSendOrno'):
                            clir.setex('acdontsave:'+str(event.sender_id)+':pl', 86400, get_user+1)
                            await Client.forward_messages(botc.CHANNEL_FOR_FWD, event.message)
            await event.delete()
        elif str(event.sender_id) not in clir.lrange('DonTCare2MsG', 0, -1) and not await pl.userisbot(clir, event):
            if get_user == None:
                if clir.get('plForWardSendOrno'):
                    clir.setex('acdontsave:'+str(event.sender_id)+':pl', 86400, 1)
                    await Client.forward_messages(botc.CHANNEL_FOR_FWD, event.message)
            else:
                if get_user < 15:
                    if clir.get('plForWardSendOrno'):
                        clir.setex('acdontsave:'+str(event.sender_id)+':pl', 86400, get_user+1)
                        await Client.forward_messages(botc.CHANNEL_FOR_FWD, event.message)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RMSG MSG:
@Client.on(events.NewMessage(pattern = '(R|r)msg', from_users = sudo))
async def RMSG_CMD(event: events.NewMessage.Event):
    try:
        msg = int(event.raw_text[5:]) 
    except:
        await event.edit('-ErroR !') if event.sender_id in Account else await event.reply('-ErroR !')
    else:
        _4sendmsg = await event.edit(f'- Wait !') if event.sender_id in Account else await event.reply(f'- Wait !')
        c = 1 if event.sender_id in Account else 0
        async for message in Client.iter_messages(event.chat_id, msg+1):
            if c < 2:
                c += 1
                continue
            try:
                await message.delete()
            except:
                await _4sendmsg.edit('-ErroR !') if event.sender_id in Account else await _4sendmsg.reply('-ErroR !')
                break
        await _4sendmsg.edit(f'-DonE ! `{msg}` msg has been DeleTeD !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» InsTa:
@Client.on(events.NewMessage(pattern = '(I|i)nsta', from_users = sudo))
async def InsTA(event: events.NewMessage.Event):
    if len(event.raw_text.split()) == 3 and event.raw_text.split()[0].lower() == 'insta':
        if event.raw_text.split()[1] == 'post': 
            post = instaloader.Post.from_shortcode(insta.context, event.raw_text.split()[2])
            insta.download_post(post, target = 'insta')
            file_name = [i for i in pl.fileindir(insta.format_filename(post), os.listdir(os.getcwd()+'/insta')) if pl.checklist4insta(i)]
            Files = [os.getcwd()+'/insta/'+fi for fi in file_name]
            if len(file_name) >= 1:
                try:
                    await Client.send_file(event.chat_id, [os.getcwd()+'/insta/'+fi for fi in file_name], reply_to=event.id, caption = f'- username = {post.owner_username}\n- like = {post.likes}\n- Comments = {post.comments}')
                except:
                    for f in Files:
                        await Client.send_file(event.chat_id, f, reply_to=event.id, caption = f'- username = {post.owner_username}\n- like = {post.likes}\n- Comments = {post.comments}')
            for FilES in os.listdir('insta'):
                os.remove('insta'+'/'+FilES)
            os.rmdir('insta')
        elif event.raw_text.split()[1] == 'profile':
            profile = instaloader.Profile.from_username(insta.context, event.raw_text.split()[2])
            insta.download_profile(profile, profile_pic_only=True)
            fucking_file = [kos for kos in os.listdir(os.getcwd()+'/'+profile.username) if kos.endswith('jpg')][0]
            
            await Client.send_file(event.chat_id,os.getcwd()+'/'+profile.username+'/'+fucking_file, reply_to=event.id, caption = f'- name = {profile.full_name}\n- bio = {profile.biography}\n- followers = {profile.followers:,}')
            for FilES in os.listdir(profile.username):
                os.remove(profile.username+'/'+FilES)
            os.rmdir(profile.username)
        elif event.raw_text.split()[1] == 'story':
            profile = instaloader.Profile.from_username(insta.context, event.raw_text.split()[2])
            insta.download_profile(profile, download_stories_only = True, profile_pic = False)
            files = [kos for kos in os.listdir(os.getcwd()+'/'+profile.username) if pl.checklist4insta(kos)]
            Files = [profile.username+'/'+sher for sher in files]
            try:
                await Client.send_file(event.chat_id, Files, reply_to=event.id)
            except:
                    for f in Files:
                        await Client.send_file(event.chat_id, f, reply_to=event.id)
            for FilES in os.listdir(profile.username):
                os.remove(profile.username+'/'+FilES)
            os.rmdir(profile.username)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Calculator:
@Client.on(events.NewMessage(pattern = '(C|c)al', from_users = sudo))
async def GeTCal(event: events.NewMessage.Event):
    try: await event.edit(f'{eval(event.raw_text[4:]):,}') if event.sender_id in Account else await event.reply(f'{eval(event.raw_text[4:]):,}')
    except: await event.edit('- ErroR !') if event.sender_id in Account else await event.reply('- ErroR !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Flood SpaM:
@Client.on(events.NewMessage(pattern='(F|f)lood', from_users = Account))
async def FloodSpaM(event: events.NewMessage.Event): 
    if event.is_reply and len(event.raw_text.split()) >= 2 and event.raw_text.split()[0].lower() == 'flood' and event.raw_text.split()[1].isdigit():
        if len(event.raw_text.split()) == 2:
            msg = await event.get_reply_message()
            await event.delete()
            for _ in range(int(event.raw_text.split()[1])):
                await Client.forward_messages(event.chat_id, msg)
        else:
            msg = await event.get_reply_message()
            await event.delete()
            for _ in range(int(event.raw_text.split()[1])):
                await msg.reply(event.raw_text[event.raw_text.find(' ', 6):])
    elif len(event.raw_text.split()) == 3 and event.raw_text.split()[0].lower() == 'flood' and event.raw_text.split()[1] == 'num' and event.raw_text.split()[2].isdigit():
        await event.delete()
        num = pl.Counter()
        for _ in range(int(event.raw_text.split()[2])):
            await Client.send_message(event.chat_id, str(num.get_num()))
    elif len(event.raw_text.split()) == 3 and event.raw_text.split()[0].lower() == 'flood' and event.raw_text.split()[1] == 'fosh' and event.raw_text.split()[2].isdigit():
        await event.delete()
        kosfosh = pl.KOS_FoSH
        if event.is_reply:
            msg = await event.get_reply_message()
            for _ in range(int(event.raw_text.split()[2])):
                await msg.reply(kosfosh[rand.randint(0, len(kosfosh)-1)])
        else:
            for _ in range(int(event.raw_text.split()[2])):
                await Client.send_message(event.chat_id, kosfosh[rand.randint(0, len(kosfosh)-1)])
    elif len(event.raw_text.split()) >= 3 and event.raw_text.split()[0].lower() == 'flood' and event.raw_text.split()[1].isdigit():
        await event.delete()
        for _ in range(int(event.raw_text.split()[1])):
            await Client.send_message(event.chat_id, event.raw_text[event.raw_text.find(' ', 6):])
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» get UseR ID:
@Client.on(events.NewMessage(pattern = '(I|i)d', from_users = sudo))
async def IdProcessing(event: events.NewMessage.Event):
    if len(event.raw_text.split()) == 2:
        if event.raw_text.split()[1][0] == '@':
            chat = await Client.get_input_entity(event.raw_text.split()[1])
            if 'channel_id' in chat.to_dict():
                await event.edit('`-100{}`'.format(chat.channel_id)) if event.sender_id in Account else await event.reply('`-100{}`'.format(chat.channel_id))
            else:
                await event.edit('`{}`'.format(chat.user_id)) if event.sender_id in Account else await event.reply('`{}`'.format(chat.user_id))      
        if event.raw_text.split()[1] == 'chat':
            if event.is_group:await event.edit(str(event.chat_id)) if event.sender_id in Account else await event.reply(str(event.chat_id))
        elif event.raw_text.split()[1][0] == '-':
            chat = await Client.get_entity(int(event.raw_text.split()[1]))#[4:])
            if chat.username == None:
                await event.edit('- not username !') if event.sender_id in Account else await event.reply('- not username !')
            else:
                await event.edit(f'@{chat.username}') if event.sender_id in Account else await event.reply(f'@{chat.username}') 
        elif event.raw_text.split()[1][0].isdigit():
            await event.edit(f'[{event.raw_text.split()[1]}](tg://user?id={event.raw_text.split()[1]})') if event.sender_id in Account else await event.reply(f'[{event.raw_text.split()[1]}](tg://user?id={event.raw_text.split()[1]})')
        elif bool(event.entities) and 'user_id' in event.entities[0].to_dict():
            await event.edit('`{}`'.format(event.entities[0].user_id)) if event.sender_id in Account else await event.reply('`{}`'.format(event.entities[0].user_id))
    elif event.is_private and event.raw_text.lower() == 'id':
        if event.is_reply:
            msg = await event.get_reply_message()
            await event.edit('`{}`'.format(msg.peer_id.user_id)) if event.sender_id in Account else await event.reply('`{}`'.format(msg.from_id.user_id))       
        else:
            await event.edit('`{}`'.format(event.sender_id)) if event.sender_id in Account else await event.reply('`{}`'.format(event.sender_id))                
    elif (event.is_group or event.is_channel) and event.raw_text.lower() == 'id':
        if event.is_reply:
            msg = await event.get_reply_message()
            if 'from_id' in msg.to_dict() and msg.from_id != None and 'channel_id' in msg.from_id.to_dict():
                await event.edit('`-100{}`'.format(msg.from_id.channel_id)) if event.sender_id in Account else await event.reply('`-100{}`'.format(msg.from_id.channel_id))                    
            elif 'from_id' in msg.to_dict() and msg.from_id == None and 'peer_id' in msg.to_dict() and 'channel_id' in msg.peer_id.to_dict():
                await event.edit('`-100{}`'.format(msg.peer_id.channel_id)) if event.sender_id in Account else await event.reply('`-100{}`'.format(msg.peer_id.channel_id))        
            else:
                await event.edit('`{}`'.format(msg.from_id.user_id)) if event.sender_id in Account else await event.reply('`{}`'.format(msg.from_id.user_id))                    
        else:
            await event.edit('`{}`'.format(event.sender_id)) if event.sender_id in Account else await event.reply('`{}`'.format(event.sender_id))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» invalid UseR:
@Client.on(events.NewMessage(pattern = '(I|i)nvite', from_users = sudo))
async def FuckinGInvalidUseR(event: events.NewMessage.Event):
    if len(event.raw_text.split()) == 2 and event.raw_text.split()[0].lower() == 'invite':
        try:
            user = await Client.get_input_entity(event.raw_text.split()[1])
            chat = await Client.get_input_entity(event.chat_id)
            await Client(InviteToChannelRequest(InputPeerChannel(chat.channel_id, chat.access_hash),[InputPeerUser(user.user_id, user.access_hash)]))
        except Exception as e:
            await event.edit('- Error : '+str(e)) if event.sender_id in Account else await event.reply('- Error : '+str(e))
        else:
            await event.edit(f'- User `{user.user_id}` added 2 gorup !') if event.sender_id in Account else await event.reply(f'- User `{user.user_id}` added 2 gorup !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» FucK Off =| :
@Client.on(events.NewMessage(pattern = '(W|w)ow', from_users = Account))
async def GetFuckinGNuD3(event: events.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if msg.media:
            cr_file = pl.create_rend_name(10)
            await Client.download_media(msg.media, os.getcwd()+'/data/photos/'+cr_file)
            await Client.send_file(botc.CHANNEL_FOR_FWD, os.getcwd()+'/data/photos/'+pl.findfile(cr_file, os.getcwd()+'/data/photos'))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» AnTI TabCHI - CaptchA: 
@Client.on(events.NewMessage(pattern = '(A|a)ntitabchi', from_users = sudo))
async def SeTAntITabCHI(event):  
    if event.is_group and len(event.raw_text.split()) == 2 and event.raw_text.split()[0].lower() == 'antitabchi':
        if event.raw_text.split()[1] == 'on': # 'AnTITABCiE'
            if str(event.chat_id) in clir.hgetall('AnTITABCiE').keys():
                if event.sender_id in Account:
                    await event.edit('فعالع')
                else:
                    await event.reply('فعالع')
            else:
                data = []
                if event.sender_id in Account:
                    await event.edit('فعال شد')
                else:
                    await event.reply('فعال شد')
                clir.hset('AnTITABCiE', str(event.chat_id), js.dumps(data))
        elif event.raw_text.split()[1] == 'off':
            if str(event.chat_id) in clir.hgetall('AnTITABCiE').keys():
                clir.hdel('AnTITABCiE', str(event.chat_id))
                await event.edit('پاک شد') if event.sender_id in Account else await event.reply('پاک شد')
            else:
                await event.edit('نبود') if event.sender_id in Account else await event.reply('نبود')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» BaS#:
@Client.on(events.NewMessage(pattern = '(B|b)ase', from_users = sudo))
async def ReBaSE(event: events.NewMessage.Event):
    if len(event.raw_text.split()) >= 3 and event.raw_text.split()[0].lower() == 'base' and event.raw_text.split()[1].isdigit():
        await event.edit(pl.Base(event.raw_text[event.raw_text.find(' ', 5)+1:], int(event.raw_text.split()[1])).result()) if event.sender_id in Account else await event.reply(pl.Base(event.raw_text[event.raw_text.find(' ', 5)+1:], int(event.raw_text.split()[1])).result())
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» MorS#:
@Client.on(events.NewMessage(pattern = '(M|m)orse', from_users = sudo))
async def ReMorsE(event: events.NewMessage.Event):
    if len(event.raw_text.split()) >= 2 and event.raw_text.split()[0].lower() == 'morse':
        await event.edit(''.join([pl.switch(morse, pl.CoDMORsE, ' ')+' ' for morse in event.raw_text[6:]])) if event.sender_id in Account else await event.reply(''.join([pl.switch(morse, pl.CoDMORsE, ' ')+' ' for morse in event.raw_text[6:]]))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» ReStarT Th3 ProGraM:
@Client.on(events.NewMessage(pattern = '(R|r)eload', from_users = Account, func=lambda e:e.raw_text.lower() == 'reload'))
async def RestartProGraM(event: events.NewMessage.Event):
    await event.edit('- bot reloaded !') if event.sender_id in Account else await event.reply('- bot reloaded !')
    os.execl(sys.executable, sys.executable, *sys.argv)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RuN CoD#:
@Client.on(events.NewMessage(pattern = '(C|c)ode', from_users = sudo))
async def RuNCoD3(event: events.NewMessage.Event):
    if len(event.raw_text.split()) >= 2 and event.raw_text.split()[0].lower() == 'code':
        cmd = event.raw_text.split()[1]
        if cmd == 'py3':
            file = os.getcwd()+'/data/code/'+'source.py'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['python3', file], capture_output=True, text=True)
            await event.edit('result:\n\n'+code.stdout+'\n\nError:\n\n'+code.stderr) if event.sender_id in Account else await event.reply('result:\n\n'+code.stdout+'\n\nError:\n\n'+code.stderr)
        elif cmd == 'py2':
            file = os.getcwd()+'/data/code/'+'source.py'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['python2', file], capture_output=True, text=True)
            await event.edit('result:\n\n'+code.stdout+'\n\nError:\n\n'+code.stderr) if event.sender_id in Account else await event.reply('result:\n\n'+code.stdout+'\n\nError:\n\n'+code.stderr)
        elif cmd == 'help':
            t = 'cmds :\npy3\npy2\ncpp\nc\nlua\njava'
            await event.edit(t) if event.sender_id in Account else await event.reply(t)
        elif cmd == 'cpp':
            file = os.getcwd()+'/data/code/'+'source.cpp'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            s = subprocess.run(['g++', '-std=c++11', file], capture_output=True, text=True)
            if s.stderr != '':
                await event.edit('Error:\n\n'+s.stderr) if event.sender_id in Account else await event.reply('Error:\n\n'+s.stderr)
                return
            else:
                code = subprocess.run(['./a.out'], capture_output=True, text=True)
                await event.edit('result:\n\n'+code.stdout) if event.sender_id in Account else await event.reply('result:\n\n'+code.stdout)
                os.remove('a.out')
        elif cmd == 'p':
            try:await eval(event.raw_text[event.raw_text.find('\n')+1:]);await event.edit('- DonE !') if event.sender_id in Account else await event.reply('- DonE !')
            except Exception as e:await event.edit(str(e)) if event.sender_id in Account else await event.reply(str(e))
        elif cmd == 'c':
            file = os.getcwd()+'/data/code/'+'source.c' 
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            s = subprocess.run(['gcc', file, '-o', 'a.out'], capture_output=True, text=True)
            if s.stderr != '':
                await event.edit('Error:\n\n'+s.stderr) if event.sender_id in Account else await event.reply('Error:\n\n'+s.stderr)
                return
            else:
                code = subprocess.run(['./a.out'], capture_output=True, text=True)
                await event.edit('result:\n\n'+code.stdout) if event.sender_id in Account else await event.reply('result:\n\n'+code.stdout)
                os.remove('a.out')
        elif cmd == 'lua':
            file = os.getcwd()+'/data/code/'+'source.lua'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['lua', file], capture_output=True, text=True)
            await event.edit('result:\n\n'+code.stdout+'\n\nError:\n\n'+code.stderr) if event.sender_id in Account else await event.reply('result:\n\n'+code.stdout+'\n\nError:\n\n'+code.stderr)
        elif cmd == 'java':
            file = os.getcwd()+'/data/code/'+'source.java'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            s = subprocess.run(['javac', file], capture_output=True, text=True)
            if s.stderr != '':
                await event.edit('Error:\n\n'+s.stderr) if event.sender_id in Account else await event.reply('Error:\n\n'+s.stderr)
                return
            else:
                os.system('cp '+os.getcwd()+'/data/code/source.class '+os.getcwd())
                os.remove(os.getcwd()+'/data/code/'+'source.class')
                code = subprocess.run(['java', 'source'], capture_output=True, text=True)
                if code.stderr != '':
                    await event.edit(code.stderr) if event.sender_id in Account else await event.reply(code.stderr)
                else:
                    await event.edit('result:\n\n'+code.stdout) if event.sender_id in Account else await event.reply('result:\n\n'+code.stdout)
                os.remove('source.class')

# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» GeT LyriCZ:
@Client.on(events.NewMessage(pattern='(L|l)yrics', from_users = sudo))
async def GetLyricZ(event: events.NewMessage.Event):
    text = event.raw_text
    if len(text) == 6 and event.is_reply:
        msg = await event.get_reply_message()
        if bool(msg.media) and 'document' in msg.media.to_dict() and 'attributes' in msg.media.document.to_dict() and 'title' in msg.media.document.attributes[0].to_dict():
            music, artist = msg.media.document.attributes[0].title, msg.media.document.attributes[0].performer
    else:
        artist, music = text[text.find(' ')+1:text.rfind('-')], text[text.rfind('-')+1:]
    res = req.get('https://api.lyrics.ovh/v1/'+artist+'/'+music)
    try: 
        lyr = res.json()['lyrics']
    except:
        lyr = '- No lyrics found !'
    await event.edit(lyr) if event.sender_id in Account else await event.reply(lyr)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Voic# ChaT:
@Client.on(events.NewMessage(pattern = '(V|v)chat', from_users = sudo))
async def GrouPCalLMain(event: events.NewMessage.Event):
    if len(event.raw_text.split()) == 2 and event.raw_text.split()[0].lower() == 'vchat':
        if event.raw_text.split()[1] == 'cr':
            await Client(CreateGroupCallRequest(event.chat_id))
            await event.edit('- Voic# ChaT WaS Creat3D !') if event.sender_id in Account else await event.reply('- Voic# ChaT WaS Creat3D !')
        elif event.raw_text.split()[1] == 'join':
            chat = await event.get_chat()
            print(chat.stringify())
            await Client(JoinGroupCallRequest(types.InputGroupCall(chat.id, chat.access_hash), 'plagueDr', params=types.DataJSON(data=js.dumps('{"enable_vp8_encoder":true}'))))
        elif event.raw_text.split()[1] == 'end': # .dumps(
            pass
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» QR CoD#:
@Client.on(events.NewMessage(pattern = '(Q|q)rcode', from_users = sudo))
async def QrCoD3(event: events.NewMessage.Event):
    if len(event.raw_text.split()) >= 2 and event.raw_text.split()[0].lower() == 'qrcode':
        if event.raw_text.split()[1] == 'create' and len(event.raw_text.split()) >= 3:
            (qrcode.make(event.raw_text[14:])).save('QRCode.png')
            if event.sender_id in Account:
                await event.delete()
                await Client.send_file(event.chat_id, 'QRCode.png', caption = event.raw_text[14:])
            else:
                await Client.send_file(event.chat_id, 'QRCode.png', reply_to = event.id, caption = event.raw_text[14:])
            os.remove('QRCode.png')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» GeT ProxY:
@Client.on(events.NewMessage(pattern='(P|p)roxy', from_users = sudo))
async def GetProxY(event: events.NewMessage.Event):
    if event.raw_text.lower() == 'proxy':
        res = req.get('https://www.api.wirexteam.tk/mtproto')#('https://www.wirexteam.ga/mtproto')
        num = pl.Counter()
        try: 
            pxy = '\n'.join(list(map(lambda px:f'• [proxy {num.get_num()}]({px["proxy"]}) - **ping: {px["ping"]} ms**', res.json()['mtproto']))[:50])
        except:
            pxy = '- cannot connect 2 weservice !'
        await event.edit(pxy) if event.sender_id in Account else await event.reply(pxy)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Check ManageR:
@Client.on(events.NewMessage(pattern = '(C|c)heck', from_users = sudo))
async def CheCKDIU(event):
    if len(event.raw_text.split()) >= 3 and event.raw_text.split()[0].lower() == 'check':
        if event.raw_text.split()[1] == 'username':
            try:check = f'• **Checking Username** `{event.raw_text.split()[2]}` **On Social Media:**\n'+'            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n'+'\n'.join(['⌬ '+i+' = '+v['stats']+ f'{"[✔️]" if v["link"] else "[✖️]"}' for i, v in req.get('https://www.wirexteam.ga/checker?username='+event.raw_text.split()[2]).json()['checker'].items()])
            except: check = '- Error !'
            finally: await event.edit(check) if event.sender_id in Account else await event.reply(check)
        elif event.raw_text.split()[1] == 'ip':
            try: check = f'• **Ip Information For** ( `{event.raw_text.split()[2]}` ):'+'\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n'+'\n'.join(['⌬ '+i+' = '+str(v) for i, v in req.get('http://ip-api.com/json/{}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,query'.format(event.raw_text.split()[2])).json().items()])
            except: check = '- Error !'
            finally: await event.edit(check) if event.sender_id in Account else await event.reply(check)
        elif event.raw_text.split()[1] == 'domain': 
            try:domain = whois(event.raw_text.split()[2]);check = f'• **Checking Domain** (`{domain.domain}`)\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n⌬ creation = {domain.creation_date}\n⌬ expiration = {domain.expiration_date}\n⌬ servers = [ {", ".join(domain.name_servers)} ]\n⌬ dns = {domain.dnssec}\n⌬ email = {domain.emails}\n⌬ country = {domain.country}\n⌬ state = {domain.state}'
            except:check = '- Error !'
            finally:await event.edit(check) if event.sender_id in Account else await event.reply(check)
        elif event.raw_text.split()[1] == 'phone':
            try:kosphone = FuckingPhone(event.raw_text[event.raw_text.find(' ', 8)+1:]);check = f'• **checking phone** (`{kosphone.national_number}`)\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n⌬ country = {geocoder.description_for_number(kosphone, "en")}\n⌬ country code = {kosphone.country_code}\n⌬ co = {carrier.name_for_number(kosphone, "en")}'
            except:check = '- Error !'
            finally:await event.edit(check) if event.sender_id in Account else await event.reply(check)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Take the system "TIME/DATE" and send it:
@Client.on(events.NewMessage(pattern='(T|t)ime', from_users = sudo, func=lambda e:e.raw_text.lower() == 'time'))
async def SeYTime(event: events.NewMessage.Event):
    Dat3 = pl.gregorian_to_jalali(dt.today().year, dt.today().month, dt.today().day)
    if event.sender_id in Account:
        await event.edit('• Tim3 NoW :\n'+'- time = %.2d:%.2d:%.2d'%(dt.today().hour, dt.today().minute, dt.today().second)+' | '+pl.send_weekday(dt.now().weekday())+'\n- date = '+'/'.join(map(lambda x:'%.2d'%x, Dat3))+' - '+'/'.join(map(lambda x:'%.2d'%x, [dt.today().year, dt.today().month, dt.today().day]))+'\n- Seasons = '+pl.send_seasons(Dat3[1])+' - '+pl.send_seasons(Dat3[1], 'j')+'\n- Month = '+pl.jdmonthname(Dat3[1])+' - '+dt.now().strftime("%B"))
    else:
        await event.reply('• Tim3 NoW :\n'+'- time = %.2d:%.2d:%.2d'%(dt.today().hour, dt.today().minute, dt.today().second)+' | '+pl.send_weekday(dt.now().weekday())+'\n- date = '+'/'.join(map(lambda x:'%.2d'%x, Dat3))+' - '+'/'.join(map(lambda x:'%.2d'%x, [dt.today().year, dt.today().month, dt.today().day]))+'\n- Seasons = '+pl.send_seasons(Dat3[1])+' - '+pl.send_seasons(Dat3[1], 'j')+'\n- Month = '+pl.jdmonthname(Dat3[1])+' - '+dt.now().strftime("%B"))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» UsE th3 Google Translate module 4 translation !:
@Client.on(events.NewMessage(pattern = '(T|t)r', from_users = sudo))
async def TranslatE(event: events.NewMessage.Event):
    Tr = Translator() # 0110100100100000011011000110111101110110011001010010000001001101
    if event.is_reply and len(event.raw_text) == 5:
        msg = await event.get_reply_message()
        msg_for_tr = msg.raw_text
    else:
        msg_for_tr = event.raw_text[6:] 
    await event.edit(Tr.translate(msg_for_tr, dest=event.raw_text[3:5]).text) if event.sender_id in Account else await event.reply(Tr.translate(msg_for_tr, dest=event.raw_text[3:5]).text)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Accounts whose Messag# donot need to be forwarded =| ! :
@Client.on(events.NewMessage(pattern = '(A|a)cdontsave', from_users = Account))
async def DonTSaveMsgInChannel(event: events.NewMessage.Event):
    if event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if str(msg.peer_id.user_id) not in clir.lrange('DonTCare2MsG', 0, -1):
            clir.lpush('DonTCare2MsG', msg.peer_id.user_id)
    await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» JoiN In GrouP:
@Client.on(events.NewMessage(pattern = '(J|j)oin', from_users = Account))
async def joinchat(event: events.NewMessage.Event):
    if len(event.raw_text.split()) > 1 and event.raw_text.split()[1][0] == '@':
        try:
            await Client(JoinChannelRequest(event.raw_text.split()[1]))
            await event.edit('- DonE ! JoinEd =>') if event.sender_id in Account else await event.reply('- DonE ! JoinEd =>')
        except: await event.edit('- ErroR ! =|') if event.sender_id in Account else await event.reply('- ErroR ! =|')
    elif len(event.raw_text.split()) > 1 and pl.check_link(event.raw_text.split()[1], ptrn = 's'):
        link = pl.check_link(event.raw_text.split()[1], ptrn = 'l')
        try:
            await Client(CheckChatInviteRequest(link[link.rfind('/')+1:]))
        except: await event.edit('- InValid LinK ! =|') if event.sender_id in Account else await event.reply('- InValid LinK ! =|')
        else:
            try:
                await Client(ImportChatInviteRequest(link[link.rfind('/')+1:]))
                await event.edit('- JoinEd In GrouP Is DonE ! =>') if event.sender_id in Account else await event.reply('- JoinEd In GrouP Is DonE ! =>')
            except: await event.edit('- Stupid,\nth3 Account Is In th3 member GrouD ! :|') if event.sender_id in Account else await event.reply('- Stupid,\nth3 Account Is In th3 member GrouD ! :|')
    else:
        try:
            await Client(JoinChannelRequest(event.raw_text.split()[1]))
            await event.edit('- DonE ! JoinEd =>') if event.sender_id in Account else await event.reply('- DonE ! JoinEd =>') 
        except:
            await event.edit('- ErroR ! =|') if event.sender_id in Account else await event.reply('- ErroR ! =|')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» InFO BOT:
@Client.on(events.NewMessage(pattern = '(I|i)nfo', from_users = Account))
async def SeYInFO(event: events.NewMessage.Event):
    if event.raw_text.lower() == 'info':
        await event.edit(f'- InFO PLSelF v.{pl.version} :\n\n- sudoS = {len(sudo)}\n- PV UseR = {len(clir.lrange("plAcUserInPV",0 ,-1))}\n- user = {getpwuid(os.getuid())[0]}\n- python3 version = {sys.version.split()[0]}\n- telethon version = {tver}\n') if event.sender_id in Account else await event.reply(f'- InFO PLSelF v.{pl.version} :\n\n- sudoS = {len(sudo)}\n- PV UseR = {len(clir.lrange("plAcUserInPV",0 ,-1))}\n- user = {getpwuid(os.getuid())[0]}\n- python3 version = {sys.version.split()[0]}\n- telethon version = {tver}\n')
    elif event.raw_text.split()[0].lower() == 'info' and event.raw_text.split()[1] == 'pv':
        c = pl.Counter()
        users = '- user in pv:\n\n'+'\n'.join(map(lambda s:f'{c.get_num()} - [{s}](tg://user?id={s})', clir.lrange('plAcUserInPV',0 ,-1)))
        await event.edit(users) if event.sender_id in Account else await event.reply(users)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Send && SaV# Voice:
@Client.on(events.NewMessage(pattern = '(V|v)oice', from_users = Account))
async def SenDSaVOicE(event: events.NewMessage.Event):
    cmd = event.raw_text.split()
    if len(cmd) >= 2 and cmd[0].lower() == 'voice':
        if cmd[1] == 'save' and event.is_reply and len(cmd) == 3:
            voice_name = cmd[2]
            if voice_name not in clir.hgetall('plVoiCESaVE').keys():
                msg = await event.get_reply_message()
                if msg.media and type(msg.media) is types.MessageMediaDocument and msg.media.document.attributes and type(msg.media.document.attributes[0]) is types.DocumentAttributeAudio and msg.media.document.attributes[0].voice:
                    voice = pl.create_rend_name(12)
                    await Client.download_media(msg.media, os.getcwd()+'/data/voice/'+voice)
                    clir.hset('plVoiCESaVE', voice_name, voice)
                    await event.edit(f'- Don# ! voice name 2 call = {voice_name}') if event.sender_id in Account else await event.reply(f'- Don# ! voice name 2 call = {voice_name}')
            else:
                await event.edit('- Th VoiC# was already in the database !') if event.sender_id in Account else await event.reply('- Th VoiC# was already in the database !')
        elif cmd[1] == 'delete' and len(cmd) == 3:
            voice_name = cmd[2]
            if voice_name in clir.hgetall('plVoiCESaVE').keys():
                os.remove(os.getcwd()+'/data/voice/'+pl.findfile(clir.hget('plVoiCESaVE', voice_name), os.getcwd()+'/data/voice/'))
                clir.hdel('plVoiCESaVE', voice_name)
                await event.edit(f'- DoN# ! {voice_name} removed 2 database !') if event.sender_id in Account else await event.reply(f'- DoN# ! {voice_name} removed 2 database !')
            else:
                await event.edit(f'- {voice_name} not in database !') if event.sender_id in Account else await event.reply(f'- {voice_name} not in database !')
        elif cmd[1] == 'list':
            num = pl.Counter()
            await event.edit('- VoiC# list:\n\n'+'\n'.join(map(lambda x:f'{num.get_num()} - {x}' ,clir.hgetall('plVoiCESaVE').keys()))) if event.sender_id in Account else await event.reply('- VoiC# list:\n\n'+'\n'.join(map(lambda x:f'{num.get_num()} - {x}' ,clir.hgetall('plVoiCESaVE').keys())))
        else:
            voice_name = cmd[1]
            if voice_name in clir.hgetall('plVoiCESaVE').keys():
                await event.delete()
                if event.is_reply:
                    msg = await event.get_reply_message()
                    await Client.send_file(event.chat_id, os.getcwd()+'/data/voice/'+pl.findfile(clir.hget('plVoiCESaVE', voice_name), os.getcwd()+'/data/voice/'), reply_to=msg.id)
                else:
                    await Client.send_file(event.chat_id, os.getcwd()+'/data/voice/'+pl.findfile(clir.hget('plVoiCESaVE', voice_name), os.getcwd()+'/data/voice/'))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» FilE ManageR:
@Client.on(events.NewMessage(pattern = '(F|f)ile', from_users = Account))
async def SenDFuCKinGFilE(event: events.NewMessage.Event):
    cmd = event.raw_text.split()
    if len(cmd) >= 2 and cmd[0].lower() == 'file':
        if cmd[1] == 'save' and event.is_reply and len(cmd) == 3:
            file_name = cmd[2]
            if file_name not in clir.hgetall('plFuCKInGFilESaVE').keys():
                msg = await event.get_reply_message()
                if msg.media:
                    await Client.send_file(botc.BOT_USERNAME, msg.media, caption=f'kosfile {file_name}')
                    #clir.hset('plFuCKInGFilESaVE', file_name, pack_bot_file_id(msg.media))
                    await event.edit(f'- Don# ! file name 2 call = {file_name}') if event.sender_id in Account else await event.reply(f'- Don# ! file name 2 call = {file_name}')
            else:
                await event.edit('- Th fil# was already in the database !') if event.sender_id in Account else await event.reply('- Th fil# was already in the database !')
        elif cmd[1] == 'delete' and len(cmd) == 3:
            file_name = cmd[2]
            if file_name in clir.hgetall('plFuCKInGFilESaVE').keys():
                clir.hdel('plFuCKInGFilESaVE', file_name)
                await event.edit(f'- DoN# ! {file_name} removed 2 database !') if event.sender_id in Account else await event.reply(f'- DoN# ! {file_name} removed 2 database !')
            else:
                await event.edit(f'- {file_name} not in database !') if event.sender_id in Account else await event.reply(f'- {file_name} not in database !')
        elif cmd[1] == 'list':
            num = pl.Counter()
            await event.edit('- FiL# list:\n\n'+'\n'.join(map(lambda x:f'{num.get_num()} - {x}' ,clir.hgetall('plFuCKInGFilESaVE').keys()))) if event.sender_id in Account else await event.reply('- FiL# list:\n\n'+'\n'.join(map(lambda x:f'{num.get_num()} - {x}' ,clir.hgetall('plFuCKInGFilESaVE').keys())))
        else:
            file_name = cmd[1]
            if file_name in clir.hgetall('plFuCKInGFilESaVE').keys():
                reply_to = ''
                if event.is_reply:
                    reply_to = event.reply_to.reply_to_msg_id
                elif event.sender_id not in Account:
                    reply_to = event.id
                await Client.send_message(botc.BOT_USERNAME, f'kosfile {file_name} {event.chat_id} {reply_to}')
                if event.sender_id in Account:
                    await event.delete()
@Client.on(events.NewMessage(pattern = 'kosnanatmary', from_users=botc.BOT_USERNAME))
async def KosNaNatMary(event: events.NewMessage.Event):
    if event.media:
        cmd = event.raw_text.split()
        chat_id = int(cmd[1])
        reply = None
        if pl.isexistList(cmd, 2):
            reply = int(cmd[2])
        await Client.send_file(chat_id, event.media, reply_to=reply)
    await event.delete()
@bot.on(events.NewMessage(pattern = 'kosfile', from_users=Account[0]))
async def KirToKosMary(event: events.NewMessage.Event):
    if event.media:
        clir.hset('plFuCKInGFilESaVE', event.raw_text.split()[1], pack_bot_file_id(event.media))
    else:
        kos = event.raw_text.split()
        reply = ''
        if pl.isexistList(kos, 3):
            reply = kos[3]
        await bot.send_file(Account[0], clir.hget('plFuCKInGFilESaVE', kos[1]), caption = f'kosnanatmary {kos[2]} {reply}')
        await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» LefT In GrouP:
@Client.on(events.NewMessage(pattern = '(L|l)eft', from_users = Account))
async def leftchat(event: events.NewMessage.Event):
    if len(event.raw_text) == 4 and event.is_group:
        try:
            await event.edit('Bye !') if event.sender_id in Account else await event.reply('Bye !')
            await Client(LeaveChannelRequest(await Client.get_input_entity(event.chat_id)))
        except: await event.edit('- ErroR ! :|') if event.sender_id in Account else await event.reply('- ErroR ! :|')
    elif len(event.raw_text.split()) > 1 and pl.check_link(event.raw_text.split()[1], ptrn = 's'):
        link = pl.check_link(event.raw_text.split()[1], ptrn = 'l')
        try:
            await Client(LeaveChannelRequest(await Client.get_input_entity(link)))
            await event.edit('- Done ! I leftEd.') if event.sender_id in Account else await event.reply('- Done ! I leftEd.')
        except: await event.edit('- ErroR ! :|') if event.sender_id in Account else await event.reply('- ErroR ! :|')
    else:
        try:
            await Client(LeaveChannelRequest(await Client.get_input_entity(event.raw_text.split()[1])))
            await event.edit('- Done ! I leftEd.') if event.sender_id in Account else await event.reply('- Done ! I leftEd.')
        except: await event.edit('- ErroR ! :|') if event.sender_id in Account else await event.reply('- ErroR ! :|')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Delet# a messag3 from SUDO:
@Client.on(events.NewMessage(pattern = '(D|d)el', from_users = sudo))
async def DeleteMessag3(event: events.NewMessage.Event): # 0110100100100000011011000110111101110110011001010010000001101000011001010111001000100000011000100111010101110100001000000110100100100000011010000110000101110110011001010010000001110100011011110010000001100110011011110111001001100111011001010111010000100000011010000110010101110010
    if event.is_reply and event.raw_text.lower() == 'del':await Client.delete_messages(event.chat_id, event.reply_to.reply_to_msg_id);await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 MutE && UnMute --D in GrouP && PV:
@Client.on(events.NewMessage(pattern = '(M|m)ute', from_users = sudo))
async def MuteAllGP(event: events.NewMessage.Event):
    if event.is_group:
        if event.raw_text.lower() == 'mute all':
            if str(event.chat_id) not in clir.lrange('plMuteAllGP', 0, -1):
                clir.lpush('plMuteAllGP', event.chat_id)
                await event.edit(f'- Th GrouP `{event.chat_id}` has been MuteD !') if event.sender_id in Account else await event.reply(f'- Th GrouP `{event.chat_id}` has been MuteD !')
            else:
                await event.edit(f'- Th GrouP `{event.chat_id}` has been 2 MuteD before !') if event.sender_id in Account else await event.reply(f'- Th GrouP `{event.chat_id}` has been 2 MuteD before !')
        elif event.raw_text.split()[0].lower() == 'mute':
            user = None
            if len(event.raw_text.split()) == 1 and event.is_reply:
                user = await event.get_reply_message()
                if not user.from_id: return
                user = '-100{}'.format(user.from_id.channel_id) if 'channel_id' in user.from_id.to_dict() else str(user.from_id.user_id)
            elif len(event.raw_text.split()) > 1:
                if event.raw_text.split()[1][0] == '@':
                    user = await Client.get_input_entity(event.raw_text.split()[1])
                    user = '-100{}'.format(user.channel_id) if 'channel_id' in user.to_dict() else '{}'.format(user.user_id)
                elif event.raw_text.split()[1].isdigit():
                    user = str(event.raw_text.split()[1])
                elif bool(event.entities) and 'user_id' in event.entities[0].to_dict():
                    user = str(event.entities[0].user_id)
            if user != None:
                if int(user) not in sudo:
                    if str(event.chat_id) in list(clir.hgetall('plMut3UserInPG').keys()):
                        if user not in clir.hget('plMut3UserInPG', str(event.chat_id)).split():
                            pl.adduserinMuteGp2hset(clir ,'plMut3UserInPG', str(event.chat_id), user)
                            await event.edit(f'- User `{user}` has been MuteD !') if event.sender_id in Account else await event.reply(f'- User `{user}` has been MuteD !')
                        else:
                            await event.edit(f'- User `{user}` has been MuteD bofore !') if event.sender_id in Account else await event.reply(f'- User `{user}` has been MuteD bofore !')    
                    else:
                        pl.adduserinMuteGp2hset(clir ,'plMut3UserInPG', str(event.chat_id), user)
                        await event.edit(f'- User `{user}` has been MuteD !') if event.sender_id in Account else await event.reply(f'- User `{user}` has been MuteD !')
                else:
                    await event.edit('- User is SUDO :| !') if event.sender_id in Account else await event.reply('- User is SUDO :| !')
    elif event.raw_text.lower() == 'mute' and event.sender_id == Account and event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if msg.peer_id.user_id == Account:
            return
        if str(msg.peer_id.user_id) not in clir.lrange('plMutePVUsEr', 0, -1):
            await event.edit(f'- User `{msg.peer_id.user_id}` has been MuteD !')
            clir.lpush('plMutePVUsEr', msg.peer_id.user_id)
        else:
            await event.edit(f'- User `{msg.peer_id.user_id}` has been MuteD bofore !')
@Client.on(events.NewMessage(pattern = '(U|u)nmute', from_users = sudo))
async def UnMuteAllGP(event: events.NewMessage.Event):
    if event.is_group:
        if event.raw_text.lower() == 'unmute all':
            if str(event.chat_id) in clir.lrange('plMuteAllGP', 0, -1): 
                clir.lrem('plMuteAllGP', 0, event.chat_id)
                await event.edit(f'- Th GrouP `{event.chat_id}` It has out of MuteD !') if event.sender_id in Account else await event.reply(f'- Th GrouP `{event.chat_id}` It has out of MuteD !')
            else:
                await event.edit(f'- Th GrouP `{event.chat_id}` has not been MuteD !') if event.sender_id in Account else await event.reply(f'- Th GrouP `{event.chat_id}` has not been MuteD !')
        elif event.raw_text.split()[0].lower() == 'unmute':
            user = None
            if len(event.raw_text.split()) == 1 and event.is_reply:
                user = await event.get_reply_message()
                if not user.from_id: return
                user = '-100{}'.format(user.from_id.channel_id) if 'channel_id' in user.from_id.to_dict() else str(user.from_id.user_id)
            elif len(event.raw_text.split()) > 1:
                if event.raw_text.split()[1][0] == '@':
                    user = await Client.get_input_entity(event.raw_text.split()[1])
                    user = '-100{}'.format(user.channel_id) if 'channel_id' in user.to_dict() else '{}'.format(user.user_id)
                elif event.raw_text.split()[1].isdigit():
                    user = str(event.raw_text.split()[1])
                elif bool(event.entities) and 'user_id' in event.entities[0].to_dict():
                    user = str(event.entities[0].user_id)
            if user != None:
                if int(user) not in sudo:
                    if str(event.chat_id) in list(clir.hgetall('plMut3UserInPG').keys()):
                        if user in clir.hget('plMut3UserInPG', str(event.chat_id)).split():
                            pl.deluserinMuteGp2hset(clir ,'plMut3UserInPG', str(event.chat_id), user)
                            await event.edit(f'- User `{user}` has been UnMuteD !') if event.sender_id in Account else await event.reply(f'- User `{user}` has been UnMuteD !')
                        else:
                            await event.edit(f'- User `{user}` has no MuteD !') if event.sender_id in Account else await event.reply(f'- User `{user}` has no MuteD !')       
                    else:
                        await event.edit(f'- User `{user}` has no MuteD !') if event.sender_id in Account else await event.reply(f'- User `{user}` has no MuteD !')
                else:
                    await event.edit('- User is SUDO :| !') if event.sender_id in Account else await event.reply('- User is SUDO :| !')
    elif event.raw_text.lower() == 'unmute' and event.sender_id == Account and event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if msg.peer_id.user_id == Account:return
        if str(msg.peer_id.user_id) in clir.lrange('plMutePVUsEr', 0, -1):
            clir.lrem('plMutePVUsEr', 0, msg.peer_id.user_id)
            await event.edit(f'- User `{msg.peer_id.user_id}` has been UnMuteD !')
        else:
            await event.edit(f'- User `{msg.peer_id.user_id}` has no MuteD !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Th Banned User IN GP:
@Client.on(events.NewMessage(pattern = '(B|b)an', from_users = sudo, func=lambda e:e.is_group))
async def BaNnedUserInGP(event: events.NewMessage.Event):
    if len(event.raw_text.split()) == 2:
        if event.raw_text.split()[1][0] == '@':
            user = await Client.get_input_entity(event.raw_text.split()[1])
            if 'user_id' in user.to_dict():
                await Client(EditBannedRequest(event.chat_id, user.user_id, ChatBannedRights(until_date=None, view_messages=True)))
                await event.edit(f'- User `{user.user_id}` has been Banned !') if event.sender_id in Account else await event.reply(f'- User `{user.user_id}` has been Banned !')
        elif event.raw_text.split()[1].isdigit():
            await Client(EditBannedRequest(event.chat_id, int(event.raw_text.split()[1]), ChatBannedRights(until_date=None, view_messages=True)))
            await event.edit(f'- User `{int(event.raw_text.split()[1])}` has been Banned !') if event.sender_id in Account else await event.reply(f'- User `{int(event.raw_text.split()[1])}` has been Banned !')
        elif bool(event.entities) and 'user_id' in event.entities[0].to_dict():
            await Client(EditBannedRequest(event.chat_id, event.entities[0].user_id, ChatBannedRights(until_date=None, view_messages=True)))
            await event.edit(f'- User `{event.entities[0].user_id}` has been Banned !') if event.sender_id in Account else await event.reply(f'- User `{event.entities[0].user_id}` has been Banned !')
    elif event.is_reply and event.raw_text.lower() == 'ban':
        msg = await event.get_reply_message()
        user = msg.from_id.channel_id if 'channel_id' in msg.from_id.to_dict() else msg.from_id.user_id
        if user in sudo:
            await event.edit(f'- User `{user}` is SUDO :| !') if event.sender_id in Account else await event.reply(f'- User `{user}` is SUDO :| !')
        else:
            try: await Client(EditBannedRequest(event.chat_id, user, ChatBannedRights(until_date=None, view_messages=True)))
            except:
                await event.edit('- ErroR !') if event.sender_id in Account else await event.reply('- ErroR !')
            else:
                await event.edit(f'- User `{user}` has been Banned !') if event.sender_id in Account else await event.reply(f'- User `{user}` has been Banned !')
#   -» Th UnBanned User IN GP:
@Client.on(events.NewMessage(pattern = '(U|u)nban', from_users = sudo))
async def BaNnedUserInGP(event: events.NewMessage.Event):
    if len(event.raw_text.split()) == 2:
        if event.raw_text.split()[1][0] == '@':
            user = await Client.get_input_entity(event.raw_text.split()[1])
            if 'user_id' in user.to_dict():
                await Client.edit_permissions(event.chat_id, user.user_id, until_date=None, view_messages=True)
                await event.edit(f'- User `{user.user_id}` has been UnBanned !') if event.sender_id in Account else await event.reply(f'- User `{user.user_id}` has been UnBanned !')
        elif event.raw_text.split()[1].isdigit():
            await Client.edit_permissions(event.chat_id, int(event.raw_text.split()[1]), until_date=None, view_messages=True)
            await event.edit(f'- User `{int(event.raw_text.split()[1])}` has been UnBanned !') if event.sender_id in Account else await event.reply(f'- User `{int(event.raw_text.split()[1])}` has been UnBanned !')
        elif bool(event.entities) and 'user_id' in event.entities[0].to_dict():
            await Client.edit_permissions(event.chat_id, event.entities[0].user_id, until_date=None, view_messages=True)
            await event.edit(f'- User `{event.entities[0].user_id}` has been UnBanned !') if event.sender_id in Account else await event.reply(f'- User `{event.entities[0].user_id}` has been UnBanned !')
    elif event.is_reply and event.raw_text.lower() == 'unban':
        msg = await event.get_reply_message()
        user = msg.from_id.channel_id if 'channel_id' in msg.from_id.to_dict() else msg.from_id.user_id
        try: await Client.edit_permissions(event.chat_id, user, until_date=None, view_messages=True)
        except:
            await event.edit('- ErroR !') if event.sender_id in Account else await event.reply('- ErroR !')
        else:
            await event.edit(f'- User `{user}` has been UnBanned !') if event.sender_id in Account else await event.reply(f'- User `{user}` has been UnBanned !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Set ManageR: 
@Client.on(events.NewMessage(pattern = '(S|s)et', from_users = sudo))
async def SetManageR(event: events.NewMessage.Event):
    cmd = event.raw_text.split()
    if len(cmd) >= 3 and cmd[0].lower() == 'set':
        if cmd[1] == 'bio':
            bio = event.raw_text[event.raw_text.find(' ', 5)+1:]
            if bio == 'delete':
                clir.delete('plFuckinBio')
                await Client(UpdateProfileRequest(about = ''))
                await event.edit('- Don# ! bio was DeleTeD !') if event.sender_id in Account else await event.reply('- Don# ! bio was DeleTeD !')
            else:
                if len(bio) <= 70:
                    clir.set('plFuckinBio', bio)
                    await Client(UpdateProfileRequest(about = bio))
                    await event.edit(f'- Don# ! bio = {bio}') if event.sender_id in Account else await event.reply(f'- Don# ! bio = {bio}')
        elif cmd[1] == 'username':
            username = event.raw_text[event.raw_text.find(' ', 5)+1:]
            if username == 'delete':
                await Client(UpdateUsernameRequest(''))
                await event.edit('- Don# ! username was DeleTeD !') if event.sender_id in Account else await event.reply('- Don# ! username was DeleTeD !')
            else:
                await Client(UpdateUsernameRequest(username))
                await event.edit(f'- Don# ! username = {username}') if event.sender_id in Account else await event.reply(f'- Don# ! username = {username}')
        elif cmd[1] == 'name':
            name = event.raw_text[event.raw_text.find(' ', 5)+1:]
            await Client(UpdateProfileRequest(first_name = name))
            await event.edit(f'- Don# ! name = {name}') if event.sender_id in Account else await event.reply(f'- Don# ! name = {name}')
        elif cmd[1] == 'lastname':
            lastname = event.raw_text[event.raw_text.find(' ', 5)+1:]
            if lastname == 'delete':
                await Client(UpdateProfileRequest(last_name = ''))
                await event.edit('- Don# ! lastname was DeleTeD !') if event.sender_id in Account else await event.reply('- Don# ! lastname was DeleTeD !')
            else:
                await Client(UpdateProfileRequest(last_name = lastname))
                await event.edit(f'- Don# ! lastname = {lastname}') if event.sender_id in Account else await event.reply(f'- Don# ! lastname = {lastname}')
        elif cmd[1] == 'profile':
            if event.raw_text.split()[2] == 'this' and event.is_reply:
                msg = await event.get_reply_message()
                if msg.media:
                    pic_name = pl.create_rend_name(10)
                    await Client.download_media(msg.media, file=pic_name)
                    Fil3 = pl.findfile(pic_name, os.getcwd())
                    pic = await Client.upload_file(os.getcwd()+'/'+Fil3)
                    try:
                        if Fil3.endswith('.mp4'):
                            await Client(UploadProfilePhotoRequest(video=pic))
                        else:
                            await Client(UploadProfilePhotoRequest(file=pic))
                    except Exception as e:
                        os.remove(Fil3)
                        await event.edit(str(e)) if event.sender_id in Account else await event.reply(str(e))
                    else:
                        if event.sender_id in Account:
                            await event.delete()
                        await msg.reply('- Don# ! profile SetED !')
                        os.remove(Fil3)
            elif cmd[2] == 'group':
                if event.is_reply and event.is_group:
                    msg = await event.get_reply_message()
                    if msg.media:
                        pic_name = pl.create_rend_name(10)
                        await Client.download_media(msg.media, file=pic_name)
                        Fil3 = pl.findfile(pic_name, os.getcwd())
                        pic = await Client.upload_file(os.getcwd()+'/'+Fil3)
                        await Client(EditPhotoRequest(event.chat_id, pic))
                        if event.sender_id in Account:
                            await event.delete()
                        await msg.reply('- Don# ! profile SetED !')
                        os.remove(Fil3)
            elif cmd[2] == 'delete':
                await Client(DeletePhotosRequest([(await Client.get_profile_photos('me'))[0]]))
                await event.edit(f'- Don# ! a Profile DeleTeD !') if event.sender_id in Account else await event.reply(f'- Don# ! a Profile DeleTeD !')
            elif cmd[2] == 'deleteall':
                await Client(DeletePhotosRequest((await Client.get_profile_photos('me'))))
                await event.edit(f'- Don# ! All Profile WaS DeleTeD !') if event.sender_id in Account else await event.reply(f'- Don# ! All Profile WaS DeleTeD !')
        elif cmd[1] == 'randname':
            if cmd[2] == 'on':
                if bool(clir.get('plSetrandnameNow')):
                        await event.edit('- The randname was already ON') if event.sender_id in Account else await event.reply('- The randname was already ON')
                else:
                    clir.set('plSetrandnameNow', 'KoSKoS')
                    await event.edit('- DonE ! SeT randname is ON !') if event.sender_id in Account else await event.reply('- DonE ! SeT randname is ON !')
            elif cmd[2] == 'off':
                get_re = clir.get('plSetrandnameNow')
                if bool(get_re):
                    await event.edit('- DonE ! SeT randname is OFF !') if event.sender_id in Account else await event.reply('- DonE ! SeT randname is OFF !')
                    clir.delete('plSetrandnameNow')
                else: await event.edit('- The randname was already OFF') if event.sender_id in Account else await event.reply('- The randname was already OFF')
        elif cmd[1] == 'lasttime':
            if cmd[2] == 'on':
                if bool(clir.get('plSetTimENow')):
                    await event.edit('- The lasttime was already ON') if event.sender_id in Account else await event.reply('- The lasttime was already ON')
                else:
                    full = (await Client.get_me()).last_name or '<<<!@n@!@dlfd;f;sfldssdkskmadki!l!l>>>'
                    clir.set('plSetTimENow', full)
                    await event.edit('- DonE ! SeT LasT Tim3 is ON !') if event.sender_id in Account else await event.reply('- DonE ! SeT LasT Tim3 is ON !')
            elif cmd[2] == 'off':
                get_re = clir.get('plSetTimENow')
                if bool(get_re):
                    await event.edit('- DonE ! SeT LasT Tim3 is OFF !') if event.sender_id in Account else await event.reply('- DonE ! SeT LasT Tim3 is OFF !')
                    await Client(UpdateProfileRequest(last_name = '')) if get_re == '<<<!@n@!@dlfd;f;sfldssdkskmadki!l!l>>>' else await Client(UpdateProfileRequest(last_name = get_re))
                    clir.delete('plSetTimENow')
                else: await event.edit('- The time was already OFF') if event.sender_id in Account else await event.reply('- The time was already OFF')
        elif cmd[1] == 'biotime':
            if cmd[2] == 'on':
                if bool(clir.get('plBioTimENow')):
                    await event.edit('- The biotime was already ON') if event.sender_id in Account else await event.reply('- The biotime was already ON')
                else:
                    clir.set('plBioTimENow', 'KoSKoS=D')
                    await event.edit('- DonE ! biotime is ON !') if event.sender_id in Account else await event.reply('- DonE ! biotime is ON !')
            elif cmd[2] == 'off':
                if bool(clir.get('plBioTimENow')):
                    await event.edit('- DonE ! SeT biotime is OFF !') if event.sender_id in Account else await event.reply('- DonE ! SeT biotime is OFF !')
                    clir.delete('plBioTimENow')
        elif cmd[1] == 'forward':
            if cmd[2] == 'off':
                if bool(clir.get('plForWardSendOrno')):
                    clir.delete('plForWardSendOrno')
                    await event.edit('- done, the forward has offline') if event.sender_id in Account else await event.reply('- done, the forward has offline')
                else:
                    await event.edit('- the forward was already offline') if event.sender_id in Account else await event.reply('- the forward was already offline')
            elif cmd[2] == 'on':
                if bool(clir.get('plForWardSendOrno')):
                    await event.edit('- the forward was already online') if event.sender_id in Account else await event.reply('- the forward was already online')
                else:
                    clir.set('plForWardSendOrno', 'True')
                    await event.edit('- done, the forward has online') if event.sender_id in Account else await event.reply('- done, the forward has online')

# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» PIN MsG : 
@Client.on(events.NewMessage(pattern = '(P|p)in', from_users = sudo, func=lambda e:e.raw_text.lower() == 'pin'))
async def PINMessaG3(event: events.NewMessage.Event):
    if event.is_reply and event.raw_text:
        msg = await event.get_reply_message()
        await Client.pin_message(event.chat_id, msg, notify = True)
        await event.edit('- Messag# Pinned !') if event.sender_id in Account else await event.reply('- Messag# Pinned !')
@Client.on(events.NewMessage(pattern = '(U|u)npin', from_users = sudo, func=lambda e:e.raw_text.lower() == 'unpin'))
async def UnPINMessaG3(event: events.NewMessage.Event):
    if event.is_group:
        msg = await Client.get_messages(event.chat_id, ids=types.InputMessagePinned())
        if msg != None:
            await Client.unpin_message(event.chat_id, msg.id)
            await event.delete() and await Client.send_message(event.chat_id, '- msg unpined !', reply_to=msg.id) if event.sender_id in Account else await Client.send_message(event.chat_id, '- msg unpined !', reply_to=msg.id) 
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SpeedTesT:
@Client.on(events.NewMessage(pattern = '(S|s)peedtest', from_users = sudo))
async def SpeeDTesT(event: events.NewMessage.Event):
    if event.raw_text.lower() == 'speedtest':
        msg = await event.edit('- FuckinG WaiT !') if event.sender_id in Account else await event.reply('- FuckinG WaiT !')
        st = Speedtest()
        FuckingTIME = dt.now()
        st.get_servers()
        st.get_best_server()
        st.download()
        st.upload()
        res = st.results.dict()
        await msg.edit(f'- result from **speedtest.net** after {(dt.now()-FuckingTIME).seconds}s :\n\n- download = {res["download"]:,} Mbps\n- upload = {res["ping"]:,} Mbps\n- ping = {res["ping"]} ms')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» PING CMD:
@Client.on(events.NewMessage(pattern = '(P|p)ing', from_users = sudo, func=lambda e:e.raw_text.lower() == 'ping'))
async def PING(event: events.NewMessage.Event):
    TStarT = dt.now()
    kosmsg = await Client.send_message(event.chat_id, '-- ping cmd !')
    await event.edit(f'- bot is ON ! **ping {(dt.now()-TStarT).microseconds/1000} ms**') if event.sender_id in Account else await event.reply(f'- bot is ON ! **ping {(dt.now()-TStarT).microseconds/1000} ms**')
    await kosmsg.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SenD FuckinG Gam3:
@Client.on(events.NewMessage(pattern = '(G|g)ame', from_users = sudo, func=lambda e:e.raw_text.lower() == 'game'))
async def SendFGam3(event: events.NewMessage.Event):
    result = await Client.inline_query('gamee', '', entity=event.chat_id)           
    await result[rand.randint(0, len(result)-1)].click(reply_to=event.id)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Block && UnBlock:
@Client.on(events.NewMessage(pattern = '(B|b)lock', from_users = Account, func=lambda e:e.raw_text.lower() == 'block'))
async def ThBlockEdUseR(event: events.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if event.is_group:
            await event.edit(f'- User `{msg.from_id.user_id}` has been blocked !')
            await Client(BlockRequest(msg.from_id.user_id))
        else:
            await event.edit(f'- User `{msg.peer_id.user_id}` has been blocked !')
            await Client(BlockRequest(msg.peer_id.user_id))

@Client.on(events.NewMessage(pattern = '(U|u)nblock', from_users = Account, func=lambda e:e.raw_text.lower() == 'unblock'))
async def ThUnBlockEdUseR(event: events.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if event.is_group:
            await event.edit(f'- User `{msg.from_id.user_id}` has been unblocked !')
            await Client(UnblockRequest(msg.from_id.user_id))
        else:
            await event.edit(f'- User `{msg.peer_id.user_id}` has been unblocked !')
            await Client(UnblockRequest(msg.peer_id.user_id))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» MaiN Message Edit:
@Client.on(events.MessageEdited())
async def check__edited_massag3(event: events.MessageEdited.Event):await check_massag3(event)
@Client.on(events.MessageEdited(from_users = sudo))
async def MaiNMessageEdited(event: events.MessageEdited.Event):
    cmd = event.raw_text.split()[0].lower()
    if event.sender_id in Account:
        if cmd == 'flood':await FloodSpaM(event)
        elif cmd == 'wow':await GetFuckinGNuD3(event)
        elif cmd == 'antitabchi':await GetFuckinGNuD3(event)
        elif cmd == 'reload':await RestartProGraM(event)
        elif cmd == 'acdontsave':await DonTSaveMsgInChannel(event)
        elif cmd == 'join':await joinchat(event)
        elif cmd == 'left':await leftchat(event)
        elif cmd == 'info':await SeYInFO(event)
        elif cmd == 'voice':await SenDSaVOicE(event)
        elif cmd == 'file':await SenDFuCKinGFilE(event)
        elif cmd == 'set':await SetManageR(event)
        elif cmd == 'block':await ThBlockEdUseR(event)
        elif cmd == 'unblock':await ThUnBlockEdUseR(event)
        elif cmd == 'turn':await TurNFuckinGOff(event)
    if cmd == 'ping':await PING(event)
    elif cmd == 'code':await RuNCoD3(event)
    elif cmd == 'pin':await PINMessaG3(event)
    elif cmd == 'rmsg':await RMSG_CMD(event)
    elif cmd == 'insta':await InsTA(event)
    elif cmd == 'cal':await GeTCal(event)
    elif cmd == 'id':await IdProcessing(event)
    elif cmd == 'invite':await FuckinGInvalidUseR(event)
    elif cmd == 'base':await ReBaSE(event)
    elif cmd == 'morse':await ReMorsE(event)
    elif cmd == 'help':await SendHelP(event)
    elif cmd == 'lyrics':await GetLyricZ(event)
    elif cmd == 'vchat':await GrouPCalLMain(event)
    elif cmd == 'qrcode':await QrCoD3(event)
    elif cmd == 'proxy':await GetProxY(event)
    elif cmd == 'check':await CheCKDIU(event)
    elif cmd == 'time':await SeYTime(event)
    elif cmd == 'tr':await TranslatE(event)
    elif cmd == 'del':await GetProxY(event)
    elif cmd == 'mute':await MuteAllGP(event)
    elif cmd == 'unmute':await UnMuteAllGP(event)
    elif cmd == 'ban':await BaNnedUserInGP(event)
    elif cmd == 'unban':await BaNnedUserInGP(event)
    elif cmd == 'speedtest':await SpeeDTesT(event)
    elif cmd == 'game':await SendFGam3(event)
    elif cmd == 'add':await AddGrouP(event)
    elif cmd == 'rem':await RemGrouP(event)
    elif cmd == 'panel':await PANELAPI(event)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» There is nothing to say here:
@Client.on(events.NewMessage(pattern='(T|t)urn off', from_users=Account, func=lambda e:e.raw_text.lower()=='turn off'))
async def TurNFuckinGOff(event: events.NewMessage.Event):
    await event.edit('- bot went offline !') if event.sender_id in Account else await event.reply('- bot went offline !')
    await bot.disconnect()
    await Client.disconnect()
    #insta.close()
# - - - - - Anti-spam settings in the group - - - - -  #
#   -» Add GrouP 2 ReDis:
@Client.on(events.NewMessage(pattern='(A|a)dd', from_users = sudo, func=lambda e: e.is_group and e.raw_text.lower() == 'add'))
async def AddGrouP(event: events.NewMessage.Event):
    if str(event.chat_id) not in clir.hgetall('plAddGroPSettinGZ').keys():
        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps({'lock_link':False,'gp_Ch':False, 'lock_photo':False,'lock_stiker':False,'lock_gif':False,'lock_tg':False,'lock_game':False,'lock_dsh':False,'lock_voice':False,'lock_forward':False,'lock_video':False,'lock_via':False,'lock_music':False,'lock_file':False,'lock_bot':False,'lock_location':False,'lock_contact':False,'lock_caption':False,'lock_contact':False,'lock_caption':False}))
        await event.edit('- Th GrouP AddEd to database !') if event.sender_id in Account else await event.reply('- Th GrouP AddEd to database !')
    else:
        await event.edit('- Th GrouP AddEd to database before !') if event.sender_id in Account else await event.reply('- Th GrouP AddEd to database before !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RemoVeD GrouP 2 ReDis:
@Client.on(events.NewMessage(pattern='(R|r)em', from_users = sudo, func=lambda e: e.is_group and e.raw_text.lower() == 'rem'))
async def RemGrouP(event: events.NewMessage.Event):
    if str(event.chat_id) in clir.hgetall('plAddGroPSettinGZ').keys():
        clir.hdel('plAddGroPSettinGZ', str(event.chat_id))
        await event.edit('- Th GrouP DeleTeD to database !') if event.sender_id in Account else await event.reply('- Th GrouP DeleTeD to database !')
    else: 
        await event.edit('- Th GrouP DeleTeD to database before !') if event.sender_id in Account else await event.reply('- Th GrouP DeleTeD to database before !')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» BoT H3lp:
@Client.on(events.NewMessage(pattern = '(H|h)elp', from_users = sudo, func=lambda e:e.raw_text.lower() == 'help'))
async def SendHelP(event: events.NewMessage.Event):
    try: 
        if event.sender_id in Account: 
            result = await Client.inline_query(botc.BOT_USERNAME, 'fuckinghelp', entity=event.chat_id)
            await result[0].click()
            await event.delete()
        else:
            result = await Client.inline_query(botc.BOT_USERNAME, 'fuckinghelp', entity=event.chat_id)
            await result[0].click(reply_to=event.id)
    except Exception as e:
        if event.sender_id in Account:
            await event.edit(f'- ErroR : {e}')
        else:
            await event.reply(f'- ErroR : {e}')
    #await event.edit(pl.STR_HELP_BOT) if event.sender_id in Account else await event.reply(pl.STR_HELP_BOT)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SenD PaneL:
@Client.on(events.NewMessage(pattern = '(P|p)anel', from_users = sudo))
async def PANELAPI(event: events.NewMessage.Event): 
    if event.is_group and event.raw_text.lower() == 'panel':
        if str(event.chat_id) in clir.hgetall('plAddGroPSettinGZ'):
            try: 
                if event.sender_id in Account: 
                    result = await Client.inline_query(botc.BOT_USERNAME, 'panel', entity=event.chat_id)
                    await result[0].click()
                    await event.delete()
                else:
                    result = await Client.inline_query(botc.BOT_USERNAME, 'panel', entity=event.chat_id)
                    await result[0].click(reply_to=event.id)
            except Exception as e:
                if event.sender_id in Account:
                    await event.edit(f'- ErroR : {e}')
                else:
                    await event.reply(f'- ErroR : {e}')
        else:
            if event.sender_id in Account:
                await event.edit('- Th GrouP not in database !')
            else:
                await event.reply('- Th GrouP not in database !')
# - - - - - - - - - - ApI_BoT - - - - - - - - - - - -  #
#   -» InPrivat3:
@bot.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def Fohsh_be_user(event: events.NewMessage.Event):
    if event.sender_id not in Account and str(event.sender_id) not in clir.lrange('plUserInApiBoT', 0, -1):
        clir.lpush('plUserInApiBoT', str(event.sender_id))
        await event.reply('fuckU!&&bye.')
#   -» 
@bot.on(events.InlineQuery(pattern="CkTabchi", users = Account))
async def ChTabchi(event: events.InlineQuery.Event): # 'ChTabchi '+data+' '+str(event.sender_id)
    if event.query.user_id in Account:
        pic_name = event.original_update.query.split()[1]
        user = event.original_update.query.split()[2]
        but = [Button.inline(pl.create_rend_name(4), data='ftabchi '+user) for _ in range(4)]
        but[rand.randint(0,3)] = Button.inline(pic_name, data='ttabchi '+user) 
        buttons = [ 
            ( 
                but[0],
                but[1],
            ),
            (
                but[2],
                but[3],
            ),
            (
                Button.inline('°• ‌Ban •°', data='tban'+user),
                Button.inline('°• UnResT •°', data='tunrt'+user),
            ),]
        builder = event.builder
        result = await builder.photo(pic_name+'.jpg',text=f'با سلام [کاربر](tg://user?id={user}) گرامی:\nلطفا کد کپچای درست را انتخاب کنید.', buttons=buttons)
        await event.answer([result])
        os.remove(pic_name+'.jpg')
#   -»
@bot.on(events.InlineQuery(pattern='fuckinghelp', users=Account))
async def SenDFucKinGHelP(event: events.InlineQuery.Event):
    buttons = [
        (
            Button.inline('°• AnTi SpaM GP •°', data='fuckinghelp1'),
        ),
        (
            Button.inline('°• KosSher FUN •°', data='fuckinghelp2'),
            Button.inline('°• Account HELP •°', data='fuckinghelp3')
        ),
        (Button.inline("°• [ ExiT ] •°", data="exitpl"),)
    ]
    builder = event.builder
    kos = await builder.article(title='fuckinghelp', text=f'**°• WlC 2 Th source help page! | pl-self v.{pl.version} •°**', buttons=buttons)
    await event.answer([kos])
#   -» 
@bot.on(events.InlineQuery(pattern="panel", users = Account)) 
async def gpanel_1(event: events.InlineQuery.Event):
    if event.query.user_id in Account:
        buttons = [
            (
                Button.inline(f"°• Settings •°", data="gpl1"),
            ),
            (
                Button.inline("°• List Mute GP •°", data="list_mute_gp"),
                Button.inline("°• List Mute PV •°", data="list_mute_pv"),
            ),
            (Button.inline("°• [ ExiT ] •°", data="exitpl"),)
        ]
        builder = event.builder
        result = await builder.article(title='panel', text='°• Welcome to the management panel of Group!\nPlease choose: •°', buttons=buttons)
        await event.answer([result])
async def panel_1(event: events.InlineQuery.Event):
    database = clir.hget('plAddGroPSettinGZ', str(event.chat_id))
    if database == None:return
    else:database = js.loads(database)
    buttons = [
        (
            Button.inline(f"°• Link [{'✔️' if database['lock_link'] else '✖️'}] •°", data="lock_link"),
            Button.inline(f"°• Photo [{'✔️' if database['lock_photo'] else '✖️'}] •°", data="lock_photo"),
        ),
        (
            Button.inline(f"°• Stiker [{'✔️' if database['lock_stiker'] else '✖️'}] •°", data="lock_stiker"),
            Button.inline(f"°• Gif [{'✔️' if database['lock_gif'] else '✖️'}] •°", data="lock_gif"),
        ),
        (
            Button.inline(f"°• Tg [{'✔️' if database['lock_tg'] else '✖️'}] •°", data="lock_tg"),
            Button.inline(f"°• Game [{'✔️' if database['lock_game'] else '✖️'}] •°", data="lock_game"),
        ),
        (
            Button.inline(f"°• Dsh [{'✔️' if database['lock_dsh'] else '✖️'}] •°", data="lock_dsh"),
            Button.inline(f"°• Voice [{'✔️' if database['lock_voice'] else '✖️'}] •°", data="lock_voice"),
        ),
        (
            Button.inline(f"°• Forward [{'✔️' if database['lock_forward'] else '✖️'}] •°", data="lock_forward"),
            Button.inline(f"°• Video [{'✔️' if database['lock_video'] else '✖️'}] •°", data="lock_video"),
        ),
        (Button.inline("[ ↻ ]", data="gpl2"),),
        (Button.inline(f"°• BacK •°", data="bk_panel"),),
    ]
    await event.edit('°• Menu: (1/2) •°', buttons=buttons)
async def panel_2(event: events.InlineQuery.Event):
    database = js.loads(clir.hget('plAddGroPSettinGZ', str(event.chat_id)))
    buttons = [
        (
            Button.inline(f"°• Via [{'✔️' if database['lock_via'] else '✖️'}] •°", data="lock_via"),
            Button.inline(f"°• Music [{'✔️' if database['lock_music'] else '✖️'}] •°", data="lock_music"),
        ),
        (
            Button.inline(f"°• File [{'✔️' if database['lock_file'] else '✖️'}] •°", data="lock_file"),
            Button.inline(f"°• Bot [{'✔️' if database['lock_bot'] else '✖️'}] •°", data="lock_bot"),
        ),
        (
            Button.inline(f"°• Location [{'✔️' if database['lock_location'] else '✖️'}] •°", data="lock_location"),
            Button.inline(f"°• Contact [{'✔️' if database['lock_contact'] else '✖️'}] •°", data="lock_contact"),
        ),
        (
            Button.inline(f"°• Caption [{'✔️' if database['lock_caption'] else '✖️'}] •°", data="lock_caption"),
            Button.inline(f"°• chT CH [{'✔️' if database['gp_Ch'] else '✖️'}] •°", data="gpchat_ch"),
        ),
        (Button.inline("[ ↻ ]", data="gpl1"),),
        (Button.inline(f"°• BacK •°", data="bk_panel"),),
    ]
    await event.edit("Menu (2/2)",buttons=buttons)
async def pl_main(event: events.InlineQuery.Event):
    buttons = [
            (
                Button.inline(f"°• Settings •°", data="gpl1"),
            ),
            (
                Button.inline("°• List Mute GP •°", data="list_mute_gp"),
                Button.inline("°• List Mute PV •°", data="list_mute_pv"),
            ),
            
            (Button.inline("°• [ ExiT ] •°", data="exitpl"),
            )
        ]
    await event.edit('°• Welcome to the management panel of Group!\nPlease choose: •°', buttons=buttons)
@bot.on(events.CallbackQuery)
async def main_call(event: events.CallbackQuery.Event):
    buttons = [(Button.inline("°• [ BacK ] •°", data="bk_panel"),),]
    if (event.data.split()[0] == b"ftabchi" or event.data.split()[0] == b"ttabchi"):
        if event.original_update.user_id == int(event.data.split()[1]):
            return await cktabchi(event)
        else : await event.answer('برای تو نیستش.',alert= True)
    elif event.query.user_id in sudo:
        try: 
            if event.data == b"gpl1": 
                return await panel_1(event)
            elif event.data == b"gpl2":
                return await panel_2(event)
            elif event.data == b"bk_panel":
                return await pl_main(event)
            elif event.data == b"exitpl":
                return await event.edit('- The panel was closed !')
            elif event.data == b"list_mute_pv":
                return await event.edit('Muted User in Pv :'+' - '.join(clir.lrange('plMutePVUsEr', 0, -1)),buttons=buttons)
            elif event.data == b"list_mute_gp":
                return await event.edit('Muted User in GrouP :',clir.hgetall('plMut3UserInPG'),buttons=buttons)
            elif event.data == b"lock_link" or event.data == b"lock_photo" or event.data == b"lock_stiker" or event.data == b"lock_gif" or event.data == b"lock_tg" or event.data == b"lock_game":
                return await main_call(event)
            elif  event.data == b"lock_dsh" or event.data == b"lock_voice" or event.data == b"lock_forward" or event.data == b"lock_video" or event.data == b"lock_via" or event.data == b"lock_music":
                return await main_call(event)
            elif  event.data == b"lock_file" or event.data == b"lock_bot" or event.data == b"lock_location" or event.data == b"gpchat_ch" or event.data == b"lock_contact" or event.data == b"lock_caption":
                return await main_call(event)
            elif event.data.split()[0] == b"tban" or event.data.split()[0] == b"tunrt": 
                return await cktabchi(event)
        except MessageNotModifiedError as e:
            await event.answer('اهسته تر', alert= True)  
    else:
        await event.answer('- You do not have this access !')
async def main_call(event: events.CallbackQuery.Event):
    database = clir.hget('plAddGroPSettinGZ', str(event.chat_id))
    if database == None: return
    else: database = js.loads(database)
    if event.query.user_id in sudo: 
            try: 
                if event.data == b"lock_link": 
                    if database['lock_link']:
                        database['lock_link'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_link'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_photo":
                    if database['lock_photo']:
                        database['lock_photo'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_photo'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_stiker":
                    if database['lock_stiker']:
                        database['lock_stiker'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_stiker'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_gif":
                    if database['lock_gif']:
                        database['lock_gif'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_gif'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_tg":
                    if database['lock_tg']:
                        database['lock_tg'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        await panel_1(event)
                    else:
                        database['lock_tg'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_game":
                    if database['lock_game']:
                        database['lock_game'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_game'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_dsh":
                    if database['lock_dsh']:
                        database['lock_dsh'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_dsh'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_voice":
                    if database['lock_voice']:
                        database['lock_voice'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_voice'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_forward":
                    if database['lock_forward']:
                        database['lock_forward'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_forward'] = True
                        clir.hset('plAddGroPSetticktabchinGZ', str(event.chat_id), js.dumps(database))
                        await panel_1(event)
                elif event.data == b"lock_video":
                    if database['lock_video']:
                        database['lock_video'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                    else:
                        database['lock_video'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_1(event)
                elif event.data == b"lock_via":
                    if database['lock_via']:
                        database['lock_via'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_via'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"lock_music":
                    if database['lock_music']:
                        database['lock_music'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_music'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"lock_file":
                    if database['lock_file']:
                        database['lock_file'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_file'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"lock_bot":
                    if database['lock_bot']:
                        database['lock_bot'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_bot'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"lock_location":
                    if database['lock_location']:
                        database['lock_location'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_location'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"gpchat_ch":
                    if database['gp_Ch']:
                        database['gp_Ch'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['gp_Ch'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"lock_contact":
                    if database['lock_contact']:
                        database['lock_contact'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_contact'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                elif event.data == b"lock_caption":
                    if database['lock_caption']:
                        database['lock_caption'] = False
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)
                    else:
                        database['lock_caption'] = True
                        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(database))
                        return await panel_2(event)   
            except MessageNotModifiedError as e:
                await event.answer('اهسته تر',alert= True)  
    else:
         await event.answer('-You do not have this access!') 
async def cktabchi(event: events.CallbackQuery.Event): 
    if str(event.chat_id) in clir.hgetall('AnTITABCiE').keys():
        database = js.loads(clir.hget('AnTITABCiE', str(event.chat_id)))
        if event.data.split()[0] == b"ftabchi":
            if event.query.user_id not in database:database.append(event.query.user_id) 
            await event.answer('- FuCk you :)',alert= True)  # event.query.user_id 
            clir.hset("AnTITABCiE", str(event.chat_id),  js.dumps(database))
        elif event.data.split()[0] ==  b"ttabchi":
            if event.query.user_id not in database:database.append(event.query.user_id)
            await event.edit(f'[کاربر](tg://user?id={int(event.data.split()[1])}) با موفقیت سنجش تبچی رو پشت سر گزاشتند')
            await Client.edit_permissions(event.chat_id, event.query.user_id, view_messages= True, send_messages= True, send_media= True, send_stickers= True, send_gifs= True, send_games= True, send_inline= True, embed_link_previews= True, send_polls= True, change_info= True, invite_users = True)
            #, view_messages: bool = True, send_messages: bool = True, send_media: bool = True, send_stickers: bool = True, send_gifs: bool = True, send_games: bool = True, send_inline: bool = True, embed_link_previews: bool = True, send_polls: bool = True, change_info: bool = True, invite_users: bool = True, pin_messages: bool = True
            await event.answer('- You\'ve been accepted !') 
            clir.hset("AnTITABCiE", str(event.chat_id), js.dumps(database))
        elif event.data.split()[0] ==  b"tban":
            await Client(EditBannedRequest(event.chat_id, str(event.data.split()[1]), ChatBannedRights(until_date=None, view_messages=True)))
        elif event.data.split()[0] ==  b"tunrt":
            await Client.edit_permissions(event.chat_id, str(event.data.split()[1]), view_messages= True, send_messages= True, send_media= True, send_stickers= True, send_gifs= True, send_games= True, send_inline= True, embed_link_previews= True, send_polls= True, change_info= True, invite_users = True)
# - - - - - - - - - - lasT-Tim3 - - - - - - - - - - -  #
async def ChangeLasTName(): 
    if bool(clir.get('plSetTimENow')):await Client(UpdateProfileRequest(last_name = pl.crtime(dt.today().hour, dt.today().minute)))
async def ChangeBioTimE():
    if bool(clir.get('plBioTimENow')):await Client(UpdateProfileRequest(about=(clir.get('plFuckinBio') or '')+pl.crbiotime(dt.now().hour if dt.now().hour < 12 else dt.now().hour - 12))) 
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
scheduler = AsyncIOScheduler(timezone="Asia/Tehran")
scheduler.add_job(ChangeLasTName, "interval", minutes = 1, next_run_time=f'{dt.today().year}-{dt.today().month}-{dt.today().day} {dt.today().hour}:{dt.today().minute}:00' ) 
scheduler.add_job(ChangeBioTimE, "interval", hours = 1, next_run_time=f'{dt.today().year}-{dt.today().month}-{dt.today().day} {dt.today().hour}:00:00' ) 
scheduler.start() 
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
Client.run_until_disconnected()
bot.run_until_disconnected()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #