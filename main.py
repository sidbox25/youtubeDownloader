from pytube import YouTube
from youtube_search import YoutubeSearch
import os
import csv

currentWorkinDirectory = os.getcwd()

downloadLocation  = os.getcwd()+"/download"

def downloadAudioByUrl(url):
        video = YouTube(url=url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path=downloadLocation,skip_existing=True,filename=f"{video.title}.mp3")

def downloadAudioByName(vidoName):
    try:
        YoutubeSearchResult = YoutubeSearch(vidoName, max_results=1).to_dict()
        url = "https://www.youtube.com/" + YoutubeSearchResult[0]["url_suffix"]

        downloadAudioByUrl(url)
    except:
        print("could not find " + vidoName)
        return


downloadAudioByUrl("https://www.youtube.com/watch?v=7Sk78uP9m-E")

"""
songsToDownload = []
with open("favered_mirror.csv","r") as file:
    desciptors = file.readline()
    for songName in file:
        if songName == "":
            pass
        songNameSplit = songName.split(",")
        songsToDownload.append(songNameSplit[2][1:-1]+" by "+songNameSplit[4][1:-1])

i = 0
for songName in songsToDownload:
    if (i<5):
        print(songName)
        downloadAudioByName(songName)
    i += 1

"""


