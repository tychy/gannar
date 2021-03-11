# gannar
gannar用の通知ツール

ガンナー http://cgi1.plala.or.jp/~ssdi/gannar.cgi

# 想定環境
`.envrc`へ
```
export GANNAR_ID=hoge
export GANNAR_KEY=hogehoge
export LINE_TOKEN=hogehogehogehoge

```

# 使いかた
```
python main.py run # メイン関数が走る
python main.py test # unittestが走る
```

# 仕様
・開始前は通知しない
・体力が全回復した時通知

TODO
・本拠地が攻められた時通知
・自分の周りで動きがあった時通知
・チャットの特定のワードに反応
・特定のアイテムが使われた時通知(ex 雪)
