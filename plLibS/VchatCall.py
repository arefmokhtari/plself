#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from pytgcalls import GroupCallFactory
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class VchatCall(GroupCallFactory):
    def __init__(self, Client):
        super().__init__(Client, self.MTPROTO_CLIENT_TYPE.TELETHON)
        self._play_voice = None
    def is_played(self) -> bool:
        return bool(self._play_voice)
    async def start_voice_chat(self, event, msg4show,  file_name = None, *,
                               youtube: bool = False, youtube_link = None):
        await self.stop_voice_chat()
        if findfile('input.raw', os.getcwd()): os.remove('input.raw')
        os.system(f'ffmpeg -i "{file_name}" -f s16le -ac 2 -ar 48000 -acodec pcm_s16le input.raw')
        os.remove(file_name)
        self._play_voice = self.get_file_group_call('input.raw')
        try:
            await self._play_voice.start(event.chat_id)
            await msg4show.edit('**• done !**')
        except asyncio.exceptions.TimeoutError as er:
            await msg4show.edit(f'{er}')
            print('-----')
    async def stop_voice_chat(self):
        if self.is_played():
            await self._play_voice.stop()
            self._play_voice = None
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #