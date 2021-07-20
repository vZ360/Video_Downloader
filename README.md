# Video_Downloader
Simple code to download videos to local machine using pytube 
import pytube
link = input("Enter Youtube Link Here >> ") #input link here 
SAVE_PATH = "D:\"                           #file location  
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH) 
