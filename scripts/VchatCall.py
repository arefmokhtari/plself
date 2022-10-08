
from typing import Optional
from pytgcalls import PyTgCalls, StreamType, idle
from pytgcalls.exceptions import AlreadyJoinedError, GroupCallNotFound, NoActiveGroupCall, NotInGroupCallError
from pytgcalls.types.input_stream import InputStream, InputAudioStream
from pytgcalls.types import input_stream
from pytgcalls import types
from pytgcalls.types.input_stream import quality as stream_quality
from telethon import TelegramClient, events
from pytgcalls.types.groups.group_call import GroupCall
from pytgcalls.pytgcalls import PyTgCalls as ptgc
from telethon.errors import ChatAdminRequiredError
from telethon.tl.functions.phone import CreateGroupCallRequest
from scripts.plPlugins import findfile
import os

class VcInfo:
    def __init__(self, chat_id, call: ptgc):
        self.chat_id = chat_id
        self.vchat = call
        self.data = None

    async def get_call(self):
        try:
            self.data = await self.vchat.get_call(self.chat_id)
        except GroupCallNotFound:
            self.data = None

    @property
    def is_playing(self) -> Optional[bool]:
        if self.data:
            _is_playing = self.data
            return _is_playing.is_playing

    @property
    def is_joined(self) -> bool:
        if self.data:
            return True

    @property
    def status(self) -> str:
        if self.data:
            return self.data.status


class VchatCall:
    def __init__(self, client: TelegramClient):
        self._client = client
        self.vchat = PyTgCalls(client)
        self.vchat.start()

    async def vc_play_local(self, event: events.newmessage.NewMessage.Event, file_name, msg4show):
        if findfile('input.raw', os.getcwd()): os.remove('input.raw')
        os.system(
            f"ffmpeg -y -i \"{file_name}\" -f s16le -ac 1 -ar 48000 -acodec pcm_s16le input.raw -hide_banner -loglevel error")
        os.remove(file_name)
        try:
            await self.vchat.join_group_call(event.chat_id, InputStream(
                InputAudioStream(
                    "input.raw",
                ),
            ), stream_type=StreamType().local_stream)
        except AlreadyJoinedError:
            await self.vchat.change_stream(event.chat_id, InputStream(
                InputAudioStream(
                    "input.raw",
                ),
            ))

        await msg4show.edit(f'**♫ Playing ♫**\n**• Song title:** `{file_name}`')

    async def vc_play_live_audio(self, event: events.newmessage.NewMessage.Event, link_stream,
                                 msg4show):
        # if not check_stream(link_stream):
        #     await msg4show.edit(f'**• Error: **\n`{link_stream}`\n`is not a valid stream link!`')
        #     return
        try:
            await self.vchat.join_group_call(event.chat_id, input_stream.AudioPiped(link_stream,
                                                                                    stream_quality.MediumQualityAudio(), ),
                                             stream_type=StreamType().pulse_stream)
        except AlreadyJoinedError:
            await self.vchat.change_stream(event.chat_id,
                                           input_stream.AudioPiped(link_stream, stream_quality.MediumQualityAudio(), ),
                                           # stream_type=StreamType().pulse_stream
                                           )
        except NoActiveGroupCall:
            await self._client(CreateGroupCallRequest(event.chat_id))
            await self.vchat.join_group_call(event.chat_id, input_stream.AudioPiped(link_stream,
                                                                                    stream_quality.MediumQualityAudio(), ),
                                             stream_type=StreamType().pulse_stream)

        except ChatAdminRequiredError:
            await msg4show.edit('**• Error: **\n`I need to be an admin for create a voice chat!`')
            return

    async def _is_played(self, chat_id):
        try:
            _is_playing: GroupCall = await self.vchat.get_call(chat_id)
            return _is_playing.is_playing
        except GroupCallNotFound:
            return None

    async def _is_joined(self, chat_id: int):
        """
        Check if the bot is joined to a voice chat
        :param int chat_id: group chat id
        :return: True if joined, False if not joined or group call not found
        """
        try:
            await self.vchat.get_call(chat_id)
            return True
        except GroupCallNotFound:
            return False

    async def vc_stop(self, chat_id):
        if await self._is_played(chat_id):
            try:
                await self.vchat.leave_group_call(chat_id)
            except NotInGroupCallError:
                return False
        else:
            return False

    def info(self, chat_id):
        return VcInfo(chat_id, self.vchat)
