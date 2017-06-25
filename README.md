# Speech Recognition

## 概要
```
音声認識をやるにあたり、学習した内容の結果をまとめていく
```


## ファイル概要
#### src/practice.py
音声データの読み込みと書き込み、グラフの表示
```
cd src/
python practice.py --graph TRUE
(graphがTRUEだと、波形のグラフを表示する)
```

#### src/make_sound.py
音叉のような音のサンプルの作成
```
cd src/
python make_sound.py --graph TRUE
(graphがTRUEだと、波形のグラフを表示する)
```

#### src/make_chord.py
pyaudioを使用して和音の作成
```
cd src/
python make_chord.py
```

#### src/tone_difference.py
pyaudioを使用して和音の作成
```
cd src/
python tone_difference.py

option
--chord(bool) -> =TRUEで和音
--soundtype(str) -> ="basic","triangle","square","sawtooth"から選択
```
