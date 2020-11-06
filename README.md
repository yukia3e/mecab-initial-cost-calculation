# mecab-initial-cost-calculation
## カスタム辞書作成方法
``` sh
/usr/lib/mecab/mecab-dict-index -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -u ${dic_name}.dic -f utf8 -t utf8 ${moto}.csv
```

```sh
vim /etc/mecabrc
```

```
userdic = /root/mecab-initial-cost-calculation/${dic_name}.dic
```