import requests
import json

state="tx"
endpoint='https://api.covidtracking.com/v1/states/'

#fetch/process daily info for state
res = requests.get(endpoint+state+'/daily.json')
covid_daily = json.loads(res.content)

today=covid_daily[0]

print('## Info about today\n')
print('Today\'s Date:',today['date'])
print('Number of Positive Cases:',today['positive'],"cases")
print('Patients Hospitalized:',today['hospitalizedCurrently'],"patients")
print('Death Toll:',today['death'],"deaths")
print('Increase in positive cases:',today['positiveIncrease'],"new cases")
print('Increase in reported deaths:',today['deathIncrease'],"new deaths")
