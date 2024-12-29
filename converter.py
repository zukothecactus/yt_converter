import subprocess
import os
from pytubefix import YouTube
from pytubefix import Playlist

def convert_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec","libmp3lame",
        "-ab", "320k",
        "-ar", "44100",
        "-y", 
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Conversion successful")
    except subprocess.CalledProcessError as e:
        print("Conversion failed")


def mp4_file_remover():
    directory_path = r"C:\Users\obren\OneDrive\Desktop\code\projekti\yt_converter\yt_converter"
    for item in os.listdir(directory_path):
        if(item.endswith(".mp4")):
            file_path = os.path.join(directory_path, item)
            try:
                os.remove(file_path)
                print(f"{item} has been deleted.")
            except Exception as e:
                print(f"Error deleting {item}: {e}")


def yt_download(link):
    
    if (is_Pl == "p"):
        playlist = Playlist(link)
        for video_url in playlist.video_urls:
            try:
                video = YouTube(video_url)
                video = video.streams.get_lowest_resolution()
                video.download()
                print(video.title +" has been downloaded\n")
                convert_to_mp3(video.title+".mp4", video.title+".mp3")
            except Exception as e:
                print(f"Failed to download {video_url}: {e}")
    else:
        youtube_video = YouTube(link)
        youtube_video = youtube_video.streams.get_lowest_resolution()
        youtube_video.download()
        print(youtube_video.title +" has been downloaded\n")
        convert_to_mp3(youtube_video.title+".mp4", youtube_video.title+".mp3")
    mp4_file_remover()
    
    
is_Pl = ''
ans = True
while(ans):
    is_Pl = input("Do you want to download a playlist or a single video (p/s)? ")
    if(is_Pl == "p"):
        link = input("Unesite link playlist-e: ")
        ans = False;
    elif is_Pl =="s":
        link = input("Unesite link od video snimka: ")
        ans = False;
    else:
        print("Morate izabrati ili jedan video ili playlist-u")
    
yt_download(link.strip())