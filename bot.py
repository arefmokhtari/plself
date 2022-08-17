#                   [   Plague Dr.  ]
# - - - - - - - - - - -LIBRarYS- - - - - - - - - - - - #
from telethon import TelegramClient, events, Button, types, __version__ as tver
from telethon.tl.functions.messages import ImportChatInviteRequest, CheckChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest, EditBannedRequest, InviteToChannelRequest, EditPhotoRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import InputPeerChannel, InputPeerUser, ChatBannedRights
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.phone import CreateGroupCallRequest, JoinGroupCallRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.utils import pack_bot_file_id
from googletrans import Translator
import instaloader
from shazamio import Shazam
import qrcode
from phonenumbers import geocoder, carrier, parse as FuckingPhone
from whois import whois
from pwd import getpwuid
import plLibS as pl
import os, sys, subprocess
import json as js
import random as rand 
from datetime import datetime as dt
from captcha.image import ImageCaptcha 
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
import requests as req
from psutil import Process
from pydub import AudioSegment
# - - - - - - - - - - - ValueS - - - - - - - - - - - - #
Account = pl.botc.acc_sudo 
acc_sudo = pl.botc.main_sudo
sudo = pl.botc.sudoS
#phone = '+989360145942'
print(pl.botc.API_ID, pl.botc.INSTAGRAM)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
print(f'{pl.Color.BLACK}\n{pl.Color.BACKGROUND_RED}# ------------- [   Plague Dr.  ] ------------- #{pl.Color.RESET}\n'+pl.Color.DARK_GRAY) 
bot = TelegramClient(pl.botc.SESSION_DIR+pl.botc.SESSION_API_NAME, pl.botc.API_ID, pl.botc.API_HASH).start(bot_token=pl.botc.BOT_TOKEN)
clir = pl.bot_redis(pl.botc.REDIS_NUMBER)
insta = instaloader.Instaloader()
pl.check_insta(insta, session = pl.botc.INSTAGRAM[0], username = pl.botc.INSTAGRAM[1], passwd = pl.botc.INSTAGRAM[2])
Client = TelegramClient(pl.botc.SESSION_DIR+pl.botc.SESSION_AC_NAME, pl.botc.API_ID, pl.botc.API_HASH)
Client.start()
group_call_factory = pl.VchatCall(Client)
print('\t- Client && bot is runing ! go FucKyourSelf && Bye.', pl.Color.RESET)
print(f' {pl.Color.RED}----{pl.Color.RESET}    {pl.Color.BACKGROUND_RED}connet to {pl.botc.SESSION_AC_NAME} account !{pl.Color.RESET}    {pl.Color.RED}----{pl.Color.RESET}')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» CheckING MsG SerVic3 In GP:
@Client.on(events.Raw(types.UpdateNewChannelMessage, func=lambda e:type(e.message) is types.MessageService))
async def GetMsGServic3InGP(event: events.raw.Raw):
    chat_id = '-100'+str(event.message.peer_id.channel_id)
    type_message = type(event.message.action)
    if chat_id in clir.hgetall('AnTITABCiE').keys():
        if type_message == types.MessageActionChatJoinedByLink:
            await Client.edit_permissions(event.message.peer_id.channel_id, event.message.from_id, 
                view_messages = True,
                send_messages = False,
            )
            image = ImageCaptcha(width = 180, height = 90)
            data = pl.create_rend_name(4) 
            image.generate(data) 
            image.write(data, data+'.jpg')
            result = await Client.inline_query(pl.botc.BOT_USERNAME, 'CkTabchi '+data+' '+str(event.message.from_id), entity=event.message.peer_id.channel_id)
            await result[0].click() 
        elif type_message == types.MessageActionChatAddUser:
            for users in event.message.action.users:
                await Client.edit_permissions(event.message.peer_id.channel_id, users, 
                view_messages = True,
                send_messages = False,
                )
                image = ImageCaptcha(width = 180, height = 90)
                data = pl.create_rend_name(4) 
                image.generate(data) 
                image.write(data, data+'.jpg')
                result = await Client.inline_query(pl.botc.BOT_USERNAME, 'CkTabchi '+data+' '+str(users), entity=event.message.peer_id.channel_id)
                await result[0].click() 
    #if (chat_id in list(clir.hgetall('plAddGroPSettinGZ').keys()) and js.loads(clir.hget('plAddGroPSettinGZ', chat_id))['lock_tg']) and'action' in event.message.to_dict() and type_message is types.MessageActionChatAddUser:
    #    pass
    if chat_id in clir.lrange('plMuteAllGP', 0, -1) or (chat_id in list(clir.hgetall('plAddGroPSettinGZ').keys()) and js.loads(clir.hget('plAddGroPSettinGZ', chat_id))['lock_tg']):
        await Client.delete_messages(event.message.peer_id.channel_id, event.message.id)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» CheckING ALL Message:
@Client.on(events.NewMessage())
async def check_massag3(event: events.newmessage.NewMessage.Event):
    if event.is_private and event.sender_id != Account[0] and event.media and event.media.ttl_seconds:
        cr_file = pl.create_rend_name(10)
        await Client.download_media(event.media, os.getcwd()+'/data/photos/'+cr_file)
        await Client.send_file(pl.botc.CHANNEL_FOR_FWD, os.getcwd()+'/data/photos/'+pl.findfile(cr_file, os.getcwd()+'/data/photos'))
    if event.sender_id in sudo: 
        pass
    elif event.is_group:
        chat_id = str(event.chat_id)
        if chat_id in clir.lrange('plMuteAllGP', 0, -1) or (chat_id in clir.hgetall('plMut3UserInPG').keys() and chat_id in clir.hget('plMut3UserInPG', str(event.chat_id)).split()):
            await event.delete()
        elif chat_id in clir.hgetall('plAddGroPSettinGZ').keys():
            database = js.loads(clir.hget('plAddGroPSettinGZ', chat_id))
            if database['lock_link'] and pl.check_msg_link(event.raw_text):
                await event.delete()
            elif  database['lock_forward'] and event.fwd_from:
                await event.delete()
            elif database['gp_Ch'] and event.sender_id and event.sender_id < 0:
                await event.delete()
            elif  database['lock_bot']:pass # not idea 4 this ...
    elif event.is_private:
        sender_id = str(event.sender_id)
        get_user = None if clir.get('acdontsave:'+sender_id+':pl') == None else int(clir.get('acdontsave:'+sender_id+':pl'))
        if sender_id in clir.lrange('plMutePVUsEr', 0, -1):
            if not await pl.userisbot(clir, event):
                if get_user == None:
                    if clir.get('plForWardSendOrno'):
                        clir.setex('acdontsave:'+sender_id+':pl', 86400, 1)
                        await Client.forward_messages(pl.botc.CHANNEL_FOR_FWD, event.message)
                else:
                    if get_user < 15:
                        if clir.get('plForWardSendOrno'):
                            clir.setex('acdontsave:'+sender_id+':pl', 86400, get_user+1)
                            await Client.forward_messages(pl.botc.CHANNEL_FOR_FWD, event.message)
            await event.delete()
        elif sender_id not in clir.lrange('DonTCare2MsG', 0, -1) and not await pl.userisbot(clir, event):
            if get_user == None:
                if clir.get('plForWardSendOrno'):
                    clir.setex('acdontsave:'+sender_id+':pl', 86400, 1)
                    await Client.forward_messages(pl.botc.CHANNEL_FOR_FWD, event.message)
            else:
                if get_user < 15:
                    if clir.get('plForWardSendOrno'):
                        clir.setex('acdontsave:'+sender_id+':pl', 86400, get_user+1)
                        await Client.forward_messages(pl.botc.CHANNEL_FOR_FWD, event.message)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RMSG MSG:
@Client.on(events.NewMessage(pattern = '(R|r)msg', from_users = sudo))
async def RMSG_CMD(event:  events.newmessage.NewMessage.Event):
    try:
        msg = int(event.raw_text[5:]) 
    except:
        await pl.send_sudo_msg(event, '• **error !**', Account)
    else:
        _4sendmsg = await pl.send_sudo_msg(event, '• **wait !**', Account)
        c = 1 if event.sender_id in Account else 0
        async for message in Client.iter_messages(event.chat_id, msg+1):
            if c < 2:
                c += 1
                continue
            try:
                await message.delete()
            except Exception as er:
                await pl.send_sudo_msg(_4sendmsg, f'• **error !** `{er}`', Account)
                break
        await _4sendmsg.edit(f'• **done,** `{msg}` **msg has been deleted !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» InsTa:
@Client.on(events.NewMessage(pattern = '(I|i)nsta', from_users = sudo))
async def InsTA(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 3 and cmd[0] == 'insta':
        if cmd[1] == 'post': 
            post = instaloader.Post.from_shortcode(insta.context, cmd[2])
            insta.download_post(post, target = 'insta')
            file_name = [i for i in pl.fileindir(insta.format_filename(post), os.listdir(os.getcwd()+'/insta')) if pl.checklist4insta(i)]
            Files = [os.getcwd()+'/insta/'+fi for fi in file_name]
            if len(file_name) >= 1:
                try:
                    await Client.send_file(event.chat_id, [os.getcwd()+'/insta/'+fi for fi in file_name], reply_to=event.id, caption = f'• **username :** `{post.owner_username}`\n• **like :** `{post.likes}`\n• **Comments :** `{post.comments}`')
                except:
                    for f in Files:
                        await Client.send_file(event.chat_id, f, reply_to=event.id, caption = f'• **username :** `{post.owner_username}`\n• **like :** `{post.likes}`\n• **Comments :** `{post.comments}`')
            for FilES in os.listdir('insta'):
                os.remove('insta'+'/'+FilES)
            os.rmdir('insta')
        elif cmd[1] == 'profile':
            profile = instaloader.Profile.from_username(insta.context, cmd[2])
            insta.download_profile(profile, profile_pic_only=True)
            fucking_file = [kos for kos in os.listdir(os.getcwd()+'/'+profile.username) if kos.endswith('jpg')][0]
            await Client.send_file(event.chat_id,os.getcwd()+'/'+profile.username+'/'+fucking_file, reply_to=event.id, caption = f'• **name :** `{profile.full_name}`\n• **bio :** `{profile.biography}`\n• **followers :** `{profile.followers:,}`')
            for FilES in os.listdir(profile.username):
                os.remove(profile.username+'/'+FilES)
            os.rmdir(profile.username)
        elif cmd[1] == 'story':
            profile = instaloader.Profile.from_username(insta.context, cmd[2])
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
async def GeTCal(event: events.newmessage.NewMessage.Event):
    try: await pl.send_sudo_msg(event, f'{eval(event.raw_text[4:]):,}', Account)
    except: await pl.send_sudo_msg(event, '• **error !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Flood SpaM:
''' nothing 4 now ...
@Client.on(events.NewMessage(pattern='(F|f)lood', from_users = Account))
async def FloodSpaM(event: events.newmessage.NewMessage.Event): 
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
        if event.is_reply:
            msg = await event.get_reply_message()
            for _ in range(int(event.raw_text.split()[2])):
                await msg.reply(rand.choice(pl.KOS_FoSH))
        else:
            for _ in range(int(event.raw_text.split()[2])):
                await Client.send_message(event.chat_id, rand.choice(pl.KOS_FoSH))
    elif len(event.raw_text.split()) >= 3 and event.raw_text.split()[0].lower() == 'flood' and event.raw_text.split()[1].isdigit():
        await event.delete()
        for _ in range(int(event.raw_text.split()[1])):
            await Client.send_message(event.chat_id, event.raw_text[event.raw_text.find(' ', 6):])'''
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» get UseR ID:
@Client.on(events.NewMessage(pattern = '(I|i)d', from_users = sudo))
async def IdProcessing(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 2:
        if cmd[1][0] == '@':
            chat = await Client.get_input_entity(cmd[1])
            if 'channel_id' in chat.to_dict():
                await pl.send_sudo_msg(event, f'`-100{chat.channel_id}`', Account)
            else:
                await pl.send_sudo_msg(event, f'`-100{chat.user_id}`', Account)
        if cmd[1] == 'chat':
            if event.is_group:await pl.send_sudo_msg(event, f'`{event.chat_id}`', Account)
        elif cmd[1][0] == '-':
            chat = await Client.get_entity(int(cmd[1]))
            if chat.username == None:
                await pl.send_sudo_msg(event, '**• not username !**', Account)
            else:
                await pl.send_sudo_msg(event, f'@{chat.username}', Account)
        elif cmd[1][0].isdigit():
            await pl.send_sudo_msg(event, f'[{cmd[1]}](tg://user?id={cmd[1]})', Account)
        elif event.entities and 'user_id' in event.entities[0].to_dict():
            await pl.send_sudo_msg(event, f'`{event.entities[0].user_id}`', Account)
    elif event.is_private and event.raw_text.lower() == 'id':
        if event.is_reply:
            msg = await event.get_reply_message()
            await pl.send_sudo_msg(event, f'`{msg.peer_id.user_id}`', Account)
        else:
            await pl.send_sudo_msg(event, f'`{event.sender_id}`', Account)
    elif (event.is_group or event.is_channel) and event.raw_text.lower() == 'id':
        if event.is_reply:
            msg = await event.get_reply_message()
            user = msg.from_id
            if user:
                await pl.send_sudo_msg(event, f'`{user}`', Account)
            #if 'from_id' in msg.to_dict() and msg.from_id != None and 'channel_id' in msg.from_id.to_dict():
            #    await event.edit('`-100{}`'.format(msg.from_id.channel_id)) if event.sender_id in Account else await event.reply('`-100{}`'.format(msg.from_id.channel_id))                    
            #elif 'from_id' in msg.to_dict() and msg.from_id == None and 'peer_id' in msg.to_dict() and 'channel_id' in msg.peer_id.to_dict():
            #    await event.edit('`-100{}`'.format(msg.peer_id.channel_id)) if event.sender_id in Account else await event.reply('`-100{}`'.format(msg.peer_id.channel_id))        
            else: await pl.send_sudo_msg(event, f'`{msg.from_id.user_id}`', Account)
        else: await pl.send_sudo_msg(event, f'`{event.sender_id}`', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» invalid UseR:
@Client.on(events.NewMessage(pattern = '(I|i)nvite', from_users = sudo))
async def FuckinGInvalidUseR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 2 and cmd[0] == 'invite':
        try:
            user = await Client.get_input_entity(cmd[1])
            chat = await Client.get_input_entity(event.chat_id)
            await Client(InviteToChannelRequest(InputPeerChannel(chat.channel_id, chat.access_hash),[InputPeerUser(user.user_id, user.access_hash)]))
        except Exception as e:
            await pl.send_sudo_msg(event, '• **error** : '+str(e), Account)
        else:
            await pl.send_sudo_msg(event, f'• **user** `{user.user_id}` **added to gorup !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» FucK Off =| :
@Client.on(events.NewMessage(pattern = '(W|w)(O|o)(W|w)', from_users = acc_sudo))
async def GetFuckinGNuD3(event: events.newmessage.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if msg.media:
            cr_file = pl.create_rend_name(10)
            await Client.download_media(msg.media, os.getcwd()+'/data/photos/'+cr_file)
            await Client.send_file(pl.botc.CHANNEL_FOR_FWD, os.getcwd()+'/data/photos/'+pl.findfile(cr_file, os.getcwd()+'/data/photos'))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» MusiC ManageR:
@Client.on(events.NewMessage(pattern='(M|m)usic', from_users=sudo))
async def FinDManageR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if event.is_reply:
        msg = await event.get_reply_message()
        if msg.media and type(msg.media) is types.MessageMediaDocument and msg.media.document and msg.media.document.attributes:
            if len_cmd >= 2:
                if cmd[1] == 'find' and msg.media.document.mime_type in ['audio/ogg', 'video/mp4', 'audio/mpeg']:
                    filename = pl.create_rend_name(6)
                    await Client.download_media(msg, filename)
                    shazam = Shazam()
                    filename = pl.findfile(filename, os.getcwd())
                    if event.sender_id in Account:await event.delete()
                    _sending_msg = await msg.reply('• **wait !**')
                    out = await shazam.recognize_song(filename)
                    if out.get('track'):
                        msg4send = f'**• music info:**\n**• name:** `{out["track"]["title"]}`\n**• artist:** `{out["track"]["subtitle"]}`\n**• genre:** `{out["track"]["genres"]["primary"]}`\n**• album:** `{out["track"]["sections"][0]["metadata"][0]["text"]}`'
                    else:
                        msg4send = '• **not found !**'
                    await _sending_msg.edit(msg4send)
                    os.remove(filename)
                elif cmd[1] == 'info':
                    await pl.send_sudo_msg(event, f'**• music info:**\n**• title:** `{msg.media.document.attributes[0].title}`\n**• performer:** `{msg.media.document.attributes[0].performer}`\n**• filename:** `{msg.media.document.attributes[1].file_name}`', Account)
                elif cmd[1] == 'cut':
                    if len_cmd == 3:
                        if cmd[2].isdigit():
                            music_end = int(cmd[2])
                            await Client.download_media(msg)
                            filename = msg.media.document.attributes[1].file_name
                            sound = AudioSegment.from_mp3(filename)
                            sound[0 : music_end * 1000].export(filename)
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                            os.remove(filename)
                    elif len_cmd == 4:
                        if cmd[2].isdigit() and cmd[3].isdigit():
                            music_start = int(cmd[2])
                            music_end = int(cmd[3])
                            await Client.download_media(msg)
                            filename = msg.media.document.attributes[1].file_name
                            sound = AudioSegment.from_mp3(filename)
                            sound[music_start * 1000 : music_end * 1000].export(filename)
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                            os.remove(filename)
                    else:
                        await Client.download_media(msg)
                        filename = msg.media.document.attributes[1].file_name
                        sound = AudioSegment.from_mp3(filename)
                        sound[0 : 120000].export(filename)
                        if event.sender_id in Account: await event.delete()
                        await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                        os.remove(filename)
                elif cmd[1] == 'video' and msg.media.document.mime_type == 'video/mp4':
                    if len_cmd == 3:
                        if cmd[2].isdigit():
                            music_end = int(cmd[2])
                            filename = pl.create_rend_name(8)+'.mp4'
                            await Client.download_media(msg, filename)
                            music_name = filename[:filename.rfind('.')]+'.mp3'
                            sound = AudioSegment.from_file(filename)
                            sound[0: music_end * 1000].export(music_name, format='mp3')
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, music_name, reply_to=msg.id)
                            os.remove(filename)
                            os.remove(music_name)
                    elif len_cmd == 4:
                        if cmd[2].isdigit() and cmd[3].isdigit():
                            music_start = int(cmd[2])
                            music_end = int(cmd[3])
                            filename = pl.create_rend_name(8)+'.mp4'
                            await Client.download_media(msg, filename)
                            music_name = filename[:filename.rfind('.')]+'.mp3'
                            sound = AudioSegment.from_file(filename)
                            sound[music_start * 1000: music_end * 1000].export(music_name, format='mp3')
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, music_name, reply_to=msg.id)
                            os.remove(filename)
                            os.remove(music_name)
                    else:
                        filename = pl.create_rend_name(8)+'.mp4'
                        await Client.download_media(msg, filename)
                        music_name = filename[:filename.rfind('.')]+'.mp3'
                        sound = AudioSegment.from_file(filename)
                        sound.export(music_name, format='mp3')
                        if event.sender_id in Account: await event.delete()
                        await Client.send_file(event.chat_id, music_name, reply_to=msg.id)
                        os.remove(filename)
                        os.remove(music_name)
                elif cmd[1] == 'voice': # soon | never ... :|
                    pass # :|
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» AnTI TabCHI - CaptchA: 
@Client.on(events.NewMessage(pattern = '(A|a)ntitabchi', from_users = sudo))
async def SeTAntITabCHI(event):  
    cmd, len_cmd = pl.get_cmds(event)
    chat_id = str(event.chat_id)
    if event.is_group and len_cmd == 2 and cmd[0] == 'antitabchi':
        if cmd[1] == 'on': # 'AnTITABCiE'
            if chat_id in clir.hgetall('AnTITABCiE').keys():
                await pl.send_sudo_msg(event, '**• anti tabchi was active !**', Account)
            else:
                clir.hset('AnTITABCiE', chat_id, js.dumps([]))
                await pl.send_sudo_msg(event, '**• done, anti tabchi is active !**', Account)
        elif cmd[1] == 'off':
            if chat_id in clir.hgetall('AnTITABCiE').keys():
                clir.hdel('AnTITABCiE', chat_id)
                await pl.send_sudo_msg(event, '**• done, anti tabchi service cleared !**', Account)
            else:
                await pl.send_sudo_msg(event, '**• anti tabchi is not active !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» BaS#:
@Client.on(events.NewMessage(pattern = '(B|b)ase', from_users = sudo))
async def ReBaSE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 3 and cmd[0] == 'base' and cmd[1].isdigit():
        await pl.send_sudo_msg(event, pl.Base(event.raw_text[event.raw_text.find(' ', 5)+1:], int(cmd[1])).result(), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» MorS#:
@Client.on(events.NewMessage(pattern = '(M|m)orse', from_users = sudo))
async def ReMorsE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 2 and cmd[0]== 'morse':
        await pl.send_sudo_msg(event, ''.join([pl.switch(morse, pl.CoDMORsE, ' ')+' ' for morse in event.raw_text[6:]]), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» ReStarT Th3 ProGraM:
@Client.on(events.NewMessage(pattern = '(R|r)eload', from_users = acc_sudo, func=lambda e:e.raw_text.lower() == 'reload'))
async def RestartProGraM(event: events.newmessage.NewMessage.Event):
    await pl.send_sudo_msg(event, '• **bot reloaded !**', Account)
    os.execl(sys.executable, sys.executable, *sys.argv)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RuN CoD#:
@Client.on(events.NewMessage(pattern = '(C|c)ode', from_users = sudo))
async def RuNCoD3(event: events.newmessage.NewMessage.Event):
    cmds, len_cmd = pl.get_cmds(event)
    if len_cmd >= 2 and cmds[0] == 'code':
        cmd = cmds[1]
        if cmd == 'py3':
            file = os.getcwd()+'/data/code/'+'source.py'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['python3', file], capture_output=True, text=True)
            if code.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+code.stderr+'`', Account)
            else:
                await pl.send_sudo_msg(event, '• **result:**\n\n`'+code.stdout+'`', Account)
        elif cmd == 'py2':
            file = os.getcwd()+'/data/code/'+'source.py'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['python2', file], capture_output=True, text=True)
            if code.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+code.stderr+'`', Account)
            else:
                await pl.send_sudo_msg(event, '• **result:**\n\n`'+code.stdout+'`', Account)
        elif cmd == 'js' or cmd == 'javascript':
            file = os.getcwd()+'/data/code/'+'source.js'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['node', file], capture_output=True, text=True)
            if code.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+code.stderr+'`', Account)
            else:
                await pl.send_sudo_msg(event, '• **result:**\n\n`'+code.stdout+'`', Account)
        elif cmd == 'help':
            await pl.send_sudo_msg(event, '• **cmds :**\n`py3`\n`py2`\n`cpp`\n`c`\n`lua`\n`js`\n`java`', Account)
        elif cmd == 'cpp':
            file = os.getcwd()+'/data/code/'+'source.cpp'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            s = subprocess.run(['g++', '-std=c++11', file], capture_output=True, text=True)
            if s.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+s.stderr+'`', Account)
            else:
                code = subprocess.run(['./a.out'], capture_output=True, text=True)
                await pl.send_sudo_msg(event, '• **result:**\n\n`'+code.stdout+'`', Account)
                os.remove('a.out')
        elif cmd == 'program':
            try:await pl._exec(event.raw_text[event.raw_text.find('\n')+1:], event, Client);await pl.send_sudo_msg(event, '• **done !**', Account)
            except Exception as e:await pl.send_sudo_msg(event, str(e), Account)
        elif cmd == 'c':
            file = os.getcwd()+'/data/code/'+'source.c' 
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            s = subprocess.run(['gcc', file, '-o', 'a.out'], capture_output=True, text=True)
            if s.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+s.stderr+'`', Account)
            else:
                code = subprocess.run(['./a.out'], capture_output=True, text=True)
                await pl.send_sudo_msg(event, '• **result:**\n\n`'+code.stdout+'`', Account)
                os.remove('a.out')
        elif cmd == 'lua':
            file = os.getcwd()+'/data/code/'+'source.lua'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            code = subprocess.run(['lua', file], capture_output=True, text=True)
            if code.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+code.stderr+'`', Account)
            else:
                await pl.send_sudo_msg(event, '• **result:**\n\n`'+code.stdout+'`', Account)
        elif cmd == 'java':
            file = os.getcwd()+'/data/code/'+'source.java'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            s = subprocess.run(['javac', file], capture_output=True, text=True)
            if s.stderr != '':
                await pl.send_sudo_msg(event, '• **error:**\n\n`'+s.stderr+'`', Account)
            else:
                os.system('cp '+os.getcwd()+'/data/code/source.class '+os.getcwd())
                os.remove(os.getcwd()+'/data/code/'+'source.class')
                code = subprocess.run(['java', 'source'], capture_output=True, text=True)
                if code.stderr != '':
                    await pl.send_sudo_msg(event,  '• **error:**\n\n`'+code.stderr+'`', Account)
                else:
                    await pl.send_sudo_msg(event,  '• **result:**\n\n`'+code.stdout+'`\n\n• **error:**\n\n`'+code.stderr+'`', Account)
                os.remove('source.class')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» GeT LyriCZ:
@Client.on(events.NewMessage(pattern='(L|l)yrics', from_users = sudo))
async def GetLyricZ(event: events.newmessage.NewMessage.Event):
    text = event.raw_text
    if len(text) == 6 and event.is_reply:
        msg = await event.get_reply_message()
        if msg.media and 'document' in msg.media.to_dict() and 'attributes' in msg.media.document.to_dict() and 'title' in msg.media.document.attributes[0].to_dict():
            music, artist = msg.media.document.attributes[0].title, msg.media.document.attributes[0].performer
    else:
        artist, music = text[text.find(' ')+1:text.rfind('-')], text[text.rfind('-')+1:]
    res = req.get('https://api.lyrics.ovh/v1/'+artist+'/'+music, timeout=10)
    try: 
        lyr = res.json()['lyrics']
    except:
        lyr = '• **no lyrics found !**'
    await pl.send_sudo_msg(event, lyr, Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» vchat ManageR:
@Client.on(events.NewMessage(pattern = '(V|v)chat', from_users = sudo, func=lambda e:e.is_group | e.is_channel))
async def GrouPCalLMain(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 2 and cmd[0] == 'vchat':
        if cmd[1] == 'create':
            await Client(CreateGroupCallRequest(event.chat_id))
            await pl.send_sudo_msg(event, '**• voice ChaT WaS created !**', Account)
        elif cmd[1] == 'join':
            chat = await event.get_chat()
            print(chat.stringify())
            await Client(JoinGroupCallRequest(types.InputGroupCall(chat.id, chat.access_hash), 'plagueDr', params=types.DataJSON(data=js.dumps('{"enable_vp8_encoder":true}'))))
        elif cmd[1] == 'play' and event.is_reply:
            msg = await event.get_reply_message()
            if type(msg.media) is types.MessageMediaDocument and msg.media.document and msg.media.document.attributes:
                msg4show = await pl.send_sudo_msg(event, '**• wait !**', Account)
                try:
                    filename = msg.media.document.attributes[1].file_name
                except IndexError: # , 
                    formt = '.oga' if msg.media.document.mime_type == 'audio/ogg' else 'mp4' if msg.media.document.mime_type == 'video/mp4' else '.mp3' if msg.media.document.mime_type == 'audio/mpeg' else ''
                    filename = pl.create_rend_name(6) +'.'+ formt
                await Client.download_media(msg, filename)
                await group_call_factory.start_voice_chat(event,msg4show, file_name=filename)
        elif cmd[1] == 'stop':
            if group_call_factory.is_played():
                await group_call_factory.stop_voice_chat()
                await pl.send_sudo_msg(event, '**• done !**', Account)
'''
@Client.on(events.NewMessage(pattern = '(V|v)chat', from_users = sudo))
async def GrouPCalLMain(event: events.newmessage.NewMessage.Event):
    if len(event.raw_text.split()) == 2 and event.raw_text.split()[0].lower() == 'vchat':
        if event.raw_text.split()[1] == 'cr':
            await Client(CreateGroupCallRequest(event.chat_id))
            await event.edit('- Voic# ChaT WaS Creat3D !') if event.sender_id in Account else await event.reply('- Voic# ChaT WaS Creat3D !')
        elif event.raw_text.split()[1] == 'join':
            chat = await event.get_chat()
            print(chat.stringify())
            await Client(JoinGroupCallRequest(types.InputGroupCall(chat.id, chat.access_hash), 'plagueDr', params=types.DataJSON(data=js.dumps('{"enable_vp8_encoder":true}'))))
        elif event.raw_text.split()[1] == 'end': # .dumps(
            pass'''
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» QR CoD#:
@Client.on(events.NewMessage(pattern = '(Q|q)rcode', from_users = sudo))
async def QrCoD3(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 2 and cmd[0] == 'qrcode':
        if cmd[1] == 'create' and len_cmd >= 3:
            (qrcode.make(event.raw_text[14:])).save('QRCode.png')
            if event.sender_id in Account:
                await event.delete()
                await Client.send_file(event.chat_id, 'QRCode.png', caption = event.raw_text[14:])
            else:
                await Client.send_file(event.chat_id, 'QRCode.png', reply_to = event.id, caption = event.raw_text[14:])
            os.remove('QRCode.png')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 CoiN MarkeT:
@Client.on(events.NewMessage(pattern = '(C|c)oin', from_users = sudo))
async def SetCoiNManaGeR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if cmd[0] == 'coin':
        if len_cmd >= 3 and cmd[1].isdigit() and cmd[2].isdigit():
            start = int(cmd[1])
            end = int(cmd[2])
            sep = 1 if start < end else -1
            coin = pl.getCoin(loop=True)
            coin_dict = {}
            for page in range(start, end, sep):
                coin.update(page=page)
                coin_dict = pl.collection_dict(coin_dict, coin.get_dict())
            pms = pl.split_coins(coin_dict)
            for i in pms:
                await event.reply(i)
        elif len_cmd > 1:
            if cmd[1].isdigit():
                coin = pl.getCoin(page=int(cmd[1]))
                pms = pl.split_coins(coin)
                for i in pms:
                    await event.reply(i)
            else:
                searching = cmd[1]
                start_page = None
                end_page = None
                if len_cmd >= 3 and cmd[2].isdigit():
                    start_page = int(cmd[2])
                if len_cmd >= 4 and cmd[3].isdigit():
                    end_page = int(cmd[3])
                if end_page and start_page:
                    sep = 1 if start_page < end_page else -1
                    coin = pl.getCoin(loop=True)
                    coin_dict = {}
                    for page in range(start_page, end_page, sep):
                        coin.update(page=page)
                        coin_dict = pl.collection_dict(coin_dict, coin.get_dict())
                    find = coin_dict.get(searching)
                    await event.reply(f'`{find}$`') if find else await event.reply('**• not found !**')
                else:
                    coin = pl.getCoin(page=start_page)
                    find = coin.get_dict().get(searching)
                    await event.reply(f'`{find}$`') if find else await event.reply('**• not found !**')
        else:
            coin = pl.getCoin()
            pms = pl.split_coins(coin)
            for i in pms:
                await event.reply(i)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» GeT ProxY: ---- not webservice to this code .
'''
@Client.on(events.NewMessage(pattern='(P|p)roxy', from_users = sudo))
async def GetProxY(event: events.newmessage.NewMessage.Event):
    if event.raw_text.lower() == 'proxy':
        res = req.get('https://www.api.wirexteam.tk/mtproto')#('https://www.wirexteam.ga/mtproto')
        num = pl.Counter()
        try: 
            pxy = '\n'.join(list(map(lambda px:f'• [proxy {num.get_num()}]({px["proxy"]}) - **ping: {px["ping"]} ms**', res.json()['mtproto']))[:50])
        except:
            pxy = '- cannot connect 2 weservice !'
        await event.edit(pxy) if event.sender_id in Account else await event.reply(pxy)'''
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Check ManageR:
@Client.on(events.NewMessage(pattern = '(C|c)heck', from_users = sudo))
async def CheCKDIU(event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 3 and cmd[0] == 'check':
        if cmd[1] == 'username':
            try:check = f'• **Checking Username** `{cmd[2]}` **On Social Media:**\n'+'            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n'+'\n'.join(['⌬ '+i+' = '+v['stats']+ f'{"[✔️]" if v["link"] else "[✖️]"}' for i, v in req.get('https://www.wirexteam.ga/checker?username='+cmd[2]).json()['checker'].items()])
            except: check = '• **error !**'
            finally: await pl.send_sudo_msg(event, check, Account)
        elif cmd[1] == 'ip':
            try: check = f'• **Ip Information For** ( `{cmd[2]}` ):'+'\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n'+'\n'.join(['⌬ '+i+' = '+str(v) for i, v in req.get('http://ip-api.com/json/{}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,query'.format(cmd[2])).json().items()])
            except: check = '• **error !**'
            finally: await pl.send_sudo_msg(event, check, Account)
        elif cmd[1] == 'domain': 
            try:domain = whois(cmd[2]);check = f'• **Checking Domain** (`{domain.domain}`)\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n⌬ creation = {domain.creation_date}\n⌬ expiration = {domain.expiration_date}\n⌬ servers = [ {", ".join(domain.name_servers)} ]\n⌬ dns = {domain.dnssec}\n⌬ email = {domain.emails}\n⌬ country = {domain.country}\n⌬ state = {domain.state}'
            except:check = '• **error !**'
            finally:await pl.send_sudo_msg(event, check, Account)
        elif cmd[1] == 'phone':
            try:kosphone = FuckingPhone(event.raw_text[event.raw_text.find(' ', 8)+1:]);check = f'• **checking phone** (`{kosphone.national_number}`)\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n⌬ country = {geocoder.description_for_number(kosphone, "en")}\n⌬ country code = {kosphone.country_code}\n⌬ co = {carrier.name_for_number(kosphone, "en")}'
            except:check = '**• error !**'
            finally:await pl.send_sudo_msg(event, check, Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Take the system "TIME/DATE" and send it:
@Client.on(events.NewMessage(pattern='(T|t)ime', from_users = sudo, func=lambda e:e.raw_text.lower() == 'time'))
async def SeYTime(event: events.newmessage.NewMessage.Event):
    Dat3 = pl.gregorian_to_jalali(dt.today().year, dt.today().month, dt.today().day)
    await pl.send_sudo_msg(event, '• Tim3 NoW :\n'+'- time = %.2d:%.2d:%.2d'%(dt.today().hour, dt.today().minute, dt.today().second)+' | '+pl.send_weekday(dt.now().weekday())+'\n- date = '+'/'.join(map(lambda x:'%.2d'%x, Dat3))+' - '+'/'.join(map(lambda x:'%.2d'%x, [dt.today().year, dt.today().month, dt.today().day]))+'\n- Seasons = '+pl.send_seasons(Dat3[1])+' - '+pl.send_seasons(Dat3[1], 'j')+'\n- Month = '+pl.jdmonthname(Dat3[1])+' - '+dt.now().strftime("%B"), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» UsE th3 Google Translate module 4 translation !:
@Client.on(events.NewMessage(pattern = '(T|t)r', from_users = sudo, func = lambda e:e.raw_text.split()[0].lower() == 'tr'))
async def TranslatE(event: events.newmessage.NewMessage.Event):
    Tr = Translator() # 0110100100100000011011000110111101110110011001010010000001001101
    if event.is_reply and len(event.raw_text) == 5:
        msg = await event.get_reply_message()
        msg_for_tr = msg.raw_text
    else:
        msg_for_tr = event.raw_text[6:] 
    await pl.send_sudo_msg(event, Tr.translate(msg_for_tr, dest=event.raw_text[3:5]).text, Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Accounts whose Messag# donot need to be forwarded =| ! :
@Client.on(events.NewMessage(pattern = '(A|a)cdontsave', from_users = Account))
async def DonTSaveMsgInChannel(event: events.newmessage.NewMessage.Event):
    if event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if str(msg.peer_id.user_id) not in clir.lrange('DonTCare2MsG', 0, -1):
            clir.lpush('DonTCare2MsG', msg.peer_id.user_id)
    await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» JoiN In GrouP:
@Client.on(events.NewMessage(pattern = '(J|j)oin', from_users = acc_sudo))
async def joinchat(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd > 1 and cmd[1][0] == '@':
        try:
            await Client(JoinChannelRequest(cmd[1]))
            await pl.send_sudo_msg(event, '• **done, joined !**', Account)
        except:await pl.send_sudo_msg(event, '• **error !**', Account)
    elif len_cmd > 1 and pl.check_link(cmd[1], ptrn = 's'):
        link = pl.check_link(cmd[1], ptrn = 'l')
        try:
            await Client(CheckChatInviteRequest(link[link.rfind('/')+1:]))
        except: await pl.send_sudo_msg(event, '• **invalid link !**', Account)
        else:
            try:
                await Client(ImportChatInviteRequest(link[link.rfind('/')+1:]))
                await pl.send_sudo_msg(event, '• **done, joined !**', Account)
            except: await pl.send_sudo_msg(event, '• **Account is in member group !**', Account)
    else:
        try:
            await Client(JoinChannelRequest(cmd[1]))
            await pl.send_sudo_msg(event, '• **done, joined !**', Account)
        except:
            await pl.send_sudo_msg(event, '• **error !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» InFO BOT:
@Client.on(events.NewMessage(pattern = '(I|i)nfo', from_users = acc_sudo))
async def SeYInFO(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if event.raw_text.lower() == 'info': 
        await pl.send_sudo_msg(event, f'• **info plSelf** `v.{pl.botc.version}` :\n\n• **sudos :** `{len(sudo)}`\n• **PV user :** `{len(clir.lrange("plAcUserInPV",0 ,-1))}`\n• **user :** `{getpwuid(os.getuid())[0]}`\n• **used RAM:** `{int(((Process(os.getpid()).memory_full_info().rss)/1024)/1024)}MB`\n• **python3 version :** `{sys.version.split()[0]}`\n• **telethon version :** `{tver}`\n', Account)
    elif len_cmd > 1 and cmd[0] == 'info' and cmd[1] == 'pv':
        c = pl.Counter()
        await pl.send_sudo_msg(event, '• **user in pv:**\n\n'+'\n'.join(map(lambda s:f'{c.get_num()} - [{s}](tg://user?id={s})', clir.lrange('plAcUserInPV',0 ,-1))), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Send && SaV# Voice:
@Client.on(events.NewMessage(pattern = '(V|v)oice', from_users = acc_sudo))
async def SenDSaVOicE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 2 and cmd[0] == 'voice':
        if cmd[1] == 'save' and event.is_reply and len_cmd == 3:
            voice_name = cmd[2]
            if voice_name not in clir.hgetall('plVoiCESaVE').keys():
                msg = await event.get_reply_message()
                if msg.media and type(msg.media) is types.MessageMediaDocument and msg.media.document.attributes and type(msg.media.document.attributes[0]) is types.DocumentAttributeAudio and msg.media.document.attributes[0].voice:
                    voice = pl.create_rend_name(12)
                    await Client.download_media(msg.media, os.getcwd()+'/data/voice/'+voice)
                    clir.hset('plVoiCESaVE', voice_name, voice)
                    await pl.send_sudo_msg(event, f'• **done, voice name to call :** `{voice_name}`', Account)
            else:
                await pl.send_sudo_msg(event, '• **voice was already in the database !**', Account)
        elif cmd[1] == 'delete' and len_cmd == 3:
            voice_name = cmd[2]
            if voice_name in clir.hgetall('plVoiCESaVE').keys():
                os.remove(os.getcwd()+'/data/voice/'+pl.findfile(clir.hget('plVoiCESaVE', voice_name), os.getcwd()+'/data/voice/'))
                clir.hdel('plVoiCESaVE', voice_name)
                await pl.send_sudo_msg(event, f'• **done,** `{voice_name}` **removed to database !**', Account)
            else:await pl.send_sudo_msg(event, f'• **the** `{voice_name}` **not in database !**', Account)
        elif cmd[1] == 'list':
            num = pl.Counter()
            await pl.send_sudo_msg(event, '• **voice list:**\n\n'+'\n'.join(map(lambda x:f'**{num.get_num()} -** `{x}`' ,clir.hgetall('plVoiCESaVE').keys())), Account)
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
@Client.on(events.NewMessage(pattern = '(F|f)ile', from_users = acc_sudo))
async def SenDFuCKinGFilE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 2 and cmd[0] == 'file':
        if cmd[1] == 'save' and event.is_reply and len_cmd == 3:
            file_name = cmd[2]
            if file_name not in clir.hgetall('plFuCKInGFilESaVE').keys():
                msg = await event.get_reply_message()
                if msg.media:
                    await Client.send_file(pl.botc.BOT_USERNAME, msg.media, caption=f'kosfile {file_name}')
                    #clir.hset('plFuCKInGFilESaVE', file_name, pack_bot_file_id(msg.media))
                    await pl.send_sudo_msg(event, f'• **done, voice name to call :** `{file_name}`', Account)
            else:
                await pl.send_sudo_msg(event, '**• file was already in the database !**', Account)
        elif cmd[1] == 'delete' and len(cmd) == 3:
            file_name = cmd[2]
            if file_name in clir.hgetall('plFuCKInGFilESaVE').keys():
                clir.hdel('plFuCKInGFilESaVE', file_name)
                await pl.send_sudo_msg(event, f'• **done,** `{file_name}` **removed the database !**', Account)
            else:
                await pl.send_sudo_msg(event, f'• **the** `{file_name}` **not in database !**', Account)
        elif cmd[1] == 'list':
            num = pl.Counter()
            await pl.send_sudo_msg(event, '• **file list:**\n\n'+'\n'.join(map(lambda x:f'**{num.get_num()} -** `{x}`' ,clir.hgetall('plFuCKInGFilESaVE').keys())), Account)
        else:
            file_name = cmd[1]
            if file_name in clir.hgetall('plFuCKInGFilESaVE').keys():
                reply_to = ''
                if event.is_reply:
                    reply_to = event.reply_to.reply_to_msg_id
                elif event.sender_id not in Account:
                    reply_to = event.id
                await Client.send_message(pl.botc.BOT_USERNAME, f'kosfile {file_name} {event.chat_id} {reply_to}')
                if event.sender_id in Account:
                    await event.delete()
@Client.on(events.NewMessage(pattern = 'kosnanatmary', from_users=pl.botc.BOT_USERNAME)) # good pattern 
async def KosNaNatMary(event: events.newmessage.NewMessage.Event):
    if event.media:
        cmd = event.raw_text.split()
        chat_id = int(cmd[1])
        reply = None
        if pl.isexistList(cmd, 2):
            reply = int(cmd[2])
        await Client.send_file(chat_id, event.media, reply_to=reply)
    await event.delete()
@bot.on(events.NewMessage(pattern = 'kosfile', from_users=Account[0]))
async def KirToKosMary(event: events.newmessage.NewMessage.Event):
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
@Client.on(events.NewMessage(pattern = '(L|l)eft', from_users = acc_sudo))
async def leftchat(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 4 and event.is_group:
        try:
            await pl.send_sudo_msg(event, 'bye', Account)
            await Client(LeaveChannelRequest(await Client.get_input_entity(event.chat_id)))
        except: await pl.send_sudo_msg(event, '**• error !**', Account)
    elif len_cmd > 1 and pl.check_link(cmd[1], ptrn = 's'):
        link = pl.check_link(cmd[1], ptrn = 'l')
        try:
            await Client(LeaveChannelRequest(await Client.get_input_entity(link)))
            await pl.send_sudo_msg(event, '• **done, i lefted.**', Account)
        except: await pl.send_sudo_msg(event, '**• error !**', Account)
    else:
        try:
            await Client(LeaveChannelRequest(await Client.get_input_entity(event.raw_text.split()[1])))
            await pl.send_sudo_msg(event, '• **done, i lefted.**', Account)
        except: await pl.send_sudo_msg(event, '**• error !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Delet# a messag3 from SUDO:
@Client.on(events.NewMessage(pattern = '(D|d)el', from_users = sudo))
async def DeleteMessag3(event: events.newmessage.NewMessage.Event): # 0110100100100000011011000110111101110110011001010010000001101000011001010111001000100000011000100111010101110100001000000110100100100000011010000110000101110110011001010010000001110100011011110010000001100110011011110111001001100111011001010111010000100000011010000110010101110010
    if event.is_reply and event.raw_text.lower() == 'del':await Client.delete_messages(event.chat_id, event.reply_to.reply_to_msg_id);await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 MutE && UnMute --D in GrouP && PV:
@Client.on(events.NewMessage(pattern = '(M|m)ute', from_users = sudo))
async def MuteAllGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    text = event.raw_text.lower()
    chat_id = str(event.chat_id)
    if event.is_group:
        if text == 'mute all':
            if chat_id not in clir.lrange('plMuteAllGP', 0, -1):
                clir.lpush('plMuteAllGP', event.chat_id)
                await pl.send_sudo_msg(event, f'• **group** `{event.chat_id}` **has been muted !**', Account)
            else:
                await pl.send_sudo_msg(event, f'• **group** `{event.chat_id}` **has been muted before !**', Account)
        elif cmd[0] == 'mute':
            user = None
            if len_cmd == 1 and event.is_reply:
                user = await event.get_reply_message()
                user = str(user.from_id)
                # this -F code 4 telethon 1.4, not now ...
                #if not user.from_id: return
                #user = '-100{}'.format(user.from_id.channel_id) if 'channel_id' in user.from_id.to_dict() else str(user.from_id.user_id)
            elif len_cmd > 1:
                if cmd[1][0] == '@':
                    user = await Client.get_input_entity(cmd[1])
                    user = '-100{}'.format(user.channel_id) if 'channel_id' in user.to_dict() else '{}'.format(user.user_id)
                elif cmd[1].isdigit():
                    user = str(cmd[1])
                elif event.entities and 'user_id' in event.entities[0].to_dict():
                    user = str(event.entities[0].user_id)
            if user != None:
                if int(user) not in sudo:
                    if chat_id in clir.hgetall('plMut3UserInPG').keys():
                        if user not in clir.hget('plMut3UserInPG', chat_id).split():
                            pl.adduserinMuteGp2hset(clir ,'plMut3UserInPG', chat_id, user)
                            await pl.send_sudo_msg(event, f'• **user** `{user}` **has been muted !**', Account)
                        else:await pl.send_sudo_msg(event, f'• **user** `{user}` **has been muted before !**', Account)
                    else:
                        pl.adduserinMuteGp2hset(clir ,'plMut3UserInPG', chat_id, user)
                        await pl.send_sudo_msg(event, f'• **user** `{user}` **has been muted !**', Account)
                else:
                    await pl.send_sudo_msg(event, '• **user is SUDO !**', Account)
    elif text == 'mute' and event.sender_id == Account[0] and event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if msg.peer_id.user_id == Account:
            return
        if str(msg.peer_id.user_id) not in clir.lrange('plMutePVUsEr', 0, -1):
            clir.lpush('plMutePVUsEr', msg.peer_id.user_id)
            await event.edit(f'• **user** `{msg.peer_id.user_id}` **has been muted !**')
        else:
            await event.edit(f'• **user** `{msg.peer_id.user_id}` **has been muted bofore !**')
@Client.on(events.NewMessage(pattern = '(U|u)nmute', from_users = sudo))
async def UnMuteAllGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    text = event.raw_text.lower()
    chat_id = str(event.chat_id)
    if event.is_group:
        if text == 'unmute all':
            if chat_id in clir.lrange('plMuteAllGP', 0, -1): 
                clir.lrem('plMuteAllGP', 0, event.chat_id)
                await pl.send_sudo_msg(event, f'• **group** `{event.chat_id}` **it has out of muted !**', Account)
            else:
                await pl.send_sudo_msg(event, f'• **group** `{event.chat_id}` **has not been muted !**', Account)
        elif cmd[0] == 'unmute':
            user = None
            if len_cmd == 1 and event.is_reply:
                user = str((await event.get_reply_message()).from_id)
                #if not user.from_id: return
                #user = '-100{}'.format(user.from_id.channel_id) if 'channel_id' in user.from_id.to_dict() else str(user.from_id.user_id)
            elif len_cmd > 1:
                if cmd[1][0] == '@':
                    user = await Client.get_input_entity(cmd[1])
                    user = '-100{}'.format(user.channel_id) if 'channel_id' in user.to_dict() else '{}'.format(user.user_id)
                elif cmd[1].isdigit():
                    user = str(cmd[1])
                elif bool(event.entities) and 'user_id' in event.entities[0].to_dict():
                    user = str(event.entities[0].user_id)
            if user != None:
                if int(user) not in sudo:
                    if chat_id in clir.hgetall('plMut3UserInPG').keys():
                        if user in clir.hget('plMut3UserInPG', str(event.chat_id)).split():
                            pl.deluserinMuteGp2hset(clir ,'plMut3UserInPG', chat_id, user)
                            await pl.send_sudo_msg(event, f'• **user** `{user}` **has been unmuted !**', Account)
                        else:
                            await pl.send_sudo_msg(event, f'• **user** `{user}` **has no muted !**', Account)
                    else:
                        await pl.send_sudo_msg(event, f'• **user** `{user}` **has no muted !**', Account)
                else:
                    await pl.send_sudo_msg(event, '• **user is SUDO !**', Account)
    elif text == 'unmute' and event.sender_id == Account[0] and event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if msg.peer_id.user_id == Account:return
        if str(msg.peer_id.user_id) in clir.lrange('plMutePVUsEr', 0, -1):
            clir.lrem('plMutePVUsEr', 0, msg.peer_id.user_id)
            await event.edit(f'• **user** `{msg.peer_id.user_id}` **has been unmuted !**')
        else:
            await event.edit(f'• **user** `{msg.peer_id.user_id}` **has no muted !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Th Banned User IN GP:
@Client.on(events.NewMessage(pattern = '(B|b)an', from_users = sudo, func=lambda e:e.is_group))
async def BaNnedUserInGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 2:
        if cmd[1][0] == '@':
            user = await Client.get_input_entity(cmd[1])
            if 'user_id' in user.to_dict():
                await Client(EditBannedRequest(event.chat_id, user.user_id, ChatBannedRights(until_date=None, view_messages=True)))
                await pl.send_sudo_msg(event, f'• **user** `{user.user_id}` **has been Banned !**', Account)
        elif cmd[1].isdigit():
            await Client(EditBannedRequest(event.chat_id, int(cmd[1]), ChatBannedRights(until_date=None, view_messages=True)))
            await pl.send_sudo_msg(event, f'• **user** `{cmd[1]}` **has been Banned !**', Account)
        elif event.entities and 'user_id' in event.entities[0].to_dict():
            await Client(EditBannedRequest(event.chat_id, event.entities[0].user_id, ChatBannedRights(until_date=None, view_messages=True)))
            await pl.send_sudo_msg(event, f'• **user** `{event.entities[0].user_id}` **has been Banned !**', Account)
    elif event.is_reply and event.raw_text.lower() == 'ban':
        msg = await event.get_reply_message()
        user = msg.from_id.channel_id if 'channel_id' in msg.from_id.to_dict() else msg.from_id.user_id
        if user in sudo:
            await pl.send_sudo_msg(event, f'• **user** `{user}` **is SUDO !**', Account)
        else:
            try: await Client(EditBannedRequest(event.chat_id, user, ChatBannedRights(until_date=None, view_messages=True)))
            except:
                await pl.send_sudo_msg(event, '• **error !**', Account)
            else:
                await pl.send_sudo_msg(event, f'• **user** `{user}` **has been Banned !**', Account)
#   -» Th UnBanned User IN GP:
@Client.on(events.NewMessage(pattern = '(U|u)nban', from_users = sudo))
async def BaNnedUserInGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd == 2:
        if cmd[1][0] == '@':
            user = await Client.get_input_entity(cmd[1])
            if 'user_id' in user.to_dict():
                await Client.edit_permissions(event.chat_id, user.user_id, until_date=None, view_messages=True)
                await pl.send_sudo_msg(event, f'• **user** `{user.user_id}` **has been unbanned !**', Account)
        elif cmd[1].isdigit():
            await Client.edit_permissions(event.chat_id, int(cmd[1]), until_date=None, view_messages=True)
            await pl.send_sudo_msg(event, f'• **user** `{cmd[1]}` **has been unbanned !**', Account)
        elif event.entities and 'user_id' in event.entities[0].to_dict():
            await Client.edit_permissions(event.chat_id, event.entities[0].user_id, until_date=None, view_messages=True)
            await pl.send_sudo_msg(event, f'• **user** `{event.entities[0].user_id}` **has been unbanned !**', Account)
    elif event.is_reply and event.raw_text.lower() == 'unban':
        msg = await event.get_reply_message()
        user = msg.from_id.channel_id if 'channel_id' in msg.from_id.to_dict() else msg.from_id.user_id
        try: await Client.edit_permissions(event.chat_id, user, until_date=None, view_messages=True)
        except:
            await pl.send_sudo_msg(event, '• **error !**', Account)
        else:
            await pl.send_sudo_msg(event, f'• **user** `{user}` **has been unbanned !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Set ManageR: 
@Client.on(events.NewMessage(pattern = '(S|s)et', from_users = sudo))
async def SetManageR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event)
    if len_cmd >= 3 and cmd[0] == 'set':
        if cmd[1] == 'bio':
            bio = event.raw_text[event.raw_text.find(' ', 5)+1:]
            if bio == 'delete':
                clir.delete('plFuckinBio')
                await Client(UpdateProfileRequest(about = ''))
                await pl.send_sudo_msg(event, '• **done, bio was deleted !**', Account)
            else:
                if len(bio) <= 70:
                    clir.set('plFuckinBio', bio)
                    await Client(UpdateProfileRequest(about = bio))
                    await pl.send_sudo_msg(event, f'• **done, bio :** `{bio}`', Account)
        elif cmd[1] == 'username':
            username = event.raw_text[event.raw_text.find(' ', 5)+1:]
            if username == 'delete':
                await Client(UpdateUsernameRequest(''))
                await pl.send_sudo_msg(event, '• **done, username was deleted !**', Account)
            else:
                await Client(UpdateUsernameRequest(username))
                await pl.send_sudo_msg(event, f'• **done, username :** `{username}`', Account)
        elif cmd[1] == 'name':
            name = event.raw_text[event.raw_text.find(' ', 5)+1:]
            await Client(UpdateProfileRequest(first_name = name))
            await pl.send_sudo_msg(event, f'• **done, name :** `{name}`', Account)
        elif cmd[1] == 'lastname':
            lastname = event.raw_text[event.raw_text.find(' ', 5)+1:]
            if lastname == 'delete':
                await Client(UpdateProfileRequest(last_name = ''))
                await pl.send_sudo_msg(event, '• **done, lastname was deleted !**', Account)
            else:
                await Client(UpdateProfileRequest(last_name = lastname))
                await pl.send_sudo_msg(event, f'• **done, lastname :** `{lastname}`', Account)
        elif cmd[1] == 'profile':
            if cmd[2] == 'this' and event.is_reply:
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
                        await pl.send_sudo_msg(event, str(e), Account)
                    else:
                        if event.sender_id in Account:
                            await event.delete()
                        await msg.reply('• **done, profile seted !**')
                        os.remove(Fil3)
            elif cmd[2] == 'group':
                if event.is_reply:
                    msg = await event.get_reply_message()
                    if msg.media:
                        if len_cmd > 3:
                            if cmd[3][0] == '@':
                                pic_name = pl.create_rend_name(10)
                                await Client.download_media(msg.media, file=pic_name)
                                Fil3 = pl.findfile(pic_name, os.getcwd())
                                pic = await Client.upload_file(os.getcwd()+'/'+Fil3)
                                await Client(EditPhotoRequest(cmd[3][1:], pic))
                                if event.sender_id in Account:
                                    await event.delete()
                                await msg.reply('• **done, profile seted !**')
                                os.remove(Fil3)
                            elif cmd[3][0]=='-' and cmd[3][1:].isdigit():
                                pic_name = pl.create_rend_name(10)
                                await Client.download_media(msg.media, file=pic_name)
                                Fil3 = pl.findfile(pic_name, os.getcwd())
                                pic = await Client.upload_file(os.getcwd()+'/'+Fil3)
                                await Client(EditPhotoRequest(await Client.get_input_entity(int(cmd[3])), pic))
                                if event.sender_id in Account:
                                    await event.delete()
                                await msg.reply('• **done, profile seted !**')
                                os.remove(Fil3)
                        elif event.is_reply and (event.is_group or event.is_channel):
                            pic_name = pl.create_rend_name(10)
                            await Client.download_media(msg.media, file=pic_name)
                            Fil3 = pl.findfile(pic_name, os.getcwd())
                            pic = await Client.upload_file(os.getcwd()+'/'+Fil3)
                            await Client(EditPhotoRequest(event.chat_id, pic))
                            if event.sender_id in Account:
                                await event.delete()
                            await msg.reply('• **done, profile seted !**')
                            os.remove(Fil3)
            elif cmd[2] == 'delete':
                await Client(DeletePhotosRequest([(await Client.get_profile_photos('me'))[0]]))
                await pl.send_sudo_msg(event, '• **done, a profile deleted !**', Account)
            elif cmd[2] == 'deleteall':
                await Client(DeletePhotosRequest((await Client.get_profile_photos('me'))))
                await pl.send_sudo_msg(event, '• **done, all profile was deleted !**', Account)
            '''elif cmd[1] == 'randname':
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
                else: await event.edit('- The randname was already OFF') if event.sender_id in Account else await event.reply('- The randname was already OFF')'''
        elif cmd[1] == 'lasttime':
            if cmd[2] == 'on':
                if clir.get('plSetTimENow'):
                    await pl.send_sudo_msg(event, '• **lasttime was already ON !**', Account)
                else:
                    full = (await Client.get_me()).last_name or '<<<!@n@!@dlfd;f;sfldssdkskmadki!l!l>>>'
                    clir.set('plSetTimENow', full)
                    await pl.send_sudo_msg(event, '• **done, set lasttime is ON !**', Account)
            elif cmd[2] == 'off':
                get_re = clir.get('plSetTimENow')
                if get_re:
                    await Client(UpdateProfileRequest(last_name = '')) if get_re == '<<<!@n@!@dlfd;f;sfldssdkskmadki!l!l>>>' else await Client(UpdateProfileRequest(last_name = get_re))
                    clir.delete('plSetTimENow')
                    await pl.send_sudo_msg(event, '• **done, set lastime is OFF !**', Account)
                else: await pl.send_sudo_msg(event, '• **lasttime was already OFF !**', Account)
        elif cmd[1] == 'biotime':
            if cmd[2] == 'on':
                if clir.get('plBioTimENow'):
                    await pl.send_sudo_msg(event, '• **biotime was already ON !**', Account)
                else:
                    clir.set('plBioTimENow', 'KoSKoS=D')
                    await pl.send_sudo_msg(event, '• **done, biotime is ON !**', Account)
            elif cmd[2] == 'off':
                if clir.get('plBioTimENow'):
                    clir.delete('plBioTimENow')
                    await pl.send_sudo_msg(event, '• **done, biotime is OFF !**', Account)
        elif cmd[1] == 'forward':
            if cmd[2] == 'off':
                if clir.get('plForWardSendOrno'):
                    clir.delete('plForWardSendOrno')
                    await pl.send_sudo_msg(event, '• **done, forward has offline !**', Account)
                else:
                    await pl.send_sudo_msg(event, '• **forward was already offline !**', Account)
            elif cmd[2] == 'on':
                if clir.get('plForWardSendOrno'):
                    await pl.send_sudo_msg(event, '• **forward was already online !**', Account)
                else:
                    clir.set('plForWardSendOrno', 'True')
                    await pl.send_sudo_msg(event, '• **done, forward has online !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» PIN MsG : 
@Client.on(events.NewMessage(pattern = '(P|p)in', from_users = sudo, func=lambda e:e.raw_text.lower() == 'pin'))
async def PINMessaG3(event: events.newmessage.NewMessage.Event):
    if event.is_reply and event.raw_text:
        msg = await event.get_reply_message()
        await Client.pin_message(event.chat_id, msg, notify = True)
        await pl.send_sudo_msg(event, '• **message pinned !**', Account)
#   -» UNPIN MsG : 
@Client.on(events.NewMessage(pattern = '(U|u)npin', from_users = sudo, func=lambda e:e.raw_text.lower() == 'unpin'))
async def UnPINMessaG3(event: events.newmessage.NewMessage.Event):
    if event.is_group:
        msg = await Client.get_messages(event.chat_id, ids=types.InputMessagePinned())
        if msg != None:
            await Client.unpin_message(event.chat_id, msg.id)
            await event.delete() and await msg.reply('• **message unpinned !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SpeedTesT:
@Client.on(events.NewMessage(pattern = '(S|s)peedtest', from_users = sudo))
async def SpeeDTesT(event: events.newmessage.NewMessage.Event):
    if event.raw_text.lower() == 'speedtest':
        msg = await pl.send_sudo_msg(event, '• **wait !**', Account)
        FuckingTIME = dt.now()
        res = await pl.dict_speedtest()
        await msg.edit(f'• **result from `speedtest.net` after {(dt.now()-FuckingTIME).seconds}s :**\n\n**• download :** `{res["download"]:,}` **Mbps**\n**• upload :** `{res["ping"]:,}` **Mbps**\n**• ping :** `{res["ping"]}` **ms**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» PING CMD:
@Client.on(events.NewMessage(pattern = '(P|p)ing', from_users = sudo, func=lambda e:e.raw_text.lower() == 'ping'))
async def PING(event: events.newmessage.NewMessage.Event):
    TStarT = dt.now()
    kosmsg = await Client.send_message(event.chat_id, '**-- ping cmd !**')
    await pl.send_sudo_msg(event, f'• `bot is ON !` **ping {(dt.now()-TStarT).microseconds/1000} ms**', Account)
    await kosmsg.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SenD FuckinG Gam3:
@Client.on(events.NewMessage(pattern = '(G|g)ame', from_users = sudo, func=lambda e:e.raw_text.lower() == 'game'))
async def SendFGam3(event: events.newmessage.NewMessage.Event):
    result = await Client.inline_query('gamee', '', entity=event.chat_id)           
    await (rand.choice(result)).click(reply_to=event.id)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Block && UnBlock:
@Client.on(events.NewMessage(pattern = '(B|b)lock', from_users = Account, func=lambda e:e.raw_text.lower() == 'block'))
async def ThBlockEdUseR(event: events.newmessage.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if event.is_group:
            await event.edit(f'• **user** `{msg.from_id.user_id}` **has been blocked !**')
            await Client(BlockRequest(msg.from_id.user_id))
        else:
            await event.edit(f'• **user** `{msg.peer_id.user_id}` **has been blocked !**')
            await Client(BlockRequest(msg.peer_id.user_id))
#   -»
@Client.on(events.NewMessage(pattern = '(U|u)nblock', from_users = Account, func=lambda e:e.raw_text.lower() == 'unblock'))
async def ThUnBlockEdUseR(event: events.newmessage.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if event.is_group:
            await Client(UnblockRequest(msg.from_id.user_id))
            await event.edit(f'• **user** `{msg.from_id.user_id}` **has been unblocked !**')
        else:
            await Client(UnblockRequest(msg.peer_id.user_id))
            await event.edit(f'• **user** `{msg.peer_id.user_id}` **has been unblocked !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» MaiN Message Edit:
@Client.on(events.MessageEdited())
async def check__edited_massag3(event: events.MessageEdited.Event):await check_massag3(event)
@Client.on(events.MessageEdited(from_users = sudo, func=lambda e:e.raw_text))
async def MaiNMessageEdited(event: events.MessageEdited.Event):
    cmd = event.raw_text.split()[0].lower()
    if event.sender_id in Account:
        #if cmd == 'flood':await FloodSpaM(event)
        if cmd == 'wow':await GetFuckinGNuD3(event)
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
        #elif cmd == 'turn':await TurNFuckinGOff(event)
    if cmd == 'ping':await PING(event)
    elif cmd == 'code':await RuNCoD3(event)
    elif cmd == 'pin':await PINMessaG3(event)
    elif cmd == 'rmsg':await RMSG_CMD(event)
    elif cmd == 'insta':await InsTA(event)
    elif cmd == 'cal':await GeTCal(event)
    elif cmd == 'music':await FinDManageR(event)
    elif cmd == 'id':await IdProcessing(event)
    elif cmd == 'invite':await FuckinGInvalidUseR(event)
    elif cmd == 'base':await ReBaSE(event)
    elif cmd == 'morse':await ReMorsE(event)
    elif cmd == 'help':await SendHelP(event)
    elif cmd == 'lyrics':await GetLyricZ(event)
    elif cmd == 'vchat':await GrouPCalLMain(event)
    elif cmd == 'qrcode':await QrCoD3(event)
    #elif cmd == 'proxy':await GetProxY(event)
    elif cmd == 'check':await CheCKDIU(event)
    elif cmd == 'time':await SeYTime(event)
    elif cmd == 'tr':await TranslatE(event)
    elif cmd == 'del':await DeleteMessag3(event)
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
'''
@Client.on(events.NewMessage(pattern='(T|t)urn off', from_users=acc_sudo, func=lambda e:e.raw_text.lower()=='turn off'))
async def TurNFuckinGOff(event: events.newmessage.NewMessage.Event):
    await event.edit('• **bot went offline !**') if event.sender_id in Account else await event.reply('• **bot went offline !**')
    await bot.disconnect()
    await Client.disconnect()
    #insta.close()'''
# - - - - - Anti-spam settings in the group - - - - -  #
#   -» Add GrouP 2 ReDis:
@Client.on(events.NewMessage(pattern='(A|a)dd', from_users = sudo, func=lambda e: e.is_group and e.raw_text.lower() == 'add'))
async def AddGrouP(event: events.newmessage.NewMessage.Event):
    if str(event.chat_id) not in clir.hgetall('plAddGroPSettinGZ').keys():
        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps({'lock_link':False,'gp_Ch':False, 'lock_photo':False,'lock_stiker':False,'lock_gif':False,'lock_tg':False,'lock_game':False,'lock_dsh':False,'lock_voice':False,'lock_forward':False,'lock_video':False,'lock_via':False,'lock_music':False,'lock_file':False,'lock_bot':False,'lock_location':False,'lock_contact':False,'lock_caption':False,'lock_contact':False,'lock_caption':False}))
        await pl.send_sudo_msg(event, '• **group add to database !**', Account)
    else: await pl.send_sudo_msg(event, '• **group added to database before !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RemoVeD GrouP 2 ReDis:
@Client.on(events.NewMessage(pattern='(R|r)em', from_users = sudo, func=lambda e: e.is_group and e.raw_text.lower() == 'rem'))
async def RemGrouP(event: events.newmessage.NewMessage.Event):
    if str(event.chat_id) in clir.hgetall('plAddGroPSettinGZ').keys():
        clir.hdel('plAddGroPSettinGZ', str(event.chat_id))
        await pl.send_sudo_msg(event, '• **group deleted to database !**', Account)
    else:await pl.send_sudo_msg(event, '• **group deleted to database before !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» BoT H3lp:
@Client.on(events.NewMessage(pattern = '(H|h)elp', from_users = sudo, func=lambda e:e.raw_text.lower() == 'help'))
async def SendHelP(event: events.newmessage.NewMessage.Event):
    await pl.send_sudo_msg(event, pl.botc.STR_HELP_BOT, Account)
    '''
    try: 
        if event.sender_id in Account: 
            result = await Client.inline_query(botc.BOT_USERNAME, 'fuckinghelp', entity=event.chat_id)
            await result[0].click()
            await event.delete()
        else:
            result = await Client.inline_query(botc.BOT_USERNAME, 'fuckinghelp', entity=event.chat_id)
            await result[0].click(reply_to=event.id)
    except Exception as e:
        await event.edit(f'• **error :** {e}') if event.sender_id in Account else await event.reply(f'• **error :** {e}')'''
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SenD PaneL:
@Client.on(events.NewMessage(pattern = '(P|p)anel', from_users = sudo))
async def PANELAPI(event: events.newmessage.NewMessage.Event): 
    if event.is_group and event.raw_text.lower() == 'panel':
        if str(event.chat_id) in clir.hgetall('plAddGroPSettinGZ'):
            try: 
                if event.sender_id in Account: 
                    result = await Client.inline_query(pl.botc.BOT_USERNAME, 'panel', entity=event.chat_id)
                    await result[0].click()
                    await event.delete()
                else:
                    result = await Client.inline_query(pl.botc.BOT_USERNAME, 'panel', entity=event.chat_id)
                    await result[0].click(reply_to=event.id)
            except Exception as e:
                await pl.send_sudo_msg(event, f'• **error :** {e}', Account)
        else:
            await pl.send_sudo_msg(event, '• **group not in database !**', Account)
# - - - - - - - - - - ApI_BoT - - - - - - - - - - - -  #
#   -» InPrivat3:
@bot.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def Fohsh_be_user(event: events.newmessage.NewMessage.Event):
    if event.sender_id not in Account and str(event.sender_id) not in clir.lrange('plUserInApiBoT', 0, -1):
        clir.lpush('plUserInApiBoT', str(event.sender_id))
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
'''@bot.on(events.InlineQuery(pattern='fuckinghelp', users=Account))
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
    await event.answer([kos])'''
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
@bot.on(events.CallbackQuery())
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
