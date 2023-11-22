from pytube import Youtube
from pathlib import Path
from os import *
from pywebio.input import *
from pywebio.output import *

def video_download():
    while True:
        video_link = input('Informe o Link do Video')
        if video_link.split('//')[0] == 'https:':
            put_text('Fazendo dowbnload do Video'.title()).style('color:red; font-size: 50px')
            video_url = Youtube(video_link)
            video = video_url.streams.get_highest_resolution()
            path_to_download = (r'c:\Users\seavi\downloads')
            video.downloads(path_to_download)
            put_text('Video baixado com sucesso!...'.title()).style('solor: blue; font-size: 50px')
            startfile(r'c:\\Users\\seavi\\downloads')

if __name__ == '__main__':
    video_download()
