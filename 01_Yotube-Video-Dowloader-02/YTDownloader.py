'''This code is print the title of the video
   and views of the video.
   Q1)How to Run
     cammand: [python .\Yotube-Video-Dowloader-02\YTDownloader.py "Link" ] 
'''
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
# print title and views of the video

# Now code for downloading
yd = yt.streams.get_by_resolution("720p")
yd.download('Users\csp\Documents\DATA-STRUCTURE & ALGO\Python-Expo\PyProjects')


