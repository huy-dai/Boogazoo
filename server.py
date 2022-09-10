from flask import Flask, json, jsonify
from video_player import MusicazooPlayer
import time

app = Flask(__name__)

@app.route('/play', methods=['POST'])
def post_play():
  playMusic()
  return json.dumps({"success": True}), 201

# Test Run 
def playMusic():
  mp = MusicazooPlayer()
  mp.play("https://www.youtube.com/watch?v=Q3iLqA0Dl_E")
  time.sleep(5)
  mp.pause()
  time.sleep(5)
  mp.play()
  time.sleep(5)
  
if __name__ == '__main__':
    app.run() 