import conf
import yt_dlp

def download_video(link):
    '''
    Downloads the provided video link using 
    yt-dlp and then returns the downloaded filename 
    and title as a tuple
    '''
    ydl_opts = {'outtmpl': (conf.CATALOG_FOLDER + "%(id)s.%(ext)s")} #Save as [video-id].[ext]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)
        
        #Retrieve filename + video title of video
        info_dict = ydl.extract_info(link, download=False)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)
        ext = info_dict.get('ext',None)
        filename = "{}.{}".format(video_id,ext)
        return (filename,video_title)
        
