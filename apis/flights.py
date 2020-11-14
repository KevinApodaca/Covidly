# -*- coding: utf-8 -*-
import requests

#Retrieve data for arrival flights at airport
def arrivals(iata):
    params = {
        'access_key': 'XXXXXXXXXX',
        'arr_iata': iata
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    return api_response['data']

#Retrieve data for departing flights at airport
def departures(iata):
    params = {
        'access_key': '29a2ab9c0a0625c6a59aaa327eb291d7',
        'dep_iata': iata
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    return api_response['data']

#Retrieve data for arrivals/departing airport returns dictioaries of departures and arrivals
def airport(iata):
    outgoing = []
    for flights in departures(iata):
        outgoing.append([flights['departure'], flights['arrival']])
    inbound = []
    for flights in arrivals(iata):
        inbound.append([flights['departure'], flights['arrival']])
    return {'departures' : outgoing , 'arrivals': inbound}

#Retrieve data for ELP, DAL, AUS, DFW, SAT arrivals and departures
def texasFive(): 
    airports = ['ELP', 'DAL', 'AUS', 'DFW', 'SAT']
    results = {}
    for iata in airports:
        results.update({iata: airport(iata)})
    return results

print(texasFive())

