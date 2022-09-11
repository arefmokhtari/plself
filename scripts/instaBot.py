#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import instaloader
import os
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class instaBot(instaloader.Instaloader):
    def __init__(self,session, username, password,dr = None, sleep: bool = True, quiet: bool = False, user_agent = None, dirname_pattern = None, filename_pattern = None,download_pictures=True, download_videos: bool = True, download_video_thumbnails: bool = True, download_geotags: bool = False,download_comments: bool = False, save_metadata: bool = True, compress_json: bool = True, post_metadata_txt_pattern: str = None,storyitem_metadata_txt_pattern: str = None, max_connection_attempts: int = 3, request_timeout: float = 300, rate_controller = None,resume_prefix = "iterator", check_resume_bbd: bool = True, slide = None, fatal_status_codes = None, iphone_support: bool = True,title_pattern = None, sanitize_paths: bool = False):
        super().__init__(sleep, quiet, user_agent, dirname_pattern, filename_pattern, download_pictures, download_videos, download_video_thumbnails, download_geotags, download_comments, save_metadata, compress_json, post_metadata_txt_pattern, storyitem_metadata_txt_pattern, max_connection_attempts, request_timeout, rate_controller, resume_prefix, check_resume_bbd, slide, fatal_status_codes, iphone_support, title_pattern, sanitize_paths)
        self._login_acc(session, username, password, dr)
    
    async def down_post(self, post, path = 'insta') -> dict:
        _post = instaloader.Post.from_shortcode(self.context, post)
        self.download_post(_post, target = path)
        file_name = [i for i in self._fileindir(self.format_filename(_post), os.listdir(path)) if self._checklist4insta(i)]
        return {'file':[path+'/'+fi for fi in file_name], 'post':_post}
    
    async def down_profile(self, username):
        _profile = self.check_profile_id(username)
        self.download_profile(_profile, profile_pic_only=True)
        pic_file = [i for i in os.listdir(_profile.username) if i.endswith('jpg')][0]
        return {'file':_profile.username+'/'+pic_file, 'profile': _profile}
    

    async def down_story(self, username):
        _profile = self.check_profile_id(username)
        self.download_profile(_profile, download_stories_only = True, profile_pic = False)
        files = [i for i in os.listdir(_profile.username) if self._checklist4insta(i)]
        return {'file':[_profile.username+'/'+i for i in files], 'profile': _profile}


    def _checklist4insta(self, pattern: str) -> bool:
        if pattern.endswith('xz') or pattern.endswith('txt') or pattern.endswith('json'):
            return False
        return True
    
    def _find_session(self,filename, dir = None):
        for files in os.listdir(dir):
            if files == filename:
                return True
        return False
    
    def _fileindir(self, pattern: str, dirlist) -> list: 
        return [FilE for FilE in dirlist if FilE.startswith(pattern)]
    
    def _login_acc(self,session, username, password, dr = None):
        print('\t- insta : ', end='')
        if self._find_session(session, dr):
            self.load_session_from_file(username, session) if dr is None else self.load_session_from_file(username, dr+'/'+session)
        else:
            self.login(username, password)
            self.save_session_to_file(session) if dr is None else self.save_session_to_file(dr+'/'+session)
                
    def _find_files(self, path):
        return [i for i in self._fileindir(path) if self._checklist4insta(i)]
    
    def remove_dir(path):
        for FilES in os.listdir(path):
            os.remove(path+'/'+FilES)
        os.rmdir(path)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - #