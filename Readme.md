# ツイッターハッシュタグ集計
## 概要
TwitterAPIのスタンダードプランでハッシュタグの件数やユーザ数を集計する．
*ライブラリには，tweepyを使ってます
(期間は1週間前まで．またリクエスト制限があるので3sに一回のリクエストになるので結果が出るまでが遅いです．）

## 環境構築
#### 必要なライブラリのインストール
```
git clone [URL]
cd twitter_hashtag_research
virtualenv venv
source venv/bin/activate
(vevn) pip install -r requirements.txt
```

#### ツイッターAPIの各種キーが必要です.
1. secret.py ファイルを作成．
2. 以下のフォーマットにわせて作成．

```
auth_data = {
    "access_token"        : "xxxxxxxxxxxxx",
    "access_token_secret" : "xxxxxxxxxxxxx",
    "consumer_key"        : "xxxxxxxxxxxxx",
    "consumer_secret"     : "xxxxxxxxxxxxx"
}
```

## Output
```
% python research.py "#DbD"
############### sesarch keyword
-> "#DbD"
############### term
2020-12-28 14:08:42 -> 2021-01-05 09:42:08
############### tweet count
-> 21853
############### user count
-> 9379

% python research.py "#DbD初心者"
############### sesarch keyword
-> "#DbD初心者"
############### term
2020-12-28 15:15:06 -> 2021-01-05 09:07:13
############### tweet count
-> 539
############### user count
-> 259
```