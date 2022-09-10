from video_player import MusicazooPlayer
import time

mp = MusicazooPlayer()
mp.play("https://www.youtube.com/watch?v=Q3iLqA0Dl_E")
time.sleep(10)
mp.pause()
time.sleep(5)
mp.play()
while True:
    pass