# twitter_bot
Twitter に投稿するスクリプト。

- twitter-bot.py : tweets.txt の内容を投稿する。
- pos.txt : tweets.txt 内の、次に投稿する行番号を保存するファイル。
- tweets.txt : ツイート用の文章を行単位で保存するファイル。


twitter-bot.py でAPIキーを設定して使用する。

```
auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token_secret="")
```

