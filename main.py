from pytube import YouTube

video = str(input("Enter the URL of the video you would like to download \n"))

print("downloading video, this may take a bit")
try:
  YouTube(video).streams.first().download()
  print("video properly downloaded")
except:
  print("something went wrong")