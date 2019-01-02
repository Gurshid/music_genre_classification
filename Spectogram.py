# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:18:28 2018

@author: Gurshid
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import wave
from matplotlib.ticker import FuncFormatter
import os

root_dir = 'D:/Projects/Machine Learning/Music Genre Classification/Wav'

# Don't know
def kilo(x, pos):
    return '%1.fk' % (x*1e-3)

#To plot the spectogram. Take input in .wav format
def vidwav(wavfile, i, fps=25):

    wf = wave.open(root_dir + '/' + wavfile, 'rb')
    
    fs = wf.getframerate()
    N = wf.getnframes()
    duration = N/float(fs)
    if duration > 30:
        duration = 30
    bytes_per_sample = wf.getsampwidth()
    bits_per_sample  = bytes_per_sample * 8
    dtype = 'int{0}'.format(bits_per_sample)
    channels = wf.getnchannels()
    
    audio = np.fromstring(wf.readframes(int(duration*fs*bytes_per_sample/channels)), dtype=dtype)
    audio.shape = (int(audio.shape[0]/channels), channels)
    freqs = np.fft.fftfreq(audio[:,0].shape[0], 1.0/fs) / 1000.0
    max_freq_kHz = freqs.max()
    times = np.arange(audio.shape[0]) / float(fs)
    
    plt.figure(i)
    plt.subplot(211)
    plt.plot(times, (audio[:,0]).astype(float)/np.max(np.abs(audio[:,0])), c='k', lw=.3)

    plt.xlim(0,duration)
    plt.ylim(-1,1)
    
    l1, = plt.plot([], [], '#333333', lw=2)
    
    plt.figure(i)
    plt.subplot(212)
    plt.specgram(audio[:,0], Fs=fs, cmap=plt.get_cmap('jet'))
    plt.xlim(0,duration)
    plt.ylim(0,max_freq_kHz*1000.0)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    formatter = FuncFormatter(kilo)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(formatter)
    
    l2, = plt.plot([], [], '#333333', lw=2)
    
#   plt.tight_layout()
    plt.subplots_adjust(bottom=0.09, 
                                 right=0.98, 
                                 top=0.98, 
                                 left=0.08, 
                                 hspace=0.14)
    
def main():
    i=0
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            vidwav(f,i)
            i=i+1

if __name__ == "__main__":
    main()