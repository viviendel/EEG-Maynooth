from pylsl import StreamInlet, resolve_stream
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

canal1 = list()
canal2 = list()
canal3 = list()
canal4 = list()
canal5 = list()
canal6 = list()
canal7 = list()
canal8 = list()

plt.ion()

while True:

    sample = inlet.pull_sample()
    # print(timestamp, sample)
    if len(canal1) > 2000:
        del canal1[0]
        # del canal2[0]
        # del canal3[0]
        # del canal4[0]
        # del canal5[0]
        # del canal6[0]
        # del canal7[0]
        # del canal8[0]

    canal1.append(int(sample[0][0]))
    # canal2.append(sample[0][1])
    # canal3.append(sample[0][2])
    # canal4.append(sample[0][3])
    # canal5.append(sample[0][4])
    # canal6.append(sample[0][5])
    # canal7.append(sample[0][6])
    # canal8.append(sample[0][7])

    # plt.plot(canal1)
    # ax1=plt.subplot(811)
    #plt.plot(canal1)
    # ax2 = plt.subplot(812, sharex=ax1)
    # plt.plot(canal2)
    # ax3 = plt.subplot(813, sharex=ax1)
    # plt.plot(canal3)
    # ax4 = plt.subplot(814, sharex=ax1)
    # plt.plot(canal4)
    # ax5 = plt.subplot(815, sharex=ax1)
    # plt.plot(canal5)
    # ax6 = plt.subplot(816, sharex=ax1)
    # plt.plot(canal6)
    # ax7 = plt.subplot(817, sharex=ax1)
    # plt.plot(canal7)
    # ax8 = plt.subplot(818, sharex=ax1)
    # plt.plot(canal8)

    if len(canal1) > 2000:
        FFT=np.fft.fft(canal1)
        plt.plot(FFT)
        plt.ylim((-50000, 50000))
        plt.draw()
        plt.pause(0.01)
        plt.clf()
    # plt.draw()
    # plt.pause(0.001)
    # plt.clf()
    # print(canal1)
# EEG-Maynooth
