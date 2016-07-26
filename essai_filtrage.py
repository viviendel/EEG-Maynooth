from pylsl import StreamInlet, resolve_stream
from matplotlib import pyplot as plt
import scipy.signal as signal
from scipy.signal import filter_design as fd
from scipy.signal import kaiserord, lfilter, firwin, freqz
from numpy import *
from scipy import signal
from scipy.signal import filter_design as fd
from matplotlib import pyplot as plt

import numpy as np

# Bandpass
Fs = 500
Wp =  [0.270, 0.333]
Ws =  [0.230, 0.373]
Rp = .1
As = 20.
b,a = signal.filter_design.iirdesign(Wp,Ws,Rp,As,ftype='ellip')
w,H = signal.freqz(b,a)  # filter response




print("attente d'un stream EEG")
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])


amp = []
temps_init = []
while True:
    sample, timestamp = inlet.pull_sample()
    #print(timestamp, sample)
    C1 = sample[0:1]  # Affichage du canal 1 (1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8)
    temps = timestamp
    temps_init.append(temps)
    amp.append(C1)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(temps_init,amp)
    plt.subplot(212)
    yf = signal.filtfilt(b, a, amp, padlen = 0)
    plt.plot(temps_init,yf,'r')
    plt.draw()
    plt.pause(0.05)  # figure updated and displayed, and the GUI event loop will run during the pause
    plt.clf()  # clear the current figure

