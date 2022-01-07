from pytube import YouTube
import os
import moviepy.editor as mp


def download_mp4(video):
    print("downloading video, this may take a bit")
    try:
        yt = YouTube(video)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(os.getcwd(),
                                                  filename="output.mp4")

        print("video properly downloaded")
    except:
        print("something went wrong")


def download_mp3(video):
    print("downloading video, this may take a bit")
    try:
        yt = YouTube(video)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(os.getcwd(),
                                                  filename="output.mp4")

        video = mp.VideoFileClip(r"output.mp4")
        video.audio.write_audiofile(r"output.mp3")

        print("video properly downloaded")
    except:
        print("something went wrong")


video = str(input("Enter the URL of the video you would like to download \n"))

choice = input("would you like to download an mp4 or mp3?\n")

if choice.lower() == "mp4":
    download_mp4(video)
elif choice.lower() == "mp3":
    download_mp3(video)
else:
    print("enter a valid option")
