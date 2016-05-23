# -*- coding: utf-8 -*-
import sys
import json
import requests

import ex_accesskey

word = input().split()

query = {
    "format": "json",
    "keyid": ex_accesskey.keyid,
    "freeword": word,
    "hit_per_page": 3
}

r = requests.get(ex_accesskey.url, params=query)

print("r:{0}".format(r))
print("r.json:{0}".format(json.dumps(r.json(), sort_keys=True, indent=2)))

r.close()