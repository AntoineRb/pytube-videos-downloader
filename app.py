from pytube import YouTube

from sys import argv

# link = argv[ 1 ]
link = input("Enter a link:")
yt = YouTube( link )

print( f'Title: { yt.title }')
print( f'Views: { yt.views }')

youtubedl = yt.streams.get_highest_resolution()

youtubedl.download('/home/antoinerb/yt/')