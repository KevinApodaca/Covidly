# -*- coding: utf-8 -*-
import requests
import pandas as pd

#Retrieve data for arrival flights at airport
def arrivals(iata):
    params = {
        'access_key': 'XXXXXXXXXXXXXXXXX',
        'arr_iata': iata
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    df = {'arrival' : []}
    for flight in api_response['data']:
        df['arrival'].append(flight['departure']['airport'])
    return df

#Retrieve data for departing flights at airport
def departures(iata):
    params = {
        'access_key': 'XXXXXXXXXXXXXXXXX',
        'dep_iata': iata
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    df = {'departure' : []}
    for flight in api_response['data']:
        df['departure'].append(flight['arrival']['airport'])
    return df

#Retrieve data for arrivals/departing airport returns dataframe
def airport(city, iata):
    arrivalSources = arrivals(iata)
    departureDestinations = departures(iata)
    df = {'city': []}

    df.update(arrivalSources)
    df.update(departureDestinations)
    
    if len(arrivalSources['arrival']) > len(departureDestinations['departure']):
        df.update({'city': ([city]*len(arrivalSources['arrival']))})
        df.update({'departure': (df['departure'] + ([None] * (len(df['arrival']) - len(df['departure']))))})
        
    elif len(arrivalSources['arrival']) < len(departureDestinations['departure']):
        df.update({'city': ([city]*len(departureDestinations['departure']))})
        df.update({'arrival': (df['arrival'] + ([None] * (len(df['departure']) - len(df['arrival']))))})
    
    else:
        df.update({'city': ([city]*len(arrivalSources['arrival']))})
    return pd.DataFrame(df)

#Returns dataframe of all supported cities
def supportedAirports():
    supportedList = {'El Paso': ['ELP'], 'San Antonio': ['SAT'], 'Dallas': ['DAL', 'DFW'], 'Austin': ['AUS'], 'Houston': ['HOU'], 'Fort Worth': ['FTW', 'AFW'], 'Corpus Christi': ['CRP'], 'Laredo': ['LRD'], 'Lubbock': ['LBB'], 'Amarillo': ['AMA']}
    frames = []
    for city in supportedList:
        for currentAirport in supportedList[city]:
            current = airport(city, currentAirport)
            frames.append(current)
    return pd.concat(frames)
    
