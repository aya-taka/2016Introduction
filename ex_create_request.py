import ex_accesskey


# エンドポイントURL
class API:
    def __init__(self, lang):
        self.key = ex_accesskey.keyid
        if lang == 0:       # 日本語
            self.url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
        elif lang == 1:     # 英語
            self.url = "http://api.gnavi.co.jp/ForeignRestSearchAPI/20150630/"
        else:               # デフォルトは日本語
            self.url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"