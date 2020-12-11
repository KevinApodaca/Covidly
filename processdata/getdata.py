""" Covidly Project
    CS 4390: Information Retrieval
    @Team 2
    Description: This file is used to scrape the latest COVID data from the Johns Hopkins CSSE repository as well as the Our World In Data and The New York Times.
"""
import requests
import json
import datetime
import requests
import platform
import pandas as pd
from apis import covid_daily_api

# Global access key for flights API
access_key = 'bd38baa42e7b653f74bd94cc7b69e4ee'

# Just changes the format of datetime depending on which OS you're on. Otherwise more bugs to fix and we don't like that.
if platform.system() == 'Linux':
    STRFTIME_DATA_FRAME_FORMAT = '%-m/%-d/%y'
elif platform.system() == 'Windows':
    STRFTIME_DATA_FRAME_FORMAT = '%#m/%#d/%y'
else:
    STRFTIME_DATA_FRAME_FORMAT = '%-m/%-d/%y'

# This method fetches the daily report of COVID cases from CSSE, these are global classes. To fetch just U.S cases we can switch the report_directory to get 'csse_covid_19_daily_reports_us'.csse_covid_19_daily_reports. Stores data as a CSV file of new cases.
def daily_report(date_string=None):
    report_directory = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

    if date_string is None:
        yesterday = datetime.date.today() - datetime.timedelta(days=2)
        file_date = yesterday.strftime('%m-%d-%Y')
    else:
        file_date = date_string

    df = pd.read_csv(report_directory + file_date + '.csv', dtype={"FIPS": str})
    return df

# This method fetches the daily reported cases by the date. Currently using a global filter so we are getting all the data.
def daily_confirmed():
    df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
    return df

# This method fetches the daily reported deaths by the date.. Currently using a global filter so we are getting all the data.
def daily_deaths():
    df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
    return df

# This method fetches a time-series data table of total confirmed cases. This is also global.
def confirmed_report():
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    return df

# This method fetches a time-series data table of total deaths. This is also by global scope.
def deaths_report():
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    return df

# This method fetches a time-series data table of total recovered cases. Global scope.
def recovered_report():
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    return df

"""
**Work in Progress**
    Description: This is supposed to bring together and consolidate all reports and generates a time series. Shows columns based on state,country, latitude, and longitude.
    Args:
        date_string: must use following date formatting '6/10/20'.
        weekly: a boolean, which returns data frame (df) for last 8 weeks.
        monthly: boolean, which returns data frame (df) for last 3 months.
"""
def realtime_growth(date_string=None, weekly=False, monthly=False):
    df1 = confirmed_report()[confirmed_report().columns[4:]].sum()
    df2 = deaths_report()[deaths_report().columns[4:]].sum()
    df3 = recovered_report()[recovered_report().columns[4:]].sum()

    growth_df = pd.DataFrame([])
    growth_df['Confirmed'], growth_df['Deaths'], growth_df['Recovered'] = df1, df2, df3
    growth_df.index = growth_df.index.rename('Date')

    yesterday = pd.Timestamp('now').date() - pd.Timedelta(days=1)

    if date_string is not None:
        return growth_df.loc[growth_df.index == date_string]

    if weekly is True:
        weekly_df = pd.DataFrame([])
        intervals = pd.date_range(end=yesterday, periods=8, freq='7D').strftime(STRFTIME_DATA_FRAME_FORMAT).tolist()
        for day in intervals:
            weekly_df = weekly_df.append(growth_df.loc[growth_df.index==day])
        return weekly_df

    elif monthly is True:
        monthly_df = pd.DataFrame([])
        intervals = pd.date_range(end=yesterday, periods=3, freq='1M').strftime(STRFTIME_DATA_FRAME_FORMAT).tolist()
        for day in intervals:
            monthly_df = monthly_df.append(growth_df.loc[growth_df.index==day])
        return monthly_df

    return growth_df

# This method calculates a percentage of change of the trends frontend component. Compares last week to this week.
def percentage_trends():
    current = realtime_growth(weekly=True).iloc[-1]
    last_week = realtime_growth(weekly=True).iloc[-2]
    trends = round(number=((current - last_week)/last_week)*100, ndigits=1)
    rate_change = round(((current.Deaths/current.Confirmed)*100)-((last_week.Deaths / last_week.Confirmed)*100), ndigits=2)
    trends = trends.append(pd.Series(data=rate_change, index=['Death_rate']))

    return trends

# This method generates the sortable table for the frontend that shows stats of all countries.
def global_cases():
    df = daily_report()[['Country_Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    df.rename(columns={'Country_Region':'Country'}, inplace=True)
    df = df.groupby('Country', as_index=False).sum()
    df.sort_values(by=['Confirmed'], ascending=False, inplace=True)

    return df

# This method fetches live data of the United States and filters by the county level (per 100000 people). Will be used for the 'Choosing State' frontend component of covidly dashboard page.
def usa_counties():
    populations = pd.read_csv('https://raw.githubusercontent.com/balsama/us_counties_data/master/data/counties.csv')[['FIPS Code', 'Population']]
    populations.rename(columns={'FIPS Code': 'fips'}, inplace=True)
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv', dtype={"fips": str}).iloc[:,:6]
    df = pd.merge(df, populations, on='fips')
    df['cases/capita'] = (df.cases / df.Population)*100000

    return df

# Retrieve data for arrival flights at airport
def arrivals(iata):
    params = {
        'access_key': access_key,
        'arr_iata': iata
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    flights_df = {'arrival' : []}
    for flight in api_response['data']:
        flights_df['arrival'].append(flight['departure']['airport'])
    return flights_df

# Retrieve data for departing flights at airport
def departures(iata):
    params = {
        'access_key': access_key,
        'dep_iata': iata
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    flights_df = {'departure' : []}
    for flight in api_response['data']:
        flights_df['departure'].append(flight['arrival']['airport'])
    return flights_df

# Retrieve data for arrivals/departing airport returns dataframe
def airport(city, iata):
    arrivalSources = arrivals(iata)
    departureDestinations = departures(iata)
    flights_df = {'city': []}

    flights_df.update(arrivalSources)
    flights_df.update(departureDestinations)

    if len(arrivalSources['arrival']) > len(departureDestinations['departure']):
        flights_df.update({'city': ([city]*len(arrivalSources['arrival']))})
        flights_df.update({'departure': (flights_df['departure'] + ([None] * (len(flights_df['arrival']) - len(flights_df['departure']))))})

    elif len(arrivalSources['arrival']) < len(departureDestinations['departure']):
        flights_df.update({'city': ([city]*len(departureDestinations['departure']))})
        flights_df.update({'arrival': (flights_df['arrival'] + ([None] * (len(flights_df['departure']) - len(flights_df['arrival']))))})

    else:
        flights_df.update({'city': ([city]*len(arrivalSources['arrival']))})
    return pd.DataFrame(flights_df)

# Returns dataframe of all supported cities
def supportedAirports():
    supportedList = {'El Paso': ['ELP'], 'San Antonio': ['SAT'], 'Dallas': ['DAL', 'DFW'], 'Austin': ['AUS'], 'Houston': ['HOU'], 'Fort Worth': ['FTW', 'AFW'], 'Corpus Christi': ['CRP'], 'Laredo': ['LRD'], 'Lubbock': ['LBB'], 'Amarillo': ['AMA']}
    frames = []
    for city in supportedList:
        for currentAirport in supportedList[city]:
            current = airport(city, currentAirport)
            frames.append(current)
    return pd.concat(frames)

# Return a df containing number of arrivals and departures from/to TX
def flight_numbers():
    df = supportedAirports()
    arrivals = 0
    departures = 0
    for index, row in df.iterrows():
        if row['arrival'] is not None:
            arrivals = arrivals + 1
        if row['departure'] is not None:
            departures = departures + 1

    flights = {'arrivals': [arrivals], 'departures': [departures]}
    dataframe = pd.DataFrame(data=flights)
    return dataframe

#Obtain list of articles from News API
def news_articles():
    endpoint = 'http://newsapi.org/v2/top-headlines?'
    params = {
        'country': 'us',
		'category': 'health',
		'sortBy': 'popularity',
		'apiKey': '265a30250d594634a08e9b722f993b41'
        }

    response = requests.get(endpoint, params=params)
    news_data = response.json()
    articles = news_data['articles']
    articles = articles[:6]
    df = pd.DataFrame(articles, columns=['title', 'description', 'url', 'urlToImage'])
    return df

def top_states():
    TXCases, TXDates = covid_daily_api.getMonthlyCases("texas")
    CACases, CADates = covid_daily_api.getMonthlyCases("california")
    NYCases, NYDates = covid_daily_api.getMonthlyCases("new york")
    UTCases, UTDates = covid_daily_api.getMonthlyCases("utah")
    FLCases, FLDates = covid_daily_api.getMonthlyCases("florida")
    return createFigure(TXCases,TXDates,CACases,CADates,NYCases,NYDates,UTCases,UTDates,FLCases,FLDates)

def fixAxis(TXCases,TXDates,CACases,CADates,NYCases,NYDates,UTCases,UTDates,FLCases,FLDates):
    for i in range(len(TXDates)):
        monthStr =str(TXDates[i])[:2]
        dayStr = str(TXDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        TXDates[i] = result

        monthStr =str(CADates[i])[:2]
        dayStr = str(CADates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        CADates[i] = result

        monthStr =str(NYDates[i])[:2]
        dayStr = str(NYDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        NYDates[i] = result

        monthStr =str(UTDates[i])[:2]
        dayStr = str(UTDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        UTDates[i] = result

        monthStr =str(FLDates[i])[:2]
        dayStr = str(FLDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        FLDates[i] = result

def createFigure(TXCases,TXDates,CACases,CADates,NYCases,NYDates,UTCases,UTDates,FLCases,FLDates):
    day = (int(datetime.today().strftime("%d")) - 1)
    fixAxis(TXCases,TXDates,CACases,CADates,NYCases,NYDates,UTCases,UTDates,FLCases,FLDates)

    StateGraph = go.Figure()
    StateGraph.add_trace(go.Scatter(x = TXDates[::-1], y = TXCases[::-1], mode = "lines+markers", name = "Texas", visible= True, line= dict(color = "red"))) # Texas
    StateGraph.add_trace(go.Scatter(x = CADates[::-1], y = CACases[::-1], mode = "lines+markers", name = "California", visible = False, line= dict(color = "blue"))) # California
    StateGraph.add_trace(go.Scatter(x = NYDates[::-1], y = NYCases[::-1], mode = "lines+markers", name = "New York", visible = False, line= dict(color = "orange"))) # New York
    StateGraph.add_trace(go.Scatter(x = UTDates[::-1], y = UTCases[::-1], mode = "lines+markers", name = "Utah", visible = False, line= dict(color = "purple"))) # Utah
    StateGraph.add_trace(go.Scatter(x = FLDates[::-1], y = FLCases[::-1], mode = "lines+markers", name = "Florida", visible = False, line= dict(color = "green"))) # Florida

    StateGraph.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                active=0,
                x=0.57,
                y=1.2,
                buttons=list([
                    dict(label="Texas",
                         method="update",
                         args=[{"visible": [True,False,False,False,False]},
                               {"title": "Texas Active Cases",
                                "annotations": []}]),
                    dict(label="California",
                         method="update",
                         args=[{"visible": [False,True,False,False,False]},
                               {"title": "California Active Cases",
                                "annotations": []}]),
                    dict(label="New York",
                         method="update",
                         args=[{"visible":[False,False,True,False,False]},
                               {"title": "New York Active Cases",
                                "annotations": []}]),
                    dict(label="Utah",
                         method="update",
                         args=[{"visible": [False,False,False,True,False] },
                               {"title": "Utah Active Cases",
                                "annotations": []}]),
                    dict(label="Florida",
                         method="update",
                         args=[{"visible":[False,False,False,False,True] },
                               {"title": "Florida Active Cases",
                                "annotations": []}]),
                    dict(label="All",
                         method="update",
                         args=[{"visible":[True,True,True,True,True]},
                               {"title": "States Active Cases",
                                "annotations": []}]),
                ]),
            )
        ])
    return StateGraph
