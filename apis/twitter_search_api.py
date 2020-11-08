#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json


endpoint="https://api.twitter.com/2/tweets/search/recent?query=covid-19&tweet.fields=created_at,author_id,lang,context_annotations&max_results=100"
headers = {"Authorization": "Bearer (token)"}

res = requests.get(endpoint,headers=headers)

twitter = json.loads(res.content)
tweet=twitter['data'][0]

fields=tweet.keys()
print(fields)
print()

for key in fields:
    print(key,":",tweet[key])
    print()