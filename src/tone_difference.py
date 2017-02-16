# -*- coding: utf-8 -*-
# http://aidiary.hatenablog.com/entry/20110607/1307449007

#modules import
import sys
import argparse
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

#functions
def play (data, fs, bit):
    import pyaudio
    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=int(fs),
                    output= True)
    # チャンク単位でストリームに出力し音声を再生
    chunk = 1024
    sp = 0  # 再生位置ポインタ
    buffer = data[sp:sp+chunk]
    while buffer != '':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp+chunk]
    stream.close()
    p.terminate()

def createWave(A, f0, fs, length, soundtype):
    """振幅A、基本周波数f0、サンプリング周波数 fs、
    長さlength秒の正弦波を作成して返す"""
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        if soundtype=="basic":
            s = A * np.sin(2 * np.pi * f0 * n / fs)
        elif soundtype=="triangle":
            s = 0.0
            for k in range(0, 10):  # サンプルごとに10個のサイン波を重ね合わせ
                s += (-1)**k * (A / (2*k+1)**2) * np.sin((2*k+1) * 2 * np.pi * f0 * n / fs)
        elif soundtype=="square":
            s = 0.0
            for k in range(1, 10):
                s += (A / (2*k-1)) * np.sin((2*k-1) * 2 * np.pi * f0 * n / fs)
        elif soundtype=="sawtooth":
            s = 0.0
            for k in range(1, 10):
                s += (A / k) * np.sin(2 * np.pi * k * f0 * n / fs)
        else:
            print("We don't have soundtype: "+soundtype)
            sys.exit()
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    return data

def createWaveChord(A, f0, fs, length, soundtype):
    """freqListの正弦波を合成した波を返す"""
    data = []
    amp = float(A) / len(freqList)
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for f in freqList:
            s += amp * np.sin(2 * np.pi * f * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    return data

def waveTrans(data):
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    #plot(data[0:100]); show()
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--chord", type=bool, default=False)
    parser.add_argument("--soundtype", type=str, default="basic")
    args = parser.parse_args()

    freqList = [262, 294, 330, 349, 392, 440, 494, 523]  # ドレミファソラシド
    chordList = [(262, 330, 392),  # C（ドミソ）
                 (294, 370, 440),  # D（レファ#ラ）
                 (330, 415, 494),  # E（ミソ#シ）
                 (349, 440, 523),  # F（ファラド）
                 (392, 494, 587),  # G（ソシレ）
                 (440, 554, 659),  # A（ラド#ミ）
                 (494, 622, 740)]  # B（シレ#ファ#）

    data = []
    if args.chord and args.soundtype=="basic":
        for freqList in chordList:
            data.extend(createWaveChord(1.0, freqList, 44100.0, 1.0, args.soundtype))
    elif not args.chord:
        for f in freqList:
            data.extend(createWave(1.0, f, 44100.0, 1.0, args.soundtype))
    else:
        print("haven't been implemented yet")
        sys.exit()

    #データフォーマットの変更、再生
    data = waveTrans(data)
    play(data, 44100, 16)
