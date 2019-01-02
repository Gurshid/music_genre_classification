# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:49:05 2018

@author: Gurshid
"""

#import libraries
from pydub import AudioSegment
import os

#setting ffmpeg path
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"

src_dir = 'D:/Projects/Machine Learning/Music Genre Classification/Mp3'
dst_dir = 'D:/Projects/Machine Learning/Music Genre Classification/Wav'

#Convert .mp3 to .wav
def conv(mp3,prefix):
    sound = AudioSegment.from_mp3(src_dir + '/' + mp3)
    sound.export(dst_dir + '/' + prefix + '.wav', format="wav")
    #print('Hello : ', i)

def main():
    #i=0
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            prefix, suffix = os.path.splitext(f)
            conv(f,prefix)
    #       i=i+1
        
if __name__ == "__main__":
    main()