# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:18:28 2018

@author: Gurshid
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import os

root_dir = 'D:/Projects/Machine Learning/Music Genre Classification/Wav'

#To plot the spectogram. Take input in .wav format
def vidwav(wavfile,i):
    
    #Option 1
    y, sr = librosa.load(root_dir + '/' + wavfile, sr=None, mono=True)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                       fmax=8000)
    
    plt.figure(i)
    plt.subplot(211)
    librosa.display.specshow(librosa.power_to_db(S,
                                                 ref=np.max),
                             y_axis='mel', fmax=8000,
                             x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    
    
    #Option 2
    x, sr = librosa.load(root_dir + '/' + wavfile, sr=None, mono=True)
    mel = librosa.feature.melspectrogram(y=x, sr=sr)
    
    plt.figure(i)
    plt.subplot(212)
    librosa.display.specshow(librosa.power_to_db(mel,
                                                 ref=np.max),
                             y_axis='mel', fmax=8000,
                             x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Log Mel spectrogram')
    plt.tight_layout()
    
    
def main():
    i=0
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            vidwav(f,i)
            i=i+1

if __name__ == "__main__":
    main()