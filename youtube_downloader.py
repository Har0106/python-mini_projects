from pytube import YouTube
import os

link = input('Enter the link: ')
try:
    yt = YouTube(link)
except:
    print('Some Error Occured')
    quit()

video = yt.streams.get_highest_resolution()
path = input('Where to save the file: ')
try:
    print('Downloading...')
    video.download(path)
    print('Download Completed')
except:
    print('Some Error Occured')
    quit()

filename = input('file name: ')
os.rename(path+video.default_filename, path+filename+'.mp4')
