# -*- coding: utf-8 -*-
#http://qiita.com/icoxfog417/items/d376200407e97ce29ee5

#modules import
import argparse
import numpy as np
import wave
from practice import *

#functions
def make_sound(graph_flag):
    A, f, phi, fs = .8, 1000, np.pi/2, 44100
    t = np.linspace(0, 3, int(3*fs))
    x = A * np.cos(2 * np.pi* f * t + phi)
    if graph_flag:
        display_graph(data=x[0:int(0.02*fs)],start_time=0,period=0.02)

    return x

#main function
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", type=bool, default=False)
    args = parser.parse_args()

    made_sample = make_sound(graph_flag=args.graph)

    output_path = "../out_data/made_sample_sound.wav"

    data_export(made_sample,output_path)
