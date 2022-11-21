#                   [   Plague Dr.  ]
# - - - - - - - - - - -LIBRarYS- - - - - - - - - - - - #
from telethon import TelegramClient, events, Button, types, __version__ as tver, errors
from telethon.tl.functions.messages import ImportChatInviteRequest, CheckChatInviteRequest # , HideChatJoinRequestRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest, EditBannedRequest, InviteToChannelRequest, EditPhotoRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import InputPeerChannel, InputPeerUser, ChatBannedRights
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.phone import CreateGroupCallRequest, JoinGroupCallRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.utils import pack_bot_file_id
from googletrans import Translator
from shazamio import Shazam
from pytgcalls.exceptions import NoActiveGroupCall
import qrcode
from phonenumbers import geocoder, carrier, parse as FuckingPhone
from whois import whois
from pwd import getpwuid
import scripts as pl
import os, sys, subprocess
import json as js
import logging, time
import random as rand
from datetime import datetime as dt
from captcha.image import ImageCaptcha
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests as req
import psutil, git
from pydub import AudioSegment
from scripts.utils.Logger import Logging
# - - - - - - - - - - - ValueS - - - - - - - - - - - - #
Account = pl.Conf.acc_sudo
acc_sudo = pl.Conf.main_sudo
sudo = pl.Conf.sudoS
# phone = '+989360145942'
pl.check_data_dir()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
logger = Logging("UserBot", logging.DEBUG)
print(f'{pl.Color.BLACK}\n{pl.Color.BG_RED}\t# {" [   Plague Dr.  ] ":-^46} #{pl.Color.RESET}\n')
bot = TelegramClient(pl.Conf.SESSION_DIR + pl.Conf.SESSION_API_NAME, pl.Conf.API_ID, pl.Conf.API_HASH).start(bot_token=pl.Conf.BOT_TOKEN)
logger.info("Api Bot is Running...")
clir = pl.bot_redis(pl.Conf.REDIS_NUMBER)
logger.info("Redis is Running...")
# insta = pl.instaBot(pl.Conf.INSTAGRAM[0], pl.Conf.INSTAGRAM[1], pl.Conf.INSTAGRAM[2], pl.Conf.SESSION_DIR[:-1])
Client = TelegramClient(pl.Conf.SESSION_DIR + pl.Conf.SESSION_AC_NAME, pl.Conf.API_ID, pl.Conf.API_HASH, base_logger=logger)
Client.start()
logger.info("UserBot is Running...")
group_call_factory = pl.VchatCall(Client)
print('\t- PlSelf Started successfully!', pl.Color.RESET)
print(f' {pl.Color.RED}----{pl.Color.RESET}    {pl.Color.BG_CYAN}{pl.Color.BOLD} Connected as {pl.Conf.SESSION_AC_NAME} ! {pl.Color.RESET}    {pl.Color.RED}----{pl.Color.RESET}')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» CheckING MsG SerVic3 In GP:
@Client.on(events.ChatAction())
async def GetMsGServic3InGP(event: events.chataction.ChatAction.Event):
    chat_id, user_id = event.action_message.peer_id.channel_id, event.action_message.from_id.user_id
    chat_id_str = '-100'+str(chat_id)
    type_message = type(event.action_message.action)
    
    if chat_id_str in clir.lrange('plMuteAllGP', 0, -1) or (chat_id_str in list(clir.hgetall('plAddGroPSettinGZ').keys()) \
        and js.loads(clir.hget('plAddGroPSettinGZ', chat_id_str))['service']):
        await Client.delete_messages(chat_id, event.action_message.id)
    
    if chat_id_str in clir.hgetall('AnTITABCiE').keys():
        if type_message == types.MessageActionChatJoinedByLink:
            await Client.edit_permissions(chat_id, user_id, 
                view_messages = True,
                send_messages = False,
            )
            image = ImageCaptcha(width = 180, height = 90)
            data = pl.create_rend_name(4) 
            image.generate(data) 
            image.write(data, data+'.png')
            result = await Client.inline_query(pl.Conf.BOT_USERNAME, f'CkTabchi {data} {user_id}', entity=chat_id)
            await result[0].click() 
        elif type_message == types.MessageActionChatAddUser:
            for users in event.action_message.action.users:
                await Client.edit_permissions(chat_id, users, 
                view_messages = True,
                send_messages = False,
                )
                image = ImageCaptcha(width = 180, height = 90)
                data = pl.create_rend_name(4) 
                image.generate(data) 
                image.write(data, data+'.png')
                result = await Client.inline_query(pl.Conf.BOT_USERNAME, f'CkTabchi {data} {users}', entity=chat_id)
                await result[0].click() 
    #if (chat_id in list(clir.hgetall('plAddGroPSettinGZ').keys()) and js.loads(clir.hget('plAddGroPSettinGZ', chat_id))['service']) and'action' in event.message.to_dict() and type_message is types.MessageActionChatAddUser:
    #    pass
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» CheckING ALL Message:
@Client.on(events.MessageEdited())
@Client.on(events.NewMessage())
async def check_massag3(event: events.newmessage.NewMessage.Event or events.messageedited.MessageEdited.Event):
    if event.is_private and event.sender_id != Account[0] and event.media and event.media.ttl_seconds:
        file_name = await event.download_media('data/photos')
        await Client.send_file(pl.Conf.CHANNEL_FOR_FWD, file_name)
    if event.sender_id in sudo:
        if event.raw_text and ((type_event := type(event)) is events.newmessage.NewMessage.Event or (type_event is events.messageedited.MessageEdited.Event and not event.reactions)):
            cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)[0]
            if event.sender_id in acc_sudo and not await pl.switch(cmd[0], {
                'wow': GetFuckinGNuD3,
                'reload': RestartProGraM,
                'acdontsave': DonTSaveMsgInChannel,
                'join': joinchat,
                'info': SeYInFO,
                'voice': SenDSaVOicE,
                'file': SenDFuCKinGFilE,
                'left': leftchat,
                'set': SetManageR,
                'turn': TurNFuckinGOff,
            }, pl.empty_async)(event):pass
            else:
                await pl.switch(cmd[0], {
                    'rmsg': RMSG_CMD,
                    'insta': InsTA,
                    'cal': GeTCal,
                    'id': IdProcessing,
                    'invite': FuckinGInvalidUseR,
                    'music': FinDManageR,
                    'antitabchi': SeTAntITabCHI,
                    'base': ReBaSE,
                    'morse': ReMorsE,
                    'code': RuNCoD3,
                    'lyrics': GetLyricZ,
                    'vc': GrouPCalLMain,
                    'qrcode': QrCoD3,
                    'coin': SetCoiNManaGeR,
                    'check': CheCKDIU,
                    'time': SeYTime,
                    'tr': TranslatE,
                    'del': DeleteMessag3,
                    'mute': MuteAllGP,
                    'unmute': UnMuteAllGP,
                    'ban': BaNnedUserInGP,
                    'unban': BaNnedUserInGP,
                    'pin': PINMessaG3,
                    'unpin': UnPINMessaG3,
                    'speedtest': SpeeDTesT,
                    'ping': PING,
                    'game': SendFGam3,
                    'block': ThBlockEdUseR,
                    'unblock': ThUnBlockEdUseR,
                    'add': AddGrouP,
                    'rem': RemGrouP,
                    'help': SendHelP,
                    'panel': PANELAPI,
                    'lock': LockGpManager,
                    'unlock': LockGpManager,
                }, pl.empty_async)(event)
    elif event.is_group:
        chat_id = str(event.chat_id)
        usr = str(event.sender_id)
        if chat_id in clir.lrange('plMuteAllGP', 0, -1) or(clir.hgetall('plMut3UserInPG').get(chat_id) and usr in clir.hget('plMut3UserInPG', chat_id).split()):
            await event.delete()
        elif chat_id in clir.hgetall('plAddGroPSettinGZ').keys():
            database = js.loads(clir.hget('plAddGroPSettinGZ', chat_id))
            if database['link'] and pl.check_msg_link(event.raw_text):
                await event.delete()
            elif  database['forward'] and event.fwd_from:
                await event.delete()
            elif database['unknown'] and event.sender_id and event.sender_id < 0:
                await event.delete()
            elif  database['bot']:pass # not idea 4 this ...
    elif event.is_private:
        sender_id = str(event.sender_id)
        get_user = None if clir.get('acdontsave:'+sender_id+':pl') == None else int(clir.get('acdontsave:'+sender_id+':pl'))
        if sender_id in clir.lrange('plMutePVUsEr', 0, -1):
            if not await pl.userisbot(clir, event):
                if get_user == None:
                    if clir.get('plForWardSendOrno'):
                        clir.setex('acdontsave:'+sender_id+':pl', 86400, 1)
                        await Client.forward_messages(pl.Conf.CHANNEL_FOR_FWD, event.message)
                else:
                    if get_user < 15:
                        if clir.get('plForWardSendOrno'):
                            clir.setex('acdontsave:'+sender_id+':pl', 86400, get_user+1)
                            await Client.forward_messages(pl.Conf.CHANNEL_FOR_FWD, event.message)
            await event.delete()
        elif sender_id not in clir.lrange('DonTCare2MsG', 0, -1) and not await pl.userisbot(clir, event):
            if get_user == None:
                if clir.get('plForWardSendOrno'):
                    clir.setex('acdontsave:'+sender_id+':pl', 86400, 1)
                    await Client.forward_messages(pl.Conf.CHANNEL_FOR_FWD, event.message)
            else:
                if get_user < 15:
                    if clir.get('plForWardSendOrno'):
                        clir.setex('acdontsave:'+sender_id+':pl', 86400, get_user+1)
                        await Client.forward_messages(pl.Conf.CHANNEL_FOR_FWD, event.message)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RMSG MSG:
async def RMSG_CMD(event:  events.newmessage.NewMessage.Event):
    try:
        msg = int(event.raw_text[5:]) 
    except:
        await pl.send_sudo_msg(event, '› **error !**', Account)
    else:
        _4sendmsg = await pl.send_sudo_msg(event, '› **wait !**', Account)
        c = 1 if event.sender_id in Account else 0
        async for message in Client.iter_messages(event.chat_id, msg+1):
            if c < 2:
                c += 1
                continue
            try:
                await message.delete()
            except Exception as er:
                await pl.send_sudo_msg(_4sendmsg, f'› **error !** `{er}`', Account)
                break
        await _4sendmsg.edit(f'› **done,** `{msg}` **msg has been deleted !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» InsTa:
async def InsTA(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX, False)
    if len_cmd == 3 and cmd[0].lower() == 'insta':
        if cmd[1] == 'post': 
            insta = pl.instaBot(pl.Conf.INSTAGRAM[0],pl.Conf.INSTAGRAM[1], pl.Conf.INSTAGRAM[2], pl.Conf.SESSION_DIR[:-1])
            file_name = await insta.down_post(cmd[2])
            Files = file_name.get('file')
            post = file_name.get('post')
            if len(file_name) >= 1:
                try:
                    await Client.send_file(event.chat_id, Files, reply_to=event.id, caption = f'› **username :** `{post.owner_username}`\n› **like :** `{post.likes}`\n› **Comments :** `{post.comments}`')
                except:
                    for f in Files:
                        await Client.send_file(event.chat_id, f, reply_to=event.id, caption = f'› **username :** `{post.owner_username}`\n› **like :** `{post.likes}`\n› **Comments :** `{post.comments}`')
            pl.instaBot.remove_dir('insta')
            del insta
        elif cmd[1] == 'profile':
            insta = pl.instaBot(pl.Conf.INSTAGRAM[0],pl.Conf.INSTAGRAM[1], pl.Conf.INSTAGRAM[2], pl.Conf.SESSION_DIR[:-1])
            files = await insta.down_profile(cmd[2])
            profile = files.get('profile')
            fucking_file = files.get('file')
            await Client.send_file(event.chat_id, fucking_file, reply_to=event.id, caption = f'› **name :** `{profile.full_name}`\n› **bio :** `{profile.biography}`\n› **followers :** `{profile.followers:,}`')
            pl.instaBot.remove_dir(profile.username)
            del insta
        elif cmd[1] == 'story':
            insta = pl.instaBot(pl.Conf.INSTAGRAM[0],pl.Conf.INSTAGRAM[1], pl.Conf.INSTAGRAM[2], pl.Conf.SESSION_DIR[:-1])
            files = await insta.down_story(cmd[2])
            profile = files.get('profile')
            Files = files.get('file')
            try:
                await Client.send_file(event.chat_id, Files, reply_to=event.id)
            except:
                    for f in Files:
                        await Client.send_file(event.chat_id, f, reply_to=event.id)
            pl.instaBot.remove_dir(profile.username)
            del insta
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Calculator:
async def GeTCal(event: events.newmessage.NewMessage.Event):
    try: await pl.send_sudo_msg(event, f'{eval(event.raw_text[4:]):,}', Account)
    except: await pl.send_sudo_msg(event, '› **error !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Flood SpaM:
''' nothing 4 now ...
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
async def IdProcessing(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd == 2:
        if cmd[1][0] == '@':
            chat = await Client.get_input_entity(cmd[1])
            if 'channel_id' in chat.to_dict():
                await pl.send_sudo_msg(event, f'`-100{chat.channel_id}`', Account)
            else:
                await pl.send_sudo_msg(event, f'`{chat.user_id}`', Account)
        elif cmd[1] == 'chat':
            if event.is_group:await pl.send_sudo_msg(event, f'`{event.chat_id}`', Account)
        elif cmd[1][0] == '-':
            chat = await Client.get_entity(int(cmd[1]))
            if chat.username == None:
                await pl.send_sudo_msg(event, '**› not username !**', Account)
            else:
                await pl.send_sudo_msg(event, f'@{chat.username}', Account)
        elif cmd[1][0].isdigit():
            await pl.send_sudo_msg(event, f'[{cmd[1]}](tg://user?id={cmd[1]})', Account)
        elif event.entities and getattr(event.entities[0], 'user_id', None):
            await pl.send_sudo_msg(event, f'`{event.entities[0].user_id}`', Account)
    elif event.is_private and cmd[0] == 'id':
        if event.is_reply:
            msg = await event.get_reply_message()
            await pl.send_sudo_msg(event, f'`{msg.peer_id.user_id}`', Account)
        else:
            await pl.send_sudo_msg(event, f'`{event.sender_id}`', Account)
    elif (event.is_group or event.is_channel) and cmd[0] == 'id':
        if event.is_reply:
            msg = await event.get_reply_message()
            user = getattr(msg.from_id, 'user_id', None) or f'-100{getattr(msg.from_id, "channel_id", None)}'
            #if user:
            await pl.send_sudo_msg(event, f'`{user}`', Account)
            #else: await pl.send_sudo_msg(event, f'`{msg.from_id.user_id}`', Account)
        else: await pl.send_sudo_msg(event, f'`{event.sender_id}`', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» invalid UseR:
async def FuckinGInvalidUseR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd == 2 and cmd[0] == 'invite':
        try:
            user = await Client.get_input_entity(cmd[1])
            chat = await Client.get_input_entity(event.chat_id)
            await Client(InviteToChannelRequest(InputPeerChannel(chat.channel_id, chat.access_hash),[InputPeerUser(user.user_id, user.access_hash)]))
        except Exception as e:
            await pl.send_sudo_msg(event, '› **error** : '+str(e), Account)
        else:
            await pl.send_sudo_msg(event, f'› **user** `{user.user_id}` **added to gorup !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» FucK Off =| :
async def GetFuckinGNuD3(event: events.newmessage.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if msg.media:
            file_name = await msg.download_media('data/photos')
            await Client.send_file(pl.Conf.CHANNEL_FOR_FWD, file_name)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» MusiC ManageR:
async def FinDManageR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if event.is_reply:
        msg = await event.get_reply_message()
        if msg.media and type(msg.media) is types.MessageMediaDocument and msg.media.document and msg.media.document.attributes:
            if len_cmd >= 2:
                if cmd[1] == 'find' and msg.media.document.mime_type in ['audio/ogg', 'video/mp4', 'audio/mpeg']:
                    filename = await msg.download_media()
                    shazam = Shazam()
                    if event.sender_id in Account:await event.delete()
                    _sending_msg = await msg.reply('› **wait !**')
                    out = await shazam.recognize_song(filename)
                    if out.get('track'):
                        try:album = out["track"]["sections"][0]["metadata"][0]["text"]
                        except IndexError:album = 'None'
                        msg4send = f'**› music info:**\n**› name:** `{out["track"]["title"]}`\n**› artist:** `{out["track"]["subtitle"]}`\n**› genre:** `{out.get("track", {}).get("genres", {}).get("primary")}`\n**› album:** `{album}`'
                    else:
                        msg4send = '› **not found !**'
                    await _sending_msg.edit(msg4send)
                    os.remove(filename)
                elif cmd[1] == 'info':
                    await pl.send_sudo_msg(event, f'**› music info:**\n**› title:** `{msg.media.document.attributes[0].title}`\n**› performer:** `{msg.media.document.attributes[0].performer}`\n**› filename:** `{msg.media.document.attributes[1].file_name}`', Account)
                elif cmd[1] == 'cut':
                    if len_cmd == 3:
                        if cmd[2].isdigit():
                            music_end = int(cmd[2])
                            filename = await msg.download_media()
                            sound = AudioSegment.from_file(filename)
                            sound[0 : music_end * 1000].export(filename)
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                            os.remove(filename)
                    elif len_cmd == 4:
                        if cmd[2].isdigit() and cmd[3].isdigit():
                            music_start = int(cmd[2])
                            music_end = int(cmd[3])
                            filename = await msg.download_media()
                            sound = AudioSegment.from_file(filename)
                            sound[music_start * 1000 : music_end * 1000].export(filename)
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                            os.remove(filename)
                    else:
                        filename = await msg.download_media()
                        sound = AudioSegment.from_file(filename)
                        sound[0 : 120000].export(filename)
                        if event.sender_id in Account: await event.delete()
                        await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                        os.remove(filename)
                elif cmd[1] == 'video' and msg.media.document.mime_type == 'video/mp4':
                    if len_cmd == 3:
                        if cmd[2].isdigit():
                            music_end = int(cmd[2])
                            video_name = await msg.download_media()
                            filename = video_name[:video_name.rfind('.')]+'.mp3'
                            sound = AudioSegment.from_file(video_name)
                            sound[0: music_end * 1000].export(filename, format='mp3')
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                            os.remove(filename)
                            os.remove(video_name)
                    elif len_cmd == 4:
                        if cmd[2].isdigit() and cmd[3].isdigit():
                            music_start = int(cmd[2])
                            music_end = int(cmd[3])
                            video_name = await msg.download_media()
                            filename = video_name[:video_name.rfind('.')]+'.mp3'
                            sound = AudioSegment.from_file(video_name)
                            sound[music_start * 1000: music_end * 1000].export(filename, format='mp3')
                            if event.sender_id in Account: await event.delete()
                            await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                            os.remove(filename)
                            os.remove(video_name)
                    else:
                        video_name = await msg.download_media()
                        filename = video_name[:video_name.rfind('.')]+'.mp3'
                        sound = AudioSegment.from_file(video_name)
                        sound.export(filename, format='mp3')
                        if event.sender_id in Account: await event.delete()
                        await Client.send_file(event.chat_id, filename, reply_to=msg.id)
                        os.remove(filename)
                        os.remove(video_name)
                elif cmd[1] == 'voice': # soon | never ... :|
                    pass # :|
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» AnTI TabCHI - CaptchA: 
async def SeTAntITabCHI(event):  
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    chat_id = str(event.chat_id)
    if event.is_group and len_cmd == 2 and cmd[0] == 'antitabchi':
        if cmd[1] == 'on': # 'AnTITABCiE'
            if chat_id in clir.hgetall('AnTITABCiE').keys():
                await pl.send_sudo_msg(event, '**› anti tabchi was active !**', Account)
            else:
                clir.hset('AnTITABCiE', chat_id, js.dumps([]))
                await pl.send_sudo_msg(event, '**› done, anti tabchi is active !**', Account)
        elif cmd[1] == 'off':
            if chat_id in clir.hgetall('AnTITABCiE').keys():
                clir.hdel('AnTITABCiE', chat_id)
                await pl.send_sudo_msg(event, '**› done, anti tabchi service cleared !**', Account)
            else:
                await pl.send_sudo_msg(event, '**› anti tabchi is not active !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» BaS#:
async def ReBaSE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 3 and cmd[0] == 'base' and cmd[1].isdigit():
        await pl.send_sudo_msg(event, pl.Base(event.raw_text[event.raw_text.find(' ', 5)+1:], int(cmd[1])).result(), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  # 
#   -» MorS#:
async def ReMorsE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 2 and cmd[0]== 'morse':
        await pl.send_sudo_msg(event, ''.join([pl.switch(morse, pl.CoDMORsE, ' ')+' ' for morse in event.raw_text[6:]]), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» ReStarT Th3 ProGraM:
async def RestartProGraM(event: events.newmessage.NewMessage.Event):
    await pl.send_sudo_msg(event, '› **bot reloaded !**', Account)
    os.execl(sys.executable, sys.executable, *sys.argv)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RuN CoD#:
async def RuNCoD3(event: events.newmessage.NewMessage.Event):
    cmds, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 2 and cmds[0] == 'code':
        cmd = cmds[1]
        if cmd == 'help':
            await pl.send_sudo_msg(event, '› **cmds :**\n`py3`\n`py2`\n`php`\n`cpp`\n`c`\n`lua`\n`js`\n`java`', Account)
        elif cmd == 'cpp':
            file = 'data/code/'+'source.cpp'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            try:s = subprocess.run(['g++', '-std=c++17', file], capture_output=True, text=True, timeout=5)
            except subprocess.TimeoutExpired: await pl.send_sudo_msg(event, '**› timeout error !**', Account)
            else:
                if s.stderr:await pl.send_sudo_msg(event, '› **error:**\n\n`'+s.stderr+'`', Account)
                else:
                    try:code = subprocess.run(['./a.out'], capture_output=True, text=True, timeout=5)
                    except subprocess.TimeoutExpired: await pl.send_sudo_msg(event, '**› timeout error !**', Account)
                    else:await pl.send_sudo_msg(event, '› **result:**\n\n`'+code.stdout+'`', Account)
                    finally:os.remove('a.out')
        elif cmd == 'program':
            try:await pl.myexec(event.raw_text[event.raw_text.find('\n')+1:], event, Client);await pl.send_sudo_msg(event, '› **done !**', Account)
            except Exception as e:await pl.send_sudo_msg(event, str(e), Account)
        elif cmd == 'c':
            file = 'data/code/'+'source.c' 
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            try:s = subprocess.run(['gcc', file, '-o', 'a.out'], capture_output=True, text=True, timeout=5)
            except subprocess.TimeoutExpired: await pl.send_sudo_msg(event, '**› timeout error !**', Account)
            else:
                if s.stderr:await pl.send_sudo_msg(event, '› **error:**\n\n`'+s.stderr+'`', Account)
                else:
                    try:code = subprocess.run(['./a.out'], capture_output=True, text=True, timeout=5)
                    except subprocess.TimeoutExpired: await pl.send_sudo_msg(event, '**› timeout error !**', Account)
                    else:await pl.send_sudo_msg(event, '› **result:**\n\n`'+code.stdout+'`', Account)
                    finally:os.remove('a.out')
        elif cmd == 'java':
            file = 'data/code/'+'source.java'
            pl.edit_source_run(event.raw_text[event.raw_text.find('\n')+1:], file)
            try:s = subprocess.run(['javac', file], capture_output=True, text=True, timeout=5)
            except subprocess.TimeoutExpired: await pl.send_sudo_msg(event, '**› timeout error !**', Account)
            else:
                if s.stderr:await pl.send_sudo_msg(event, '› **error:**\n\n`'+s.stderr+'`', Account)
                else:
                    os.system('cp data/code/source.class '+os.getcwd())
                    os.remove('data/code/'+'source.class')
                    try:code = subprocess.run(['java', 'source'], capture_output=True, text=True, timeout=5)
                    except subprocess.TimeoutExpired: await pl.send_sudo_msg(event, '**› timeout error !**', Account)
                    else:await pl.send_sudo_msg(event, '› **error:**\n\n`'+code.stderr+'`' if code.stderr else '› **result:**\n\n`'+code.stdout+'`', Account)
                    finally:os.remove('source.class')
        else:
            await pl.run_interpreter_code(
                subprocess.run,
                {'lua':'data/code/source.lua', 'py3':'data/code/source.py', 'py2':'data/code/source.py', 'php':'data/code/source.php', 'js':'data/code/source.js', 'javascript':'data/code/source.js','node':'data/code/source.js', 'nodejs':'data/code/source.js'}.get(cmd),
                {'lua':'lua', 'py3':'python3', 'py2':'python2', 'php':'php', 'js':'node', 'javascript':'node', 'node':'node', 'nodejs':'node'}.get(cmd),
                event.raw_text[event.raw_text.find('\n')+1:],
                subprocess.TimeoutExpired,
                event,
                Account
            )
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» GeT LyriCZ:
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
        lyr = '› **no lyrics found !**'
    await pl.send_sudo_msg(event, lyr, Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» vchat ManageR:

download_progresses = {}

async def vc_progress(current, total, message, chat_id):
    if chat_id not in download_progresses.keys():
        download_progresses[chat_id] = time.time() - 5
    if time.time() - download_progresses[chat_id] > 5:
        try:
            await message.edit(f"**• Downloading:** `{current * 100 / total:.1f}`%")
        except:
            pass
        download_progresses[chat_id] = time.time()

async def GrouPCalLMain(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd == 1:
        await pl.send_sudo_msg(event,
                               f'**Command :** `{pl.Conf.COMMAND_PREFIX}vc`\n\n**✘  Intro :** `Manage voice chat in group.`\n\n**✘  Usage :** \n\t`{pl.Conf.COMMAND_PREFIX}vc start`\n\t`{pl.Conf.COMMAND_PREFIX}vc stop`\n\t`{pl.Conf.COMMAND_PREFIX}vc join`\n\t`{pl.Conf.COMMAND_PREFIX}vc play <reply to audio>`\n\t`{pl.Conf.COMMAND_PREFIX}vc radio`',
                               Account)
        return

    if len_cmd == 2:
        if cmd[1] == 'start':
            try:
                await Client(CreateGroupCallRequest(event.chat_id))
            except errors.rpcbaseerrors.BadRequestError as e:
                print(e)
                await pl.send_sudo_msg(event, '**• voice chat ending, please request again !**', Account)
            else:
                await pl.send_sudo_msg(event, '**• voice chat was created !**', Account)
        elif cmd[1] == 'join':
            chat = await event.get_chat()
            await Client(
                JoinGroupCallRequest(types.InputGroupCall(int(chat.id), int(chat.access_hash)),
                                     await Client.get_entity('me'),
                                     params=types.DataJSON(data=js.dumps('{"enable_vp8_encoder":true}'))))
        elif cmd[1] == 'play' and event.is_reply:

            msg = await event.get_reply_message()
            if type(msg.media) is types.MessageMediaDocument and msg.media.document and msg.media.document.attributes:
                if event.chat.call_active:
                    msg4show = await pl.send_sudo_msg(event, '**• wait !**', Account)
                    filename = await Client.download_media(msg,
                                                           progress_callback=lambda c, t: vc_progress(c, t, msg4show,
                                                                                                      event.chat_id))
                    try:
                        await group_call_factory.vc_play_local(event, filename, msg4show)
                        del download_progresses[event.chat_id]
                        return
                    except NoActiveGroupCall:
                        pass

                await pl.send_sudo_msg(event,
                                       '**• voice chat not found !\n\nstart voice chat using command "`.vc start`"**',
                                       Account)

        elif cmd[1] == 'stop':
            msg4show = await pl.send_sudo_msg(event, '**• Wait...**', Account)
            await group_call_factory.vc_stop(event.chat_id)
            if event.chat.call_active:
                try:
                    await group_call_factory.vchat.leave_group_call(event.chat_id)
                except:
                    pass
            await msg4show.edit('**• Voice Chat stopped successfully**')

        elif cmd[1] == 'radio':
            result = await Client.inline_query(pl.Conf.BOT_USERNAME, 'radiopanel', entity=event.chat_id)
            await result[0].click()
            try:
                await event.delete()
            except:
                pass

        elif cmd[1] == 'pause':
            if event.chat.call_active:
                vcall = await group_call_factory.vchat.get_call(event.chat_id)
                if vcall.is_playing:
                    await group_call_factory.vchat.pause_stream(event.chat_id)
                    await pl.send_sudo_msg(event, '**• The stream has been successfully paused**', Account)
                else:
                    await pl.send_sudo_msg(event, '**• There is no audio playing !**', Account)
            else:
                await pl.send_sudo_msg(event,
                                       '**• voice chat not found !\n\nstart voice chat using command "`.vc start`"**',
                                       Account)

        elif cmd[1] == 'resume':
            if event.chat.call_active:
                vcall = await group_call_factory.vchat.get_call(event.chat_id)
                if vcall.is_playing:
                    await pl.send_sudo_msg(event, '**• Stream already playing!**', Account)
                else:
                    await group_call_factory.vchat.resume_stream(event.chat_id)
                    await pl.send_sudo_msg(event, '**• The stream has been successfully resumed**', Account)
            else:
                await pl.send_sudo_msg(event,
                                       '**• voice chat not found !\n\nstart voice chat using command "`.vc start`"**',
                                       Account)


@bot.on(events.InlineQuery(pattern="radiopanel", users=Account))
async def radioPanel(event: events.InlineQuery.Event):
    builder = event.builder
    result = builder.article(
        title="Radio Panel",
        text="**Welcome to Radio Panel**\n\nChoose from the following options:\n\n‌",
        buttons=[
            [Button.inline("Radio Stations 🎙", data="radio.stations")],
            [Button.inline("Radio Settings ⚙️", data="radio.settings")],
            [Button.inline("Close", data="radio.close")],
        ],
        description="Radio Panel",
    )
    await event.answer([result])


@bot.on(events.InlineQuery(pattern="radio.stream.load.", users=Account))
async def radioStreamLoad(event: events.InlineQuery.Event):
    builder = event.builder
    query = event.text[18:]

    _stream_title = pl.get_playing_stream_title(query)
    result = builder.article(
        title="Radio Stream",
        text=f'**• [Radio]({query}) started !**\n\n'
             f'**Currently playing**: __{_stream_title}__',
        buttons=[
            [Button.inline("Stop", data="radio.stream.stop")],
            [Button.inline("Close", data="radio.close")],
        ],
        description="Radio Stream",
    )
    await event.answer([result])
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» QR CoD#:
async def QrCoD3(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 2 and cmd[0] == 'qrcode':
        if cmd[1] == 'create' and len_cmd >= 3:
            try:(qrcode.make(event.raw_text[14:])).save('QRCode.png')
            except qrcode.exceptions.DataOverflowError:await pl.send_sudo_msg(event, '**› qrcode size is large !**', Account)
            else:
                if event.sender_id in Account:
                    await event.delete()
                    await Client.send_file(event.chat_id, 'QRCode.png', caption = event.raw_text[14:])
                else:
                    await Client.send_file(event.chat_id, 'QRCode.png', reply_to = event.id, caption = event.raw_text[14:])
                os.remove('QRCode.png')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 CoiN MarkeT:
async def SetCoiNManaGeR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
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
                    await event.reply(f'`{find}$`') if find else await event.reply('**› not found !**')
                else:
                    coin = pl.getCoin(page=start_page)
                    find = coin.get_dict().get(searching)
                    await event.reply(f'`{find}$`') if find else await event.reply('**› not found !**')
        else:
            coin = pl.getCoin()
            pms = pl.split_coins(coin)
            for i in pms:
                await event.reply(i)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» GeT ProxY: ---- not webservice to this code .
'''
async def GetProxY(event: events.newmessage.NewMessage.Event):
    if event.raw_text.lower() == 'proxy':
        res = req.get('https://www.api.wirexteam.tk/mtproto')#('https://www.wirexteam.ga/mtproto')
        num = pl.Counter()
        try: 
            pxy = '\n'.join(list(map(lambda px:f'› [proxy {num.get_num()}]({px["proxy"]}) - **ping: {px["ping"]} ms**', res.json()['mtproto']))[:50])
        except:
            pxy = '- cannot connect 2 weservice !'
        await event.edit(pxy) if event.sender_id in Account else await event.reply(pxy)'''
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Check ManageR:
async def CheCKDIU(event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 3 and cmd[0] == 'check':
        if False: #cmd[1] == 'username': # need to check ... later !
            try:check = f'› **Checking Username** `{cmd[2]}` **On Social Media:**\n'+'            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n'+'\n'.join(['⌬ '+i+' = '+v['stats']+ f'{"[✔️]" if v["link"] else "[✖️]"}' for i, v in req.get('https://www.wirexteam.ga/checker?username='+cmd[2], timeout=10).json()['checker'].items()])
            except: check = '› **error !**'
            finally: await pl.send_sudo_msg(event, check, Account)
        elif cmd[1] == 'ip':
            try: check = f'› **Ip Information For** ( `{cmd[2]}` ):'+'\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n'+'\n'.join(['⌬ '+i+' = '+str(v) for i, v in req.get('http://ip-api.com/json/{}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,query'.format(cmd[2]), timeout=10).json().items()])
            except: check = '› **error !**'
            finally: await pl.send_sudo_msg(event, check, Account)
        elif cmd[1] == 'domain': 
            try:domain = whois(cmd[2]);check = f'› **Checking Domain** (`{domain.domain}`)\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n⌬ creation = {domain.creation_date}\n⌬ expiration = {domain.expiration_date}\n⌬ servers = [ {", ".join(domain.name_servers)} ]\n⌬ dns = {domain.dnssec}\n⌬ email = {domain.emails}\n⌬ country = {domain.country}\n⌬ state = {domain.state}'
            except:check = '› **error !**'
            finally:await pl.send_sudo_msg(event, check, Account)
        elif cmd[1] == 'phone':
            try:kosphone = FuckingPhone(event.raw_text[event.raw_text.find(' ', 8)+1:]);check = f'› **checking phone** (`{kosphone.national_number}`)\n            ⋰⋰⋰⋰⋱⋱⋱⋱⋰⋰⋰⋰⋱⋱⋱⋱\n⌬ country = {geocoder.description_for_number(kosphone, "en")}\n⌬ country code = {kosphone.country_code}\n⌬ co = {carrier.name_for_number(kosphone, "en")}'
            except:check = '**› error !**'
            finally:await pl.send_sudo_msg(event, check, Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Take the system "TIME/DATE" and send it:
async def SeYTime(event: events.newmessage.NewMessage.Event):
    Dat3 = pl.gregorian_to_jalali(dt.today().year, dt.today().month, dt.today().day)
    await pl.send_sudo_msg(event, '› Tim3 NoW :\n'+'- time = %.2d:%.2d:%.2d'%(dt.today().hour, dt.today().minute, dt.today().second)+' | '+pl.send_weekday(dt.now().weekday())+'\n- date = '+'/'.join(map(lambda x:'%.2d'%x, Dat3))+' - '+'/'.join(map(lambda x:'%.2d'%x, [dt.today().year, dt.today().month, dt.today().day]))+'\n- Seasons = '+pl.send_seasons(Dat3[1])+' - '+pl.send_seasons(Dat3[1], 'j')+'\n- Month = '+pl.jdmonthname(Dat3[1])+' - '+dt.now().strftime("%B"), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» UsE th3 Google Translate module 4 translation !:
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
async def DonTSaveMsgInChannel(event: events.newmessage.NewMessage.Event):
    if event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        user_id = f'{getattr(msg.from_id, "user_id", "")}'
        if user_id and user_id not in clir.lrange('DonTCare2MsG', 0, -1):
            clir.lpush('DonTCare2MsG', msg.peer_id.user_id)
    await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» JoiN In GrouP:
async def joinchat(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX, False)
    if len_cmd > 1 and cmd[1][0] == '@':
        try:
            await Client(JoinChannelRequest(cmd[1]))
            await pl.send_sudo_msg(event, '› **done, joined !**', Account)
        except:await pl.send_sudo_msg(event, '› **error !**', Account)
    elif len_cmd > 1 and pl.check_link(cmd[1], ptrn = 's'):
        link = pl.check_link(cmd[1], ptrn = 'l')
        try:
            await Client(CheckChatInviteRequest(link[link.rfind('/')+1:]))
        except: await pl.send_sudo_msg(event, '› **invalid link !**', Account)
        else:
            try:
                await Client(ImportChatInviteRequest(link[link.rfind('/')+1:]))
                await pl.send_sudo_msg(event, '› **done, joined !**', Account)
            except Exception as er: await pl.send_sudo_msg(event, f'›** error: {er}!**', Account)
    else:
        try:
            await Client(JoinChannelRequest(cmd[1]))
            await pl.send_sudo_msg(event, '› **done, joined !**', Account)
        except:
            await pl.send_sudo_msg(event, '› **error !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» InFO BOT:
async def SeYInFO(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if event.raw_text.lower() == 'info':
        repo = git.Repo(search_parent_directories=True)
        message = f'› **info plSelf** `v.{pl.Conf.version}` :\n\n› **sudos :** `{len(sudo)}`\n› **PV user :** `{len(clir.lrange("plAcUserInPV",0 ,-1))}`\n› **user :** `{getpwuid(os.getuid())[0]}`\n› **used RAM:** `{int(((psutil.Process(os.getpid()).memory_full_info().rss)/1024)/1024)}/{"%.3f"%(((psutil.virtual_memory().total)/1024)/1024)}MB`\n› **process:** `{os.getpid()}` **-** `{os.getppid()}`\n› **python3 version :** `{sys.version.split()[0]}`\n› **telethon version :** `{tver}`\n› **os:** `{subprocess.check_output(["lsb_release","-is"]).decode("utf-8").lower().strip(chr(10))}`\n› **git:** `{repo.remotes.origin.url}`\n› **HEAD: {len(list(repo.iter_commits()))} -** `{repo.head.commit.message}`'
        if filename := clir.get('plSetMyFuckingLogo'):
            await Client.send_file(event.chat_id, filename, caption=message, reply_to=event.id)
        else:
            await pl.send_sudo_msg(event, message, Account)
    elif len_cmd > 1 and cmd[0] == 'info' and cmd[1] == 'pv':
        c = pl.Counter()
        await pl.send_sudo_msg(event, '› **user in pv:**\n\n'+'\n'.join(map(lambda s:f'{c.get_num()} - [{s}](tg://user?id={s})', clir.lrange('plAcUserInPV',0 ,-1))), Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Send && SaV# Voice:
async def SenDSaVOicE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 2 and cmd[0] == 'voice':
        if cmd[1] == 'play' and event.is_reply:
            msg = await event.get_reply_message()
            if msg.media and getattr(msg.media.document, 'attributes', None) and type(msg.media.document.attributes[0]) is types.DocumentAttributeAudio and msg.media.document.attributes[0].voice:
                file = await msg.download_media()
                try:txt = pl.voice_to_str(AudioSegment, file)
                except:
                    await pl.send_sudo_msg(event, '**› voice is empty, or it is not persian !**', Account)
                    os.remove(file)
                else:await pl.send_sudo_msg(event, f'{txt}' or '**› is empty !**', Account)
        elif cmd[1] == 'save' and event.is_reply and len_cmd == 3:
            voice_name = cmd[2]
            if voice_name not in clir.hgetall('plVoiCESaVE').keys():
                msg = await event.get_reply_message()
                if msg.media and type(msg.media) is types.MessageMediaDocument and msg.media.document.attributes and type(msg.media.document.attributes[0]) is types.DocumentAttributeAudio and msg.media.document.attributes[0].voice:
                    voice = await msg.download_media('data/voice')
                    clir.hset('plVoiCESaVE', voice_name, voice)
                    await pl.send_sudo_msg(event, f'› **done, voice name to call :** `{voice_name}`', Account)
            else:
                await pl.send_sudo_msg(event, '› **voice was already in the database !**', Account)
        elif cmd[1] == 'delete' and len_cmd == 3:
            voice_name = cmd[2]
            if voice_name in clir.hgetall('plVoiCESaVE').keys():
                os.remove(clir.hget('plVoiCESaVE', voice_name))
                clir.hdel('plVoiCESaVE', voice_name)
                await pl.send_sudo_msg(event, f'› **done,** `{voice_name}` **removed to database !**', Account)
            else:await pl.send_sudo_msg(event, f'› **the** `{voice_name}` **not in database !**', Account)
        elif cmd[1] == 'list':
            num = pl.Counter()
            await pl.send_sudo_msg(event, '› **voice list:**\n\n'+'\n'.join(map(lambda x:f'**{num.get_num()} -** `{x}`' ,clir.hgetall('plVoiCESaVE').keys())), Account)
        else:
            voice_name = cmd[1]
            if voice_name in clir.hgetall('plVoiCESaVE').keys():
                await event.delete()
                if event.is_reply:
                    msg = await event.get_reply_message()
                    await Client.send_file(event.chat_id, clir.hget('plVoiCESaVE', voice_name), reply_to=msg.id)
                else:
                    await Client.send_file(event.chat_id, clir.hget('plVoiCESaVE', voice_name))
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» FilE ManageR:
async def SenDFuCKinGFilE(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 2 and cmd[0] == 'file':
        if cmd[1] == 'save' and event.is_reply and len_cmd == 3:
            file_name = cmd[2]
            if file_name not in clir.hgetall('plFuCKInGFilESaVE').keys():
                msg = await event.get_reply_message()
                if msg.media:
                    await Client.send_file(pl.Conf.BOT_USERNAME, msg.media, caption=f'kosfile {file_name}')
                    #clir.hset('plFuCKInGFilESaVE', file_name, pack_bot_file_id(msg.media))
                    await pl.send_sudo_msg(event, f'› **done, voice name to call :** `{file_name}`', Account)
            else:
                await pl.send_sudo_msg(event, '**› file was already in the database !**', Account)
        elif cmd[1] == 'delete' and len(cmd) == 3:
            file_name = cmd[2]
            if file_name in clir.hgetall('plFuCKInGFilESaVE').keys():
                clir.hdel('plFuCKInGFilESaVE', file_name)
                await pl.send_sudo_msg(event, f'› **done,** `{file_name}` **removed the database !**', Account)
            else:
                await pl.send_sudo_msg(event, f'› **the** `{file_name}` **not in database !**', Account)
        elif cmd[1] == 'list':
            num = pl.Counter()
            await pl.send_sudo_msg(event, '› **file list:**\n\n'+'\n'.join(map(lambda x:f'**{num.get_num()} -** `{x}`' ,clir.hgetall('plFuCKInGFilESaVE').keys())), Account)
        else:
            file_name = cmd[1]
            if file_name in clir.hgetall('plFuCKInGFilESaVE').keys():
                reply_to = ''
                if event.is_reply:
                    reply_to = event.reply_to.reply_to_msg_id
                elif event.sender_id not in Account:
                    reply_to = event.id
                await Client.send_message(pl.Conf.BOT_USERNAME, f'kosfile {file_name} {event.chat_id} {reply_to}')
                if event.sender_id in Account:
                    await event.delete()
@Client.on(events.NewMessage(pattern = 'kosnanatmary', from_users=pl.Conf.BOT_USERNAME)) # good pattern 
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
async def leftchat(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX, False)
    if event.raw_text.lower() == 'left' and event.is_group:
        try:
            await pl.send_sudo_msg(event, 'bye', Account)
            await Client(LeaveChannelRequest(await Client.get_input_entity(event.chat_id)))
        except Exception as er: await pl.send_sudo_msg(event, f'**› error: {er}**', Account)
    elif len_cmd > 1 and pl.check_link(cmd[1], ptrn = 's'):
        link = pl.check_link(cmd[1], ptrn = 'l')
        try:
            await Client(LeaveChannelRequest(await Client.get_input_entity(link)))
            await pl.send_sudo_msg(event, '› **done, i lefted.**', Account)
        except Exception as er: await pl.send_sudo_msg(event, f'**› error: {er}**', Account)
    else:
        try:
            await Client(LeaveChannelRequest(await Client.get_input_entity(event.raw_text.split()[1])))
            await pl.send_sudo_msg(event, '› **done, i lefted.**', Account)
        except Exception as er: await pl.send_sudo_msg(event, f'**› error: {er}**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Lock && UnLock ManageR:
async def LockGpManager(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd > 1:
        database = clir.hget('plAddGroPSettinGZ', str(event.chat_id))
        if database:
            database = js.loads(database)
            if cmd[1] == 'settings':
                await pl.send_sudo_msg(event, '\n'.join(map(lambda k: f'**›** `{k[0]}` **=> [{"✔️" if k[1] else "✖️"}]**', database.items())), Account)
            elif cmd[0] == 'lock':
                if (key := database.get(cmd[1], None)) != None:
                    if key:
                        await pl.send_sudo_msg(event, f'**› {cmd[1]} is already locked !**', Account)
                    else:
                        await pl.setup_data(database, cmd[1], clir,js, event,pl.empty_async)
                        await pl.send_sudo_msg(event, f'**› done, {cmd[1]} was locked !**', Account)
            else:
                if (key := database.get(cmd[1], None)) != None:
                    if key:
                        await pl.setup_data(database, cmd[1], clir, js, event, pl.empty_async)
                        await pl.send_sudo_msg(event, f'**› done, {cmd[1]} is unlocked !**', Account)
                    else:
                        await pl.send_sudo_msg(event, f'**› {cmd[1]} is already unlocked !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Delet# a messag3 from SUDO:
async def DeleteMessag3(event: events.newmessage.NewMessage.Event): # 0110100100100000011011000110111101110110011001010010000001101000011001010111001000100000011000100111010101110100001000000110100100100000011010000110000101110110011001010010000001110100011011110010000001100110011011110111001001100111011001010111010000100000011010000110010101110010
    if event.is_reply and event.raw_text.lower() == 'del':await Client.delete_messages(event.chat_id, event.reply_to.reply_to_msg_id);await event.delete()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 MutE && UnMute --D in GrouP && PV:
async def MuteAllGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    text = event.raw_text.lower()
    chat_id = str(event.chat_id)
    if event.is_group:
        if text == 'mute all':
            if chat_id not in clir.lrange('plMuteAllGP', 0, -1):
                clir.lpush('plMuteAllGP', event.chat_id)
                await pl.send_sudo_msg(event, f'› **group** `{event.chat_id}` **has been muted !**', Account)
            else:
                await pl.send_sudo_msg(event, f'› **group** `{event.chat_id}` **has been muted before !**', Account)
        elif cmd[0] == 'mute':
            user = None
            if len_cmd == 1 and event.is_reply:
                user = await event.get_reply_message()
                user = f'{getattr(user.from_id, "user_id", "")}' or f'-100{getattr(user.from_id, "channel_id", None)}'
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
                            await pl.send_sudo_msg(event, f'› **user** `{user}` **has been muted !**', Account)
                        else:await pl.send_sudo_msg(event, f'› **user** `{user}` **has been muted before !**', Account)
                    else:
                        pl.adduserinMuteGp2hset(clir ,'plMut3UserInPG', chat_id, user)
                        await pl.send_sudo_msg(event, f'› **user** `{user}` **has been muted !**', Account)
                else:
                    await pl.send_sudo_msg(event, '› **user is SUDO !**', Account)
    elif text == 'mute' and event.sender_id == Account[0] and event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        user = f'{getattr(msg.from_id, "user_id", "")}' or f'-100{getattr(msg.from_id, "channel_id", None)}'
        if int(user) in Account:
            return
        if user not in clir.lrange('plMutePVUsEr', 0, -1):
            clir.lpush('plMutePVUsEr', user)
            await event.edit(f'› **user** `{user}` **has been muted !**')
        else:
            await event.edit(f'› **user** `{user}` **has been muted bofore !**')
async def UnMuteAllGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    text = event.raw_text.lower()
    chat_id = str(event.chat_id)
    if event.is_group:
        if text == 'unmute all':
            if chat_id in clir.lrange('plMuteAllGP', 0, -1): 
                clir.lrem('plMuteAllGP', 0, event.chat_id)
                await pl.send_sudo_msg(event, f'› **group** `{event.chat_id}` **it has out of muted !**', Account)
            else:
                await pl.send_sudo_msg(event, f'› **group** `{event.chat_id}` **has not been muted !**', Account)
        elif cmd[0] == 'unmute':
            user = None
            if len_cmd == 1 and event.is_reply:
                msg = await event.get_reply_message()
                user = f'{getattr(msg.from_id, "user_id", "")}' or f'-100{getattr(msg.from_id, "channel_id", None)}'
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
                            await pl.send_sudo_msg(event, f'› **user** `{user}` **has been unmuted !**', Account)
                        else:
                            await pl.send_sudo_msg(event, f'› **user** `{user}` **has no muted !**', Account)
                    else:
                        await pl.send_sudo_msg(event, f'› **user** `{user}` **has no muted !**', Account)
                else:
                    await pl.send_sudo_msg(event, '› **user is SUDO !**', Account)
    elif text == 'unmute' and event.sender_id == Account[0] and event.is_private and event.is_reply:
        msg = await event.get_reply_message()
        if msg.peer_id.user_id == Account:return
        if str(msg.peer_id.user_id) in clir.lrange('plMutePVUsEr', 0, -1):
            clir.lrem('plMutePVUsEr', 0, msg.peer_id.user_id)
            await event.edit(f'› **user** `{msg.peer_id.user_id}` **has been unmuted !**')
        else:
            await event.edit(f'› **user** `{msg.peer_id.user_id}` **has no muted !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Th Banned User IN GP:
async def BaNnedUserInGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd == 2:
        if cmd[1][0] == '@':
            user = await Client.get_input_entity(cmd[1])
            if 'user_id' in user.to_dict():
                await Client(EditBannedRequest(event.chat_id, user.user_id, ChatBannedRights(until_date=None, view_messages=True)))
                await pl.send_sudo_msg(event, f'› **user** `{user.user_id}` **has been Banned !**', Account)
        elif cmd[1].isdigit():
            await Client(EditBannedRequest(event.chat_id, int(cmd[1]), ChatBannedRights(until_date=None, view_messages=True)))
            await pl.send_sudo_msg(event, f'› **user** `{cmd[1]}` **has been Banned !**', Account)
        elif event.entities and 'user_id' in event.entities[0].to_dict():
            await Client(EditBannedRequest(event.chat_id, event.entities[0].user_id, ChatBannedRights(until_date=None, view_messages=True)))
            await pl.send_sudo_msg(event, f'› **user** `{event.entities[0].user_id}` **has been Banned !**', Account)
    elif event.is_reply and event.raw_text.lower() == 'ban':
        msg = await event.get_reply_message()
        user = getattr(msg.from_id, 'user_id', None)
        if not user:
            await pl.send_sudo_msg(event, f'**› user id not found !**', Account)
        elif user in sudo:
            await pl.send_sudo_msg(event, f'› **user** `{user}` **is SUDO !**', Account)
        else:
            try: await Client(EditBannedRequest(event.chat_id, user, ChatBannedRights(until_date=None, view_messages=True)))
            except:
                await pl.send_sudo_msg(event, '› **error !**', Account)
            else:
                await pl.send_sudo_msg(event, f'› **user** `{user}` **has been Banned !**', Account)
#   -» Th UnBanned User IN GP:
async def BaNnedUserInGP(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd == 2:
        if cmd[1][0] == '@':
            user = await Client.get_input_entity(cmd[1])
            if 'user_id' in user.to_dict():
                await Client.edit_permissions(event.chat_id, user.user_id, until_date=None, view_messages=True)
                await pl.send_sudo_msg(event, f'› **user** `{user.user_id}` **has been unbanned !**', Account)
        elif cmd[1].isdigit():
            await Client.edit_permissions(event.chat_id, int(cmd[1]), until_date=None, view_messages=True)
            await pl.send_sudo_msg(event, f'› **user** `{cmd[1]}` **has been unbanned !**', Account)
        elif event.entities and 'user_id' in event.entities[0].to_dict():
            await Client.edit_permissions(event.chat_id, event.entities[0].user_id, until_date=None, view_messages=True)
            await pl.send_sudo_msg(event, f'› **user** `{event.entities[0].user_id}` **has been unbanned !**', Account)
    elif event.is_reply and event.raw_text.lower() == 'unban':
        msg = await event.get_reply_message()
        user = getattr(msg.from_id, 'user_id', None)
        try: await Client.edit_permissions(event.chat_id, user, until_date=None, view_messages=True)
        except:
            await pl.send_sudo_msg(event, '› **error !**', Account)
        else:
            await pl.send_sudo_msg(event, f'› **user** `{user}` **has been unbanned !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» Set ManageR: 
async def SetManageR(event: events.newmessage.NewMessage.Event):
    cmd, len_cmd = pl.get_cmds(event, pl.Conf.COMMAND_PREFIX)
    if len_cmd >= 3 and cmd[0] == 'set':
        try:
            if cmd[1] == 'bio':
                bio = event.raw_text[event.raw_text.find(' ', 5)+1:]
                if bio == 'delete':
                    clir.delete('plFuckinBio')
                    await Client(UpdateProfileRequest(about = ''))
                    await pl.send_sudo_msg(event, '› **done, bio was deleted !**', Account)
                else:
                    if len(bio) <= 70:
                        clir.set('plFuckinBio', bio)
                        await Client(UpdateProfileRequest(about = bio))
                        await pl.send_sudo_msg(event, f'› **done, bio :** `{bio}`', Account)
            elif cmd[1] == 'logo':
                if cmd[2] == 'this' and event.is_reply:
                    msg = await event.get_reply_message()
                    if msg.media and type(msg.media) in [types.MessageMediaPhoto]:
                        file_name = await msg.download_media('data/temp')
                        clir.set('plSetMyFuckingLogo', file_name)
                        await pl.send_sudo_msg(event, '› **done, logo seted !**', Account)
                elif cmd[2] == 'delete':
                    if filename := clir.get('plSetMyFuckingLogo'):
                        os.remove(filename)
                        clir.delete('plSetMyFuckingLogo')
                        await pl.send_sudo_msg(event, '› **done, logo deleted !**', Account)
                    else:
                        await pl.send_sudo_msg(event, '› ** logo not found !**', Account)
            elif cmd[1] == 'username':
                username = event.raw_text[event.raw_text.find(' ', 5)+1:]
                if username == 'delete':
                    await Client(UpdateUsernameRequest(''))
                    await pl.send_sudo_msg(event, '› **done, username was deleted !**', Account)
                else:
                    await Client(UpdateUsernameRequest(username))
                    await pl.send_sudo_msg(event, f'› **done, username :** `{username}`', Account)
            elif cmd[1] == 'name':
                name = event.raw_text[event.raw_text.find(' ', 5)+1:]
                await Client(UpdateProfileRequest(first_name = name))
                await pl.send_sudo_msg(event, f'› **done, name :** `{name}`', Account)
            elif cmd[1] == 'lastname':
                lastname = event.raw_text[event.raw_text.find(' ', 5)+1:]
                if lastname == 'delete':
                    await Client(UpdateProfileRequest(last_name = ''))
                    await pl.send_sudo_msg(event, '› **done, lastname was deleted !**', Account)
                else:
                    await Client(UpdateProfileRequest(last_name = lastname))
                    await pl.send_sudo_msg(event, f'› **done, lastname :** `{lastname}`', Account)
            elif cmd[1] == 'profile':
                if cmd[2] == 'this' and event.is_reply:
                    msg = await event.get_reply_message()
                    if msg.media:
                        pic_name= await msg.download_media()
                        pic = await Client.upload_file(pic_name)
                        try:
                            if pic_name.endswith('.mp4'):
                                await Client(UploadProfilePhotoRequest(video=pic))
                            else:
                                await Client(UploadProfilePhotoRequest(file=pic))
                        except Exception as e:
                            await pl.send_sudo_msg(event, str(e), Account)
                        else:
                            if event.sender_id in Account: await event.delete()
                            await msg.reply('› **done, profile seted !**')
                        finally:os.remove(pic_name)
                elif cmd[2] == 'group':
                    if event.is_reply:
                        msg = await event.get_reply_message()
                        if msg.media:
                            if len_cmd > 3:
                                if cmd[3][0] == '@':
                                    pic_name = await msg.download_media()
                                    pic = await Client.upload_file(pic_name)
                                    await Client(EditPhotoRequest(cmd[3][1:], pic))
                                    if event.sender_id in Account:await event.delete()
                                    await msg.reply('› **done, profile seted !**')
                                    os.remove(pic_name)
                                elif cmd[3][0]=='-' and cmd[3][1:].isdigit():
                                    pic_name = await msg.download_media()
                                    pic = await Client.upload_file(pic_name)
                                    await Client(EditPhotoRequest(await Client.get_input_entity(int(cmd[3])), pic))
                                    if event.sender_id in Account:await event.delete()
                                    await msg.reply('› **done, profile seted !**')
                                    os.remove(pic_name)
                            elif event.is_reply and (event.is_group or event.is_channel):
                                pic_name = await msg.download_media()
                                pic = await Client.upload_file(pic_name)
                                await Client(EditPhotoRequest(event.chat_id, pic))
                                if event.sender_id in Account:await event.delete()
                                await msg.reply('› **done, profile seted !**')
                                os.remove(pic_name)
                elif cmd[2] == 'delete':
                    await Client(DeletePhotosRequest([(await Client.get_profile_photos('me'))[0]]))
                    await pl.send_sudo_msg(event, '› **done, a profile deleted !**', Account)
                elif cmd[2] == 'deleteall':
                    await Client(DeletePhotosRequest((await Client.get_profile_photos('me'))))
                    await pl.send_sudo_msg(event, '› **done, all profile was deleted !**', Account)
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
                        await pl.send_sudo_msg(event, '› **lasttime was already ON !**', Account)
                    else:
                        full = (await Client.get_me()).last_name or '<<<!@n@!@dlfd;f;sfldssdkskmadki!l!l>>>'
                        clir.set('plSetTimENow', full)
                        await pl.send_sudo_msg(event, '› **done, set lasttime is ON !**', Account)
                elif cmd[2] == 'off':
                    get_re = clir.get('plSetTimENow')
                    if get_re:
                        await Client(UpdateProfileRequest(last_name = '')) if get_re == '<<<!@n@!@dlfd;f;sfldssdkskmadki!l!l>>>' else await Client(UpdateProfileRequest(last_name = get_re))
                        clir.delete('plSetTimENow')
                        await pl.send_sudo_msg(event, '› **done, set lastime is OFF !**', Account)
                    else: await pl.send_sudo_msg(event, '› **lasttime was already OFF !**', Account)
            elif cmd[1] == 'biotime':
                if cmd[2] == 'on':
                    if clir.get('plBioTimENow'):
                        await pl.send_sudo_msg(event, '› **biotime was already ON !**', Account)
                    else:
                        clir.set('plBioTimENow', 'KoSKoS=D')
                        await pl.send_sudo_msg(event, '› **done, biotime is ON !**', Account)
                elif cmd[2] == 'off':
                    if clir.get('plBioTimENow'):
                        clir.delete('plBioTimENow')
                        await pl.send_sudo_msg(event, '› **done, biotime is OFF !**', Account)
            elif cmd[1] == 'forward':
                if cmd[2] == 'off':
                    if clir.get('plForWardSendOrno'):
                        clir.delete('plForWardSendOrno')
                        await pl.send_sudo_msg(event, '› **done, forward has offline !**', Account)
                    else:
                        await pl.send_sudo_msg(event, '› **forward was already offline !**', Account)
                elif cmd[2] == 'on':
                    if clir.get('plForWardSendOrno'):
                        await pl.send_sudo_msg(event, '› **forward was already online !**', Account)
                    else:
                        clir.set('plForWardSendOrno', 'True')
                        await pl.send_sudo_msg(event, '› **done, forward has online !**', Account)
        except Exception as er:
            await pl.send_sudo_msg(event, f'**› error: {er}**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» PIN MsG : 
async def PINMessaG3(event: events.newmessage.NewMessage.Event):
    if event.is_reply and event.raw_text:
        msg = await event.get_reply_message()
        await Client.pin_message(event.chat_id, msg, notify = True)
        await pl.send_sudo_msg(event, '› **message pinned !**', Account)
#   -» UNPIN MsG : 
async def UnPINMessaG3(event: events.newmessage.NewMessage.Event):
    if event.is_group:
        msg = await Client.get_messages(event.chat_id, ids=types.InputMessagePinned())
        if msg != None:
            await Client.unpin_message(event.chat_id, msg.id)
            await event.delete() and await msg.reply('› **message unpinned !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SpeedTesT:
async def SpeeDTesT(event: events.newmessage.NewMessage.Event):
    if event.raw_text.lower() == 'speedtest':
        msg = await pl.send_sudo_msg(event, '› **wait !**', Account)
        FuckingTIME = dt.now()
        res = await pl.dict_speedtest()
        await msg.edit(f'› **result from `speedtest.net` after {(dt.now()-FuckingTIME).seconds}s :**\n\n**› download :** `{res["download"]:,}` **Mbps**\n**› upload :** `{res["ping"]:,}` **Mbps**\n**› ping :** `{res["ping"]}` **ms**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» PING CMD:
async def PING(event: events.newmessage.NewMessage.Event):
    TStarT = dt.now()
    kosmsg = await pl.send_sudo_msg(event, '› `bot is ON !`', Account)
    await kosmsg.edit(f'› `bot is ON !` **ping {(dt.now()-TStarT).microseconds/1000} ms**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SenD FuckinG Gam3:
async def SendFGam3(event: events.newmessage.NewMessage.Event):
    result = await Client.inline_query('gamee', '', entity=event.chat_id)
    await (rand.choice(result)).click(reply_to=event.id)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» 2 Block && UnBlock:
async def ThBlockEdUseR(event: events.newmessage.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if event.is_group:
            user = getattr(msg.from_id, 'user_id', None)
            if not user: await pl.send_sudo_msg(event, f'**› user id not found !**', Account)
            else:
                await Client(BlockRequest(user))
                await event.edit(f'› **user** `{user}` **has been blocked !**')
        else:
            await event.edit(f'› **user** `{user}` **has been blocked !**')
            await Client(BlockRequest(msg.peer_id.user_id))
#   -»
async def ThUnBlockEdUseR(event: events.newmessage.NewMessage.Event):
    if event.is_reply:
        msg = await event.get_reply_message()
        if event.is_group:
            user = getattr(msg.from_id, 'user_id', None)
            if not user: await pl.send_sudo_msg(event, f'**› user id not found !**', Account)
            else:
                await Client(UnblockRequest(user))
                await event.edit(f'› **user** `{user}` **has been unblocked !**')
        else:
            await Client(UnblockRequest(msg.peer_id.user_id))
            await event.edit(f'› **user** `{msg.peer_id.user_id}` **has been unblocked !**')
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» There is nothing to say here:
async def TurNFuckinGOff(event: events.newmessage.NewMessage.Event):
    await event.edit('› **bot went offline !**') if event.sender_id in Account else await event.reply('› **bot went offline !**')
    os.system(f'kill {os.getppid()}')
# - - - - - Anti-spam settings in the group - - - - -  #
#   -» Add GrouP 2 ReDis:
async def AddGrouP(event: events.newmessage.NewMessage.Event):
    if str(event.chat_id) not in clir.hgetall('plAddGroPSettinGZ').keys():
        clir.hset('plAddGroPSettinGZ', str(event.chat_id), js.dumps(pl.BOT_GROUP_DATABASE))
        await pl.send_sudo_msg(event, '› **group add to database !**', Account)
    else: await pl.send_sudo_msg(event, '› **group added to database before !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» RemoVeD GrouP 2 ReDis:
async def RemGrouP(event: events.newmessage.NewMessage.Event):
    if str(event.chat_id) in clir.hgetall('plAddGroPSettinGZ').keys():
        clir.hdel('plAddGroPSettinGZ', str(event.chat_id))
        await pl.send_sudo_msg(event, '› **group deleted to database !**', Account)
    else:await pl.send_sudo_msg(event, '› **group deleted to database before !**', Account)
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» BoT H3lp:
async def SendHelP(event: events.newmessage.NewMessage.Event):
    await pl.send_sudo_msg(event, pl.Conf.STR_HELP_BOT, Account)
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
        await event.edit(f'› **error :** {e}') if event.sender_id in Account else await event.reply(f'› **error :** {e}')'''
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#   -» SenD PaneL:
async def PANELAPI(event: events.newmessage.NewMessage.Event): 
    if event.is_group and event.raw_text.lower() == 'panel':
        if str(event.chat_id) in clir.hgetall('plAddGroPSettinGZ'):
            try: 
                if event.sender_id in Account: 
                    result = await Client.inline_query(pl.Conf.BOT_USERNAME, 'panel', entity=event.chat_id)
                    await result[0].click()
                    await event.delete()
                else:
                    result = await Client.inline_query(pl.Conf.BOT_USERNAME, 'panel', entity=event.chat_id)
                    await result[0].click(reply_to=event.id)
            except Exception as e:
                await pl.send_sudo_msg(event, f'› **error :** {e}', Account)
        else:
            await pl.send_sudo_msg(event, '› **group not in database !**', Account)
# - - - - - - - - - - ApI_BoT - - - - - - - - - - - -  #
#   -» InPrivat3:
@bot.on(events.NewMessage(pattern='/start'))
async def bot_starting_user(event: events.newmessage.NewMessage.Event):
    if event.sender_id in sudo:
        await event.reply('**› hello sudo !**')
    elif event.is_private and (usr := str(event.sender_id)) not in clir.lrange('plUserInApiBoT', 0, -1):
        clir.lpush('plUserInApiBoT', usr)
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
                Button.inline('°› ‌Ban ›°', data='tban'+user),
                Button.inline('°› UnResT ›°', data='tunrt'+user),
            ),]
        builder = event.builder
        result = await builder.photo(pic_name+'.png',text=f'با سلام [کاربر](tg://user?id={user}) گرامی:\nلطفا کد کپچای درست را انتخاب کنید.', buttons=buttons)
        await event.answer([result])
        os.remove(pic_name+'.png')
#   -»
'''@bot.on(events.InlineQuery(pattern='fuckinghelp', users=Account))
async def SenDFucKinGHelP(event: events.InlineQuery.Event):
    buttons = [
        (
            Button.inline('°› AnTi SpaM GP ›°', data='fuckinghelp1'),
        ),
        (
            Button.inline('°› KosSher FUN ›°', data='fuckinghelp2'),
            Button.inline('°› Account HELP ›°', data='fuckinghelp3')
        ),
        (Button.inline("°› [ ExiT ] ›°", data="exitpl"),)
    ]
    builder = event.builder
    kos = await builder.article(title='fuckinghelp', text=f'**°› WlC 2 Th source help page! | pl-self v.{pl.version} ›°**', buttons=buttons)
    await event.answer([kos])'''
#   -» 
@bot.on(events.InlineQuery(pattern="panel", users = Account)) 
async def gpanel_1(event: events.InlineQuery.Event):
    if event.query.user_id in Account:
        buttons = [
            (
                Button.inline(f"°› Settings ›°", data="gpl1"),
            ),
            (
                Button.inline("°› List Mute GP ›°", data="list_mute_gp"),
                Button.inline("°› List Mute PV ›°", data="list_mute_pv"),
            ),
            (Button.inline("°› [ ExiT ] ›°", data="exitpl"),)
        ]
        builder = event.builder
        result = await builder.article(title='panel', text='°› Welcome to the management panel of Group!\nPlease choose: ›°', buttons=buttons)
        await event.answer([result])
async def panel_1(event: events.InlineQuery.Event):
    database = clir.hget('plAddGroPSettinGZ', str(event.chat_id))
    if database == None:return
    else:database = js.loads(database)
    buttons = [
        (
            Button.inline(f"°› Link [{'✔️' if database['link'] else '✖️'}] ›°", data="link"),
            Button.inline(f"°› Photo [{'✔️' if database['photo'] else '✖️'}] ›°", data="photo"),
        ),
        (
            Button.inline(f"°› Stiker [{'✔️' if database['stiker'] else '✖️'}] ›°", data="stiker"),
            Button.inline(f"°› Gif [{'✔️' if database['gif'] else '✖️'}] ›°", data="gif"),
        ),
        (
            Button.inline(f"°› service [{'✔️' if database['service'] else '✖️'}] ›°", data="service"),
            Button.inline(f"°› Game [{'✔️' if database['game'] else '✖️'}] ›°", data="game"),
        ),
        (
            Button.inline(f"°› button [{'✔️' if database['button'] else '✖️'}] ›°", data="button"),
            Button.inline(f"°› Voice [{'✔️' if database['voice'] else '✖️'}] ›°", data="voice"),
        ),
        (
            Button.inline(f"°› Forward [{'✔️' if database['forward'] else '✖️'}] ›°", data="forward"),
            Button.inline(f"°› Video [{'✔️' if database['video'] else '✖️'}] ›°", data="video"),
        ),
        (Button.inline("[ ↻ ]", data="gpl2"),),
        (Button.inline(f"°› BacK ›°", data="bk_panel"),),
    ]
    await event.edit('°› Menu: (1/2) ›°', buttons=buttons)
async def panel_2(event: events.InlineQuery.Event):
    database = js.loads(clir.hget('plAddGroPSettinGZ', str(event.chat_id)))
    buttons = [
        (
            Button.inline(f"°› Via [{'✔️' if database['via'] else '✖️'}] ›°", data="via"),
            Button.inline(f"°› Music [{'✔️' if database['music'] else '✖️'}] ›°", data="music"),
        ),
        (
            Button.inline(f"°› File [{'✔️' if database['file'] else '✖️'}] ›°", data="file"),
            Button.inline(f"°› Bot [{'✔️' if database['bot'] else '✖️'}] ›°", data="bot"),
        ),
        (
            Button.inline(f"°› Location [{'✔️' if database['location'] else '✖️'}] ›°", data="location"),
            Button.inline(f"°› Contact [{'✔️' if database['contact'] else '✖️'}] ›°", data="contact"),
        ),
        (
            Button.inline(f"°› Caption [{'✔️' if database['caption'] else '✖️'}] ›°", data="caption"),
            Button.inline(f"°› unknown [{'✔️' if database['unknown'] else '✖️'}] ›°", data="unknown"),
        ),
        (Button.inline("[ ↻ ]", data="gpl1"),),
        (Button.inline(f"°› BacK ›°", data="bk_panel"),),
    ]
    await event.edit("Menu (2/2)",buttons=buttons)
async def pl_main(event: events.InlineQuery.Event):
    buttons = [
            (
                Button.inline(f"°› Settings ›°", data="gpl1"),
            ),
            (
                Button.inline("°› List Mute GP ›°", data="list_mute_gp"),
                Button.inline("°› List Mute PV ›°", data="list_mute_pv"),
            ),
            
            (Button.inline("°› [ ExiT ] ›°", data="exitpl"),
            )
        ]
    await event.edit('°› Welcome to the management panel of Group!\nPlease choose: ›°', buttons=buttons)
@bot.on(events.CallbackQuery())
async def main_call(event: events.CallbackQuery.Event):
    buttons = [(Button.inline("°› [ BacK ] ›°", data="bk_panel"),),]
    if (event.data.split()[0] == b"ftabchi" or event.data.split()[0] == b"ttabchi"):
        if event.original_update.user_id == int(event.data.split()[1]):
            return await cktabchi(event)
        else : await event.answer('برای تو نیستش.', alert= True)
    elif event.query.user_id in sudo:
        try:
            if event.data == b"exitpl":
                return await event.edit('**› panel was closed !**')
            elif event.data == b"list_mute_pv":
                return await event.edit('Muted User in Pv :'+' - '.join(clir.lrange('plMutePVUsEr', 0, -1)),buttons=buttons)
            elif event.data == b"list_mute_gp":
                return await event.edit('Muted User in GrouP :',clir.hgetall('plMut3UserInPG'),buttons=buttons)
            elif event.data == b"radio.stations":
                return await radio_stations(event)
            elif event.data.startswith(b"radio.play."):
                station = event.data.decode()[11:]
                stations = pl.Conf.RADIO_STATIONS
                await event.edit(f"**✘ Loading** \n`{station}`")
                await group_call_factory.vc_play_live_audio(event, stations[station], Client)
                text = f'<b>✘ Radio started !</b>\n• <u>{station}</u>\n\n'
                await event.edit(text,
                                 buttons=[
                                     [Button.inline("Stop", data="radio.stream.stop")],
                                     [Button.inline("Close", data="radio.close")],
                                 ], parse_mode="html")
                _stream_title = pl.get_playing_stream_title(stations[station])
                text = text + \
                       f'<b>• Currently playing</b>:\n\t <i>{_stream_title}</i>'
                await event.edit(text,
                                 buttons=[
                                     [Button.inline("Stop", data="radio.stream.stop")],
                                     [Button.inline("Close", data="radio.close")],
                                 ], parse_mode="html")

            elif event.data == b"radio.stream.stop":
                await group_call_factory.vc_stop(event.chat_id)
                await event.edit("• Radio Stream Stopped •",
                                 buttons=[(Button.inline("°• [ BacK ] •°", data="radio.menu.main"))])
            elif event.data == b"radio.close":
                await event.answer("• Radio Panel Closed •")
                await Client.delete_messages(event.chat_id, event.message_id)

            elif event.data == b"radio.menu.main":
                await event.edit("**Welcome to Radio Panel**\n\nChoose from the following options:\n\n‌",
                                 buttons=[
                                     [Button.inline("Radio Stations 🎙", data="radio.stations")],
                                     [Button.inline("Radio Settings ⚙️", data="radio.settings")],
                                     [Button.inline("Close", data="radio.close")],
                                 ])
            else:
                await pl.switch(event.data,{
                    b"gpl1":panel_1,
                    b"gpl2":panel_2,
                    b"bk_panel":pl_main,
                    b"link":main_call,
                    b"photo":main_call,
                    b"stiker":main_call,
                    b"gif":main_call,
                    b"service":main_call,
                    b"game":main_call,
                    b"button":main_call,
                    b"voice":main_call,
                    b"forward":main_call,
                    b"video":main_call,
                    b"via":main_call,
                    b"music":main_call,
                    b"file":main_call,
                    b"bot":main_call,
                    b"location":main_call,
                    b"unknown":main_call,
                    b"contact":main_call,
                    b"caption":main_call,
                    b"tban":cktabchi,
                    b"tunrt":cktabchi,
                }, pl.empty_async)(event)
        except MessageNotModifiedError as e:
            await event.answer('اهسته تر', alert= True)  
    else:
        await event.answer('- You do not have this access !')
async def main_call(event: events.CallbackQuery.Event):
    database = clir.hget('plAddGroPSettinGZ', str(event.chat_id))
    if database == None: return
    else: database = js.loads(database)
    if event.query.user_id in sudo:
            try:await pl.setup_data(
                    database, 
                    key := event.data.decode('utf-8'), 
                    clir, 
                    js, 
                    event,
                    panel_1 if key in [
                        "link",
                        "photo",
                        "stiker",
                        "gif",
                        "service",
                        "game",
                        "button",
                        "voice",
                        "forward",
                        "video",
                    ] else panel_2,
                ) 
            except MessageNotModifiedError as e:
                await event.answer('اهسته تر', alert= True)  
    else:
         await event.answer('-You do not have this access!') 

async def radio_stations(event: events.CallbackQuery.Event):
    stations = pl.Conf.RADIO_STATIONS
    buttons = []
    for station in stations.keys():
        buttons.append([Button.inline(station, data=f"radio.play.{station}")])

    await event.edit("**✘ Radio Stations**\n\n‌", buttons=buttons)


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
