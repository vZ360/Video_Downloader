import pytube
link = input("Enter Youtube Link Here >> ") #enter link here
SAVE_PATH = "D:\"                          #file name 
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH) 




