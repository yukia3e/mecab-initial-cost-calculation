# mecab-initial-cost-calculation
MeCabのカスタム辞書を作成する際に算出が必要となる単語生起コストについて、算出するPythonプロジェクト。

## カスタム辞書作成方法（cost-calculation活用）
### コスト計算
``` sh
python3 cost-calculation.py -f ${moto}.csv -o ${cost_calculated}.csv

python3 cost-calculation.py -f ${moto}.csv -o ${cost_calculated}.csv -c 0.5 -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd --skip
```

### 辞書ファイル作成
``` sh
/usr/lib/mecab/mecab-dict-index -d /usr/share/mecab/dic/ipadic -u ${dic_name}.dic -f utf-8 -t utf-8 ${cost_calculated}.csv

/usr/lib/mecab/mecab-dict-index -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -u ${dic_name}.dic -f utf-8 -t utf-8 ${moto}.csv
```
※ `sudo find  /usr/ -name rewrite.def`

### mecabrcへの定義
```sh
vim /etc/mecabrc
vim /usr/local/etc/mecabrc
```

```
userdic = /root/mecab-initial-cost-calculation/${dict_name}.dic
```

### 実行時指定
```
mecab -u ${dict_name}.dic
mecab -u /root/mecab-initial-cost-calculation/${dict_name}.dic,/root/mecab-initial-cost-calculation/${dict_name} -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -Odump
```
http://www.mwsoft.jp/programming/nlp/mecab_dictionary_customize.html


## コスト自動推定
### モデル
https://taku910.github.io/mecab/dic.html より
[ダウンロード](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7bnc5aFZSTE9qNnM)

### 辞書データ
https://taku910.github.io/mecab/ よりIPA 辞書,
[ダウンロード](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM) 