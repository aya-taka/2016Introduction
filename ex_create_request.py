import ex_accesskey
import requests
import json


#   API
#   key:アクセスキー
#   url:その接続で用いるWebAPIのURL
#   language:入力された言語
#               0:日本語   1:それ以外
class API:
    def __init__(self, lang):
        self.key = ex_accesskey.keyid
        self.json_default = 0
        self.json_dic = 0
        if lang == 0:       # 日本語
            self.url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
            self.language = 0
        elif lang == 1:     # 英語
            self.url = "http://api.gnavi.co.jp/ForeignRestSearchAPI/20150630/"
            self.language = 1
        else:               # デフォルトは日本語
            self.url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
            self.language = 0

    def get_json(self, query):
        self.json_default = requests.get(self.url, params=query)
        #   jsonを辞書型で読み込みなおす
        self.json_dic = json.loads(json.dumps(self.json_default.json(), sort_keys=True, indent=2))
        #   print(self.json_dic)
        #   self.get_name()
        return self.json_dic

    def get_name(self):
        if self.language == 0:
            data = []
            for var in self.json_dic["rest"]:
                data.append(var["name"])
            return data
        elif self.language == 1:
            data = []
            for var in self.json_dic["rest"]:
                data.append(var["name"]["name"])
            return data
        else:
            pass