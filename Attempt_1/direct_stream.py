import vlc
import pafy
import time

url = "https://www.youtube.com/watch?v=DcCISK3sCYg"
  
# creating pafy object of the video
video = pafy.new(url) 

print(video.streams)


# getting best stream
best = video.getbest()

# creating vlc media player object
media = vlc.MediaPlayer(best.url)
  
# start playing video
media.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(100)