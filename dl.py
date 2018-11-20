from __future__ import unicode_literals
import youtube_dl
import sys

def _hook(_d):
    if _d['status'] == 'finished':
        print('Done downloading, now converting ...')

_codec = str(sys.argv[2])
_out = '%(id)s.'+_codec
_ext = '.%(ext)s'
ydl_opts = {
    'format': 'bestaudio/best',
    'preferredcodec': _codec,
    'outtmpl': _out,        
    'noplaylist' : True,        
    'progress_hooks': [_hook],
    'key': 'FFmpegExtractAudio',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.extract_info(str(sys.argv[1]))