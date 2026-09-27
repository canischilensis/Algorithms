from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=GV3HUDMQ-F8').streams.first().download()
#yt = YouTube('https://www.youtube.com/watch?v=1D9MBzh_J58&')
#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
