#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

q_text='covid'
arg_names={'fields':"&tweet.fields="
           ,'expansions':"&expansions="
           ,'user':'&user.fields='
           ,'tweets':'ids='}
default_fields=['created_at','author_id','lang','attachments']
default_expansions=['referenced_tweets.id','geo.place_id','author_id']
default_user=['name','username','profile_image_url']
token= ''
results='100'
headers = {"Authorization": "Bearer " + token}
base_endpoint="https://api.twitter.com/2/tweets/search/recent?query="

def filter_tweet(tweet):
    t_fields = tweet.keys()
    return not ('referenced_tweets') in t_fields and (tweet['lang']=='en')

def parse_query_args(arglist,type='fields'):
    if(arglist is None or len(arglist)==0):
        return ''
    if(type=='expansions' and ('referenced_tweets.id' not in arglist)):
        arglist.apend('referenced_tweets.id')
    q_arg=arg_names[type]
    for arg in arglist:
        q_arg=q_arg+arg+','
    return q_arg[:len(q_arg)-1]

def fetch_tweets(fields=default_fields,expansions=default_expansions,user=default_user,q_results=results):
    q_fields=parse_query_args(fields)
    q_expansions=parse_query_args(expansions,'expansions')
    q_user=parse_query_args(user,'user')
    endpoint=base_endpoint+q_text+q_fields+q_expansions+q_user+"&max_results="+q_results
    res = requests.get(endpoint,headers=headers)
    twitter = json.loads(res.content)
    tweets=twitter['data']
    #fields for user and places is sent seperately so adding them to dicts is necessary to access it later
    users={}
    for u in twitter['includes']['users']:
        users[u['id']]=u
    places={}
    if('places' in twitter['includes'].keys()):
        for p in twitter['includes']['places']:
            places[p['id']]=p
    
    ref_tweets=set()
    final_tweets=[]
    for t in tweets:
        #extract retweets
        if('referenced_tweets' in t.keys()):
            for rt in t['referenced_tweets']:
                if(rt['type']=='retweeted' and rt['id'] not in ref_tweets):
                    ref_tweets.add(rt['id'])
        if(filter_tweet(t)):
            #add missing fields from user and places
            if('geo' in t.keys()):
                place_info=places[t['geo']['place_id']]
                for pk in place_info.keys():
                    t['geo'+pk]=place_info[pk]
            author_info=users[t['author_id']]
            for ak in author_info.keys():
                t[ak]=author_info[ak]
            final_tweets.append(t)
    #fetch tweets that were retweeted
    q_retweets=parse_query_args(ref_tweets,'tweets')
    rt_endpoint="https://api.twitter.com/2/tweets?"+q_retweets+q_fields+q_expansions+q_user
    rt_res = requests.get(rt_endpoint,headers=headers)
    rt_twitter=json.loads(rt_res.content)
    retweets=rt_twitter['data']
    for u in rt_twitter['includes']['users']:
        users[u['id']]=u
    if('places' in rt_twitter['includes'].keys()):
        for p in rt_twitter['includes']['places']:
            places[p['id']]=p

    for t in retweets:
        if(filter_tweet(t)):
            if('geo' in t.keys()):
                place_info=places[t['geo']['place_id']]
                for pk in place_info.keys():
                    t['geo'+pk]=place_info[pk]
            author_info=users[t['author_id']]
            for ak in author_info.keys():
                t[ak]=author_info[ak]
            final_tweets.append(t)

    return sorted(final_tweets,key=lambda t:t['created_at'])
