# -*- coding: utf-8 -*-
# http://aidiary.hatenablog.com/entry/20120225/1330179868

import wave
import numpy as np
import matplotlib.pyplot as plt

def wavread(filename):
    wf = wave.open(filename, "r")
    fs = wf.getframerate()
    x = wf.readframes(wf.getnframes())
    x = np.frombuffer(x, dtype="int16") / 32768.0  # (-1, 1)に正規化
    wf.close()
    return x, float(fs)

if __name__ == "__main__":
    # 音声をロード
    wav, fs = wavread("../data/a.wav")
    t = np.arange(0.0, len(wav) / fs, 1/fs)

    # 音声波形の中心部分を切り出す
    center = len(wav) / 2  # 中心のサンプル番号
    cuttime = 0.04         # 切り出す長さ [s]
    wavdata = wav[int(center - cuttime/2*fs) : int(center + cuttime/2*fs)]
    time = t[int(center - cuttime/2*fs) : int(center + cuttime/2*fs)]

    # 波形をプロット
    plt.plot(time * 1000, wavdata)
    plt.xlabel("time [ms]")
    plt.ylabel("amplitude")
    plt.savefig("../out_data/waveform.png")
    plt.show()
