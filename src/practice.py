# -*- coding: utf-8 -*-
#  http://qiita.com/yu_tailsfox/items/86380a0d4d016e1634f1

#modules import
import numpy as np
import wave

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

if __name__ == '__main__':
    input_path = "../data/ashitaka_sekki.wav"
    output_path = "../out_data/ashitaka_sekki.wav"

    #data import
    x = data_load(file_name=input_path)
    print(x.shape)

    #data export
    data_export(x,output_path)
