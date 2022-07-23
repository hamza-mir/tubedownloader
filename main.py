from pytube import YouTube as yt

vid = yt('https://www.youtube.com/watch?v=L2QfUJVnrDY')

print(f'Title: {vid.title}')
streams = vid.streams.filter(type='video', progressive=True)
for stream in streams:
    itag = str(stream.itag)
    mtype = stream.mime_type
    res = stream.resolution
    adapt = stream.is_adaptive
    size = stream.filesize / (10 ** 6)
    print(f"itag: {itag}, type: {mtype}, resolution:{res}, size: {size:.2f}MB, audio/video separate: {adapt}")



# final = vid.streams.get_by_itag(398)
# final.download()