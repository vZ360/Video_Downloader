import pytube
link = input("Enter Youtube Link Here >> ") #enter link here
SAVE_PATH = "D:\"                          #file path comment edited by paulson
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH) 




