# Attempt One - Direct Stream

I wanted to test using `pafy` to get the streaming link for a Youtube video and then playing that directly in a Python-controlled VLC instance. While this option works, the output stream resolution is very low (either 360p or 480p) and there doesn't seem to be an easy way of combining separate video/audio stream together in VLC without them de-syncing after a period of time.

For now best option seem to still be to download the video directly and play it offline.