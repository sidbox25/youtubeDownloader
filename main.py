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

def getUrlByName(vidoName):
    results = YoutubeSearch(vidoName, max_results=1).to_dict()
    
    return "https://www.youtube.com/" + results[0]["url_suffix"]

def downloadAudioByName(vidoName):
    try:
        url = getUrlByName(vidoName)

        
    except:
        print("could not find " + vidoName)
        return

    downloadAudioByUrl(url)


songsToDownload = []
with open("downloadList1.csv","r") as file:
    for songName in file:
        if songName == "":
            pass
        songsToDownload.append(songName)


for songName in songsToDownload:
    print(songName)
    downloadAudioByName(songName)




