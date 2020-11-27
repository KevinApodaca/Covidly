import requests
import json


# location given here 
location = "University of Texas at El Paso"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

### US INFO ### 

# api-endpoint 
URL_US = 'https://api.covidtracking.com/v1/us/daily.json'

# sending get request and saving the response as response object 
US = requests.get(url = URL_US, params = PARAMS) 
# extracting data in json format 
dataUS = US.json() 

# This methods returns the date of the information retreived from the following methods 
def date_us():
	return dataUS[0]['date']

# This method returns the positive cases in US
def pos_cases_us():
	return dataUS[0]['positive']
# This method returns the increase in the positive cases in the US (day to day)
def pos_increase_us():
	return dataUS[0]['positiveIncrease']
# This method returns the negative cases in US
def neg_cases_us():
	return dataUS[0]['negative']
# This method returns the recovered cases in US
def recov_cases_us():
	return dataUS[0]['recovered']
#This method returns the number of pending results in the US
def pending_us():
	return dataUS[0]['pending']
# This method returns the total deaths in US
def deaths_us():
	return dataUS[0]['death']
# This method returns the increase in deaths in US (day to day)
def deaths_increase_us():
	return dataUS[0]['deathIncrease']
# This method returns the current hospitalized people in US
def currHospitalized_us():
	 return dataUS[0]['hospitalizedCurrently']
 #This method returns the current people in ICU in US
def currInIcu_us():
	 return dataUS[0]['inIcuCurrently']

### STATES INFO ### 

# api-endpoint 
URL_texas = "https://api.covidtracking.com/v1/states/tx/daily.json"
URL_california ='https://api.covidtracking.com/v1/states/ca/daily.json'
URL_newYork = 'https://api.covidtracking.com/v1/states/ny/daily.json'
URL_florida = 'https://api.covidtracking.com/v1/states/fl/daily.json'
URL_utah = 'https://api.covidtracking.com/v1/states/ut/daily.json'

 
# sending get request and saving the response as response object 
TX = requests.get(url = URL_texas, params = PARAMS) 
CA = requests.get(url = URL_california, params = PARAMS)  
NY = requests.get(url = URL_newYork, params = PARAMS)
FL = requests.get(url = URL_florida, params = PARAMS)
UT = requests.get(url = URL_utah, params = PARAMS)
# extracting data in json format 
dataTX = TX.json() 
dataNY = NY.json()
dataCA = CA.json()
dataFL = FL.json()
dataUT = UT.json() 
#data[0] is the most recent data collected


# This methods returns the date of the information retreived from the following methods 
def stateDateRetreived(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['date']
	if state == "new york":
		return dataNY[0]['date']
	if state == "california":
		return dataCA[0]['date']
	if state == "florida":
		return dataFL[0]['date']
	if state == "utah":
		return dataUT[0]['date']

# This method returns the last updated information of the state of texas in ET 
def stateLastUpdated(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['lastUpdateEt']
	if state == "new york":
		return dataNY[0]['lastUpdateEt']
	if state == "california":
		return dataCA[0]['lastUpdateEt']
	if state == "florida":
		return dataFL[0]['lastUpdateEt']
	if state == "utah":
		return dataUT[0]['lastUpdateEt']

# This method returns the positive cases in the state 
def statePostiveCases(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['positive']
	if state == "new york":
		return dataNY[0]['positive']
	if state == "california":
		return dataCA[0]['positive']
	if state == "florida":
		return dataFL[0]['positive']
	if state == "utah":
		return dataUT[0]['positive']

# This method returns the increase in positive cases in the state
def statePostiveIncrease(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['positiveIncrease']
	if state == "new york":
		return dataNY[0]['positiveIncrease']
	if state == "california":
		return dataCA[0]['positiveIncrease']
	if state == "florida":
		return dataFL[0]['positiveIncrease']
	if state == "utah":
		return dataUT[0]['positiveIncrease']

# This method returns the negative cases in the state
def stateNegativeCases(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['negative']
	if state == "new york":
		return dataNY[0]['negative']
	if state == "california":
		return dataCA[0]['negative']
	if state == "florida":
		return dataFL[0]['negative']
	if state == "utah":
		return dataUT[0]['negative']

# This method returns the recovered cases in the state
def stateRecoveredCases(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['recovered']
	if state == "new york":
		return dataNY[0]['recovered']
	if state == "california":
		return dataCA[0]['recovered']
	if state == "florida":
		return dataFL[0]['recovered']
	if state == "utah":
		return dataUT[0]['recovered']

#This method returns the total deaths in the state
def stateDeaths(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['death']
	if state == "new york":
		return dataNY[0]['death']
	if state == "california":
		return dataCA[0]['death']
	if state == "florida":
		return dataFL[0]['death']
	if state == "utah":
		return dataUT[0]['death']
 #This method returns the increase in deaths in the state
def stateDeathsIncrease(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['deathIncrease']
	if state == "new york":
		return dataNY[0]['deathIncrease']
	if state == "california":
		return dataCA[0]['deathIncrease']
	if state == "florida":
		return dataFL[0]['deathIncrease']
	if state == "utah":
		return dataUT[0]['deathIncrease']
# This method returns the current hospitalized people in the state
def stateCurrHospitalized(state):
	state.lower()
	if state == "texas":
		return dataTX[0]['hospitalizedCurrently']
	if state == "new york":
		return dataNY[0]['hospitalizedCurrently']
	if state == "california":
		return dataCA[0]['hospitalizedCurrently']
	if state == "florida":
		return dataFL[0]['hospitalizedCurrently']
	if state == "utah":
		return dataUT[0]['hospitalizedCurrently']




def getMonthlyCases(state):
    stateDailyCases = []
    stateDates = []
    if state.lower() == "texas":
        for i in range(0,31):
            stateDailyCases.append(dataTX[i]['hospitalizedCurrently'])
            stateDates.append(dataTX[i]['date'] % 10000)

    if state.lower() == "new york":
        for i in range(0,31):
            stateDailyCases.append(dataNY[i]['hospitalizedCurrently'])
            stateDates.append(dataNY[i]['date'] % 10000)

    if state.lower() == "california":
        for i in range(0,31):
            stateDailyCases.append(dataCA[i]['hospitalizedCurrently'])
            stateDates.append(dataCA[i]['date'] %10000)

    if state.lower() == "florida":
        for i in range(0,31):
            stateDailyCases.append(dataFL[i]['hospitalizedCurrently'])
            stateDates.append(dataFL[i]['date'] %10000)

    if state.lower() == "utah":
        for i in range(0,31):
            stateDailyCases.append(dataUT[i]['hospitalizedCurrently'])
            stateDates.append(dataUT[i]['date'] %10000)
    return stateDailyCases, stateDates




# DELETE THIS AFTER FINSISHED TESTING
# print("Texas: ", getMonthlyCases("texas"))
# print("__________________________________________")
# print("California: ", getMonthlyCases("california"))
# print("__________________________________________")
# print("New York: ", getMonthlyCases("NEW YORK"))
# print("__________________________________________")
# print("Utah: ", getMonthlyCases("utaH"))
# print("__________________________________________")
# print("Florida: ", getMonthlyCases("Florida"))
# print("__________________________________________")


# state="tx"
# endpoint='https://api.covidtracking.com/v1/states/'

# #fetch/process daily info for state
# res = requests.get(endpoint+state+'/daily.json')
# covid_daily = json.loads(res.content)

# today=covid_daily[0]

# print('## Info about today\n')
# print('Today\'s Date:',today['date'])
# print('Number of Positive Cases:',today['positive'],"cases")
# print('Patients Hospitalized:',today['hospitalizedCurrently'],"patients")
# print('Death Toll:',today['death'],"deaths")
# print('Increase in positive cases:',today['positiveIncrease'],"new cases")
# print('Increase in reported deaths:',today['deathIncrease'],"new deaths")
