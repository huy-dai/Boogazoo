import vlc
import utils
import conf
import time
from os.path import exists

PLAYING = 3 #VLC status code
PAUSED = 4 


class MusicazooPlayer:
    '''
    Main musicazoo service. Manages queueing of
    songs, and provide interactive options for
    playing, resuming, skipping, and changing
    speeds of a video.
    '''
    def __init__(self):
        self.queue = [] #Holds tuples of (filename, title) of videos on the queue
        self.player = vlc.MediaListPlayer() #Main player
        
        vlc_object = vlc.Instance() 
        self.media_list = vlc_object.media_list_new() # Create new media list
        self.player.set_media_list(self.media_list) # Set media list to the media player
        
        #The following describes the video being played:
        self.curr_title = None
        
    def play(self):
        self.player.play()
        media_state = self.player.get_state()
        while media_state != PLAYING: #Make sure video gets played before continuing
            time.sleep(0.1)
            media_state = self.player.get_state()
                
    def queue_video(self,yt_url):
        '''
        Add a new video to the queue (if it doesn't already exists) and
        downloads it locally for later viewing
        '''
        new_filename, new_title = utils.download_video(yt_url)
        full_path = conf.CATALOG_FOLDER + new_filename
        file_exists = exists(full_path)
        if not file_exists:
            return #Error quietly
        if (new_filename,new_title) not in self.queue:
            self.queue.append((new_filename,new_title))
            media = vlc.Media(full_path) #Initialize media
            self.media_list.add_media(media) #Add media to ongoing media list
            
    def pause(self):
        self.player.set_pause(1)
    def stop(self):
        self.player.stop()
    def next(self):
        self.queue.pop(0)
        if self.queue[0][1]: #Title of the first video in queue
            self.curr_title = self.queue[0][1] 
        self.player.next() # Observed behavior is that video player
                           # will only change if there is another video queued
        
    def get_curr_title(self):
        return self.curr_title

if __name__ == '__main__':
    #Test case
    mp = MusicazooPlayer()
    mp.queue_video("https://www.youtube.com/watch?v=Q3iLqA0Dl_E")
    mp.queue_video("https://www.youtube.com/watch?v=8bBmDAtHUJY")
    mp.play()
    time.sleep(3)
    mp.next()
    time.sleep(10)
            
