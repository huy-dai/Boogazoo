import vlc
import utils
import conf
import time

PLAYING = 3 #VLC status code
PAUSED = 4 

class MusicazooPlayer:
    '''
    A simple video player for Musicazoo
    '''
    def __init__(self):
        self.player = vlc.MediaPlayer()
        
        #The following describes the video being played
        self.filename = None
        self.title = None
        
    def play(self, yt_url=None):
        media_state = self.player.get_state()
        if media_state == PAUSED:
            #Resume video
            self.player.play()
        else:
            #Play a new video
            self.filename, self.title = utils.download_video(yt_url)
            full_path = conf.CATALOG_FOLDER + self.filename
            media = vlc.Media(full_path)
            self.player.set_media(media)
            self.player.play()
            media_state = self.player.get_state()
            while media_state != PLAYING: #Make sure video gets played before continuing
                time.sleep(0.1)
                media_state = self.player.get_state()
            
    def pause(self):
        self.player.set_pause(1)
        


        
