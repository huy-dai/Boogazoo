# Plans for Boogazoo

## Back-End

Use yt-dlp to download videos locally to a cache, and then use python-vlc to handle playing and queueing of video files

Provide REST APIs endpoint using Flask and a WSGI server (maybe Gunincorn) to allow remote interactions and returning of current state info

## Front-End

Design a simple Javascript website with modern CSS styling that interfaces with the back-end APIs for controlling of videos. Current framework considerations include Node.js or Svelte kit

Also displays information about the current queue, provide options to add video links
