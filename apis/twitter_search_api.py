#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

endpoint="https://api.twitter.com/2/tweets/search/recent?query=covid-19&tweet.fields=created_at,author_id,lang,context_annotations&max_results=100"
headers = {"Authorization": "Bearer <Your Token Here>"}

res = requests.get(endpoint,headers=headers)

twitter = json.loads(res.content)
tweet=twitter['data'][0]

fields=tweet.keys()
print(fields)
print()

for key in fields:
    print(key,":",tweet[key])
    print()
    
## Documention on query params/additional fields

#https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
#https://developer.twitter.com/en/docs/twitter-api/fields
#https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
#https://developer.twitter.com/en/docs/twitter-api/expansions
