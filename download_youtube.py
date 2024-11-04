from pytubefix import *
import io

def download(url):
    yt = YouTube(url)
    title = f"{yt.author} - {yt.title}"
    video_stream = yt.streams.get_highest_resolution()
    video_buffer = io.BytesIO()
    video_stream.stream_to_buffer(video_buffer)
    video_buffer.seek(0)
    return video_buffer, title
    
