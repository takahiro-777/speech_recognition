# -*- coding: utf-8 -*-
#  http://qiita.com/yu_tailsfox/items/86380a0d4d016e1634f1
# http://flat-leon.hatenablog.com/entry/python_argparse

#modules import
import argparse
import numpy as np
import wave
import matplotlib.pyplot as plt

#functions
def data_load(file_name):
    wavefile = wave.open(file_name, "r")
    framerate = wavefile.getframerate()
    data = wavefile.readframes(wavefile.getnframes())
    x = np.frombuffer(data, dtype="int16")
    return x

def data_export(data,file_name):
    w = wave.Wave_write(file_name)
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    w.writeframes(data)
    w.close()

def display_graph(data,start_time,period):
    flip=1
    x = np.linspace(0, period, int(44100*period))
    start_pos = int(44100*start_time)
    #print(x.shape)
    #print(data.shape)
    #for i in range(1, 7):
        #plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
    plt.plot(x, data[start_pos:(start_pos+int(44100*period))] * flip)
    plt.show()

#main function
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", type=bool, default=False)
    args = parser.parse_args()

    input_path = "../data/ashitaka_sekki.wav"
    output_path = "../out_data/ashitaka_sekki.wav"

    #data import
    x = data_load(file_name=input_path)
    print(x.shape)

    #graph display
    if args.graph:
        display_graph(data=x,start_time=4,period=2)

    #data export
    data_export(x,output_path)
