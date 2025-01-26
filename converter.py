import subprocess
import os
import yt_dlp
from pytubefix import YouTube
from pytubefix import Playlist
import shlex

def convert_to_mp3(input_file: str, output_file: str = None):
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Generate default output file name if not provided
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".mp3"
    
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-ac", "2",
        "-b:a", "320k",
        "-ar", "44100",
        "-y", 
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Conversion successful")
    except subprocess.CalledProcessError as e:
        print("Conversion failed")
        print(f"Command output: {e.stderr}")
    except FileNotFoundError:
        print("FFmpeg is not installed or not in PATH")


def mp4_file_remover():
    directory_path = r"C:\Users\obren\OneDrive\Desktop\code\projekti\yt_converter"
    for item in os.listdir(directory_path):
        if(item.endswith(".mp4")):
            file_path = os.path.join(directory_path, item)
            try:
                os.remove(file_path)
                print(f"{item} has been deleted.")
            except Exception as e:
                print(f"Error deleting {item}: {e}")


def yt_download(link):
#if(ext == "mp3"):
    if (is_Pl == "p"):
        playlist = Playlist(link)
        for video_url in playlist.video_urls:
            try:
                youtube_video = YouTube(video_url, 'WEB')
                youtube_video = youtube_video.streams.get_lowest_resolution()
                downloaded = youtube_video.download()
                ime = os.path.join(os.path.dirname(downloaded), youtube_video.title[:-24].strip()+".mp4")
                os.rename(downloaded, ime)
                print(ime +" has been downloaded\n")
                convert_to_mp3(ime)
            except Exception as e:
                print(f"Failed to download {video_url}: {e}")
    else:
        youtube_video = YouTube(link, 'WEB')
        youtube_video = youtube_video.streams.get_lowest_resolution()
        downloaded = youtube_video.download()
        ime = os.path.join(os.path.dirname(downloaded), youtube_video.title[:-24].strip()+".mp4")
        os.rename(downloaded, ime)
        print(ime +" has been downloaded\n")
        convert_to_mp3(ime)
    mp4_file_remover()
    
is_Pl = ''
ext = ''
ans = True
while(ans):
    is_Pl = input("Do you want to download a playlist or a single video (p/s)? ")
    #ext = input("Do you want audio or video files (mp3/mp4)? ")
    if(is_Pl == "p"):
        link = input("Unesite link playlist-e: ")
        ans = False;
    elif is_Pl =="s":
        link = input("Unesite link od video snimka: ")
        ans = False;
    else:
        print("Morate izabrati ili jedan video ili playlist-u")
    
yt_download(link.strip())