# -*- coding: utf-8 -*-
import sys
import json
import requests
import re
#   アクセスキーを記述したファイルをインポート
#   ファイル名：ex_accesskey.py
#   定義：
#   key:(文字列)アクセスキー
import ex_accesskey
#   リクエストの作成を記述したファイルをインポート
#   ファイル名：ex_create_request.py
#   定義
#   クラス　API
#   init()  言語を指定し、キーIDとURLを指定
#   get_json()  json形式のデータの取得
#   get_name()  json形式のデータからname要素を抽出
import ex_create_request
#   検索対象文字列の読み込み
#   フリーワード検索に使用
word = input("検索キーワードをスペース区切りで入力してください：")
#   文字種識別
#   アルファベットかどうかのみ？
regexp = re.compile(r'^[0-9A-Za-z]+$')
#   print("".join(word.split()))
result = regexp.search("".join(word.split()))
if result != None:
    request_url = ex_create_request.API(1)
    #   print(1)
else:
    request_url = ex_create_request.API(0)
    #   print(0)

#   リクエストの作成
#   帰ってくる件数はデフォルト10件
query = {
    "format": "json",
    "keyid": request_url.key,
}
query["freeword"] = word
#   リクエストを送信し、json形式を取得
request_url.get_json(query)

#   print("r:{0}".format(r))
#   出力
#   rest以下の内容を対象にnameの中身を出力
for data in request_url.get_name():
    print("レストラン名:{0}".format(data))