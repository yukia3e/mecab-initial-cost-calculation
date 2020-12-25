# mecab-initial-cost-calculation

MeCab のカスタム辞書を作成する際に算出が必要となる単語生起コストについて、算出する Python プロジェクト。

## 環境構築（for Docker）

```
cd env/
sh build.sh
sh run.sh
```

## 環境構築（for Mac）

### venv で新しい仮想環境を構築

```
python3 -m venv .venv
```

### 各種パッケージ のインストール

```
# 仮想環境に入る
$ source .venv/bin/activate

# パッケージのインストール
(.venv)$ pip install -r requirements.txt

# 仮想環境を抜ける
(.venv)$ deactivate
```

### 形態素解析関連のインストール

```
# MeCabのインストール
$ brew install MeCab

# Neologd辞書のインストール
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a -y
# 出力されるパスがNeologdのパスとなるのでメモしておく

# char.defの書き換え
$ cp mecab/defs/char.def ~/mecab-ipadic-neologd/build/mecab-ipadic-2.7.0-20070801-neologd-20200910/

```

## カスタム辞書作成方法

### コスト計算

```sh
cd src

echo "Full Options for Docker"
python3 cost-calculation.py -f ${data}.csv -o ${calc_result}.csv -c 0.5 -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd --skip

echo "Sample for Docker"
python3 cost-calculation.py -f data/${data}.csv -o calc_result/${calc_result}.csv -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd

echo "Sample for Mac"
python3 cost-calculation.py -f data/${data}.csv -o calc_result/${calc_result}.csv -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd
```

### 辞書ファイル作成

```sh
echo "for Docker"
/usr/lib/mecab/mecab-dict-index -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -u dict/${dict_file}.dic -f utf-8 -t utf-8 calc_result/${calc_result}.csv

echo "for Mac"
/usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -u dict/${dict_file}.dic -f utf-8 -t utf-8 calc_result/${calc_result}.csv
```

### 実行時指定

```
mecab -u name.dic
mecab -u /root/mecab-initial-cost-calculation/${dict_file}.dic -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -Odump
```

http://www.mwsoft.jp/programming/nlp/mecab_dictionary_customize.html

## 参考）コスト自動推定 モデル・辞書データ

### モデル

https://taku910.github.io/mecab/dic.html より
[ダウンロード](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7bnc5aFZSTE9qNnM)

### 辞書データ

https://taku910.github.io/mecab/ より IPA 辞書,
[ダウンロード](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM)
