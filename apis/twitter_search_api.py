#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

default_query='covid'
arg_names={'fields':"&tweet.fields="
           ,'expansions':"&expansions="
           ,'user':'&user.fields='
           ,'tweets':'ids='}
default_fields=['created_at','author_id','lang','possibly_sensitive']
default_expansions=['referenced_tweets.id','author_id']#author_id necessary here as well to retrieve author info
default_user=['name','username']
token= ''
results='100'
headers = {"Authorization": "Bearer " + token}
base_endpoint="https://api.twitter.com/2/tweets/search/recent?query="
oembed_endpoint="https://publish.twitter.com/oembed?url=https://twitter.com/"
dark_mode="&theme=dark"

#currently removes retweets, sensitive tweets, and non-english tweets - can be modified to remove quotes and replies
def filter_tweet(tweet):
    t_fields = tweet.keys()
    is_retweet = False
    if('referenced_tweets' in t_fields):
        for rt in tweet['referenced_tweets']:
            if(rt['type']=='retweeted'):
                    is_retweet = True
                    break
    is_sensitive = False
    if('possibly_sensitive' in t_fields):
        is_sensitive = tweet['possibly_sensitive']
    return (not is_retweet) and (not is_sensitive) and (tweet['lang']=='en')

def parse_query_args(arglist,type='fields'):
    if(arglist is None or len(arglist)==0):
        return ''
    if(type=='expansions' and ('referenced_tweets.id' not in arglist)):
        arglist.apend('referenced_tweets.id')
    q_arg=arg_names[type]
    for arg in arglist:
        q_arg=q_arg+arg+','
    return q_arg[:len(q_arg)-1]

def fetch_tweets(query=default_query,fields=default_fields,expansions=default_expansions,user=default_user,q_results=results,mode="light"):
    q_text=query
    q_fields=parse_query_args(fields)
    q_expansions=parse_query_args(expansions,'expansions')
    q_user=parse_query_args(user,'user')
    endpoint=base_endpoint+q_text+q_fields+q_expansions+q_user+"&max_results="+q_results
    res = requests.get(endpoint,headers=headers)
    twitter = json.loads(res.content)
    tweets=twitter['data']
    #fields for user are sent seperately so adding them to dicts is necessary to access later
    users={}
    for u in twitter['includes']['users']:
        users[u['id']]=u
    
    ref_tweets=set()
    final_tweets=[]
    for t in tweets:
        #extract retweets
        if('referenced_tweets' in t.keys()):
            for rt in t['referenced_tweets']:
                if(rt['type']=='retweeted' and rt['id'] not in ref_tweets):
                    ref_tweets.add(rt['id'])
        if(filter_tweet(t)):
            #add missing fields from user
            author_info=users[t['author_id']]
            for ak in author_info.keys():
                t['author_'+ak]=author_info[ak]
            final_tweets.append(t)
    #fetch tweets that were retweeted
    q_retweets=parse_query_args(ref_tweets,'tweets')
    rt_endpoint="https://api.twitter.com/2/tweets?"+q_retweets+q_fields+q_expansions+q_user
    rt_res = requests.get(rt_endpoint,headers=headers)
    rt_twitter=json.loads(rt_res.content)
    retweets=rt_twitter['data']
    #same process to extract users as above
    for u in rt_twitter['includes']['users']:
        users[u['id']]=u

    for t in retweets:
        if(filter_tweet(t)):
            author_info=users[t['author_id']]
            for ak in author_info.keys():
                t['author_'+ak]=author_info[ak]
            final_tweets.append(t)
    
    if(mode=="dark"):
        oe_mode=dark_mode
    else:
        oe_mode=""
    
    for t in final_tweets:
        oe_endpoint = oembed_endpoint+t['author_username']+'/status/'+t['id']+oe_mode
        res = requests.get(oe_endpoint,headers=headers)
        embed = json.loads(res.content)
        t_fields = t.keys()
        for k in t.copy().keys():
            if(k!='created_at'):
                t.pop(k)
        t['oembed']=embed['html']
        
    

    return sorted(final_tweets,key=lambda t:t['created_at'],reverse=True)
