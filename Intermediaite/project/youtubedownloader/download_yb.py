from pytube import YouTube


link = "https://www.youtube.com/watch?v=pRKp-0CYgWg"

youtubeObj = YouTube(link)

youtubeObj = youtubeObj.streams.get_highest_resolution()
try:
    youtubeObj.download()
except:
    print("An error as occurred")
else:
    print("Done.")

