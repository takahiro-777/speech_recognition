#coding:utf-8
#Last Change: 2013_11_15_12:42:13.
#http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

import math
import numpy
import pyaudio

# 定数の生成
key_name = ["C","D","E","F","G","A","B","C+"]
key_diff = [-9,-7,-5,-4,-2,0,2,3]
key_frequency = {}
for key,diff in zip(key_name,key_diff):
  key_frequency[key] = 440 * math.pow(2,diff * (1/12.0))

def sine(frequency, length, rate):
  length = int(length * rate)
  factor = float(frequency) * (math.pi * 2) / rate
  return numpy.sin(numpy.arange(length) * factor)

def chord(frequency, length, rate):
  # 音源生成
  src = []
  src.append(sine(frequency,length,rate))
  src.append(sine(frequency * math.pow(2,(4/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(7/12.0)),length,rate))
  res = numpy.array([0] * len(src[0])) #ダミーの空配列

  #加算&クリッピング
  for s in src:
    res = res + s
  res *= 0.5

  return res

def play_chord(stream, frequency=440, length=1, rate=44100):
  chunks = []
  chunks.append(chord(frequency, length, rate))
  chunk = numpy.concatenate(chunks) * 0.25
  stream.write(chunk.astype(numpy.float32).tostring())

if __name__ == '__main__':
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paFloat32,
      channels=1, rate=44100, output=1)

  for key in key_name:
    play_chord(stream,frequency=key_frequency[key])

  stream.close()
  p.terminate()
