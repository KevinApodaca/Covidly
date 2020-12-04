# importing the requests library 
import requests
# importing the pandas Library 
import pandas as pd

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

# This methods returns the date of the information retrieved from the following methods 
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
statesDict = {'texas':dataTX[0],'new york': dataNY[0],'california': dataCA[0],'florida': dataFL[0],'utah': dataUT[0] }

# This methods returns the date of the information retrieved from the following methods 
def stateDateRetrieved(state):
	state = state.lower()
	return statesDict[state]['date']

# This method returns the last updated information of the state of texas in ET 
def stateLastUpdated(state):
	state = state.lower()
	return statesDict[state]['lastUpdateEt']

# This method returns the positive cases in the state 
def statePostiveCases(state):
	state = state.lower()
	return statesDict[state]['positive']

# This method returns the increase inpositive cases in the state
def statePostiveIncrease(state):
	state = state.lower()
	return statesDict[state]['positiveIncrease']

# This method returns the negative cases in the state
def stateNegativeCases(state):
	state = state.lower()
	return statesDict[state]['negative']

# This method returns the recovered cases in the state
def stateRecoveredCases(state):
	state = state.lower()
	return statesDict[state]['recovered']
   
#This method returns the total deaths in the state
def stateDeaths(state):
	state = state.lower()
	return statesDict[state]['death']
    
 #This method returns the increase in deaths in the state
def stateDeathsIncrease(state):
	state = state.lower()
	return statesDict[state]['deathIncrease']

# This method returns the current hospitalized people in the state
def stateCurrHospitalized(state):
	state = state.lower()
	return statesDict[state]['hospitalizedCurrently']


counties = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
## counties['date','county','state','fips','cases','deaths']

# This method returns the positive cases in the county. Works for any County in the US.
def casesCounty(countyP, stateP): # it takes in two parameters the county's name and the state's name
    findRecentDate = counties[-1:]['date']
    recentDate = findRecentDate.values[0]
    res = counties.loc[ (counties['county'] == countyP) & (counties['state'] == stateP) & ((counties['date']) == recentDate) ]
    return res['cases'].values[0]

# This method returns the deathss in the county. Works for any County in the US. NOTE: Needs to be tested
def deathsCounty(countyP, stateP): # it takes in two parameters the county's name and the state's name
    findRecentDate = counties[-1:]['date']
    recentDate = findRecentDate.values[0]
    res = counties.loc[ (counties['county'] == countyP) & (counties['state'] == stateP) & ((counties['date']) == recentDate) ]
    return res['deaths'].values[0]

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
