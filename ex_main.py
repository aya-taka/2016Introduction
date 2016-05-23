# -*- coding: utf-8 -*-
import sys
import json
import requests
#   アクセスキーを記述したファイルをインポート
#   ファイル名：ex_accesskey.py
#   定義：
#   key:アクセスキー
#   url:アクセスするURL
import ex_accesskey
#   検索対象文字列の読み込み
#   フリーワード検索に使用
word = input("検索キーワードをスペース区切りで入力してください：")
#   文字種識別
#   アルファベットかどうかのみ？
if word.isalpha():
    request_url = ex_accesskey.URL(1)
else:
    request_url = ex_accesskey.URL(0)

#   リクエストの作成
#   帰ってくる件数はデフォルト10件
query = {
    "format": "json",
    "keyid": request_url.key,
    "freeword": word,
}
#   requestsを使用して、指定URLにリクエストを送信
#   rに帰ってきた情報を格納
r = requests.get(request_url.url, params=query)
#   jsonを辞書型で読み込みなおす
r = json.loads(json.dumps(r.json(), sort_keys=True, indent=2))

#   print("r:{0}".format(r))
#   出力
#   rest以下の内容を対象にnameの中身を出力
for data in r["rest"]:
    print("レストラン名:{0}".format(data["name"]))