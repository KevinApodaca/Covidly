#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:39:22 2020

@author: xavier
"""

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

    
## Fields in Day object
#  from fields = today.keys()

# date :  20201103
# state :  TX
# positive :  916773
# probableCases :  None
# negative :  7412096
# pending :  None
# totalTestResultsSource :  posNeg
# totalTestResults :  8328869
# hospitalizedCurrently :  5936
# hospitalizedCumulative :  None
# inIcuCurrently :  1734
# inIcuCumulative :  None
# onVentilatorCurrently :  None
# onVentilatorCumulative :  None
# recovered :  792286
# dataQualityGrade :  A
# lastUpdateEt :  11/2/2020 19:10
# dateModified :  2020-11-02T19:10:00Z
# checkTimeEt :  11/02 14:10
# death :  18194
# hospitalized :  None
# dateChecked :  2020-11-02T19:10:00Z
# totalTestsViral :  8328869
# positiveTestsViral :  None
# negativeTestsViral :  None
# positiveCasesViral :  916773
# deathConfirmed :  None
# deathProbable :  None
# totalTestEncountersViral :  None
# totalTestsPeopleViral :  None
# totalTestsAntibody :  491876
# positiveTestsAntibody :  48506
# negativeTestsAntibody :  None
# totalTestsPeopleAntibody :  None
# positiveTestsPeopleAntibody :  None
# negativeTestsPeopleAntibody :  None
# totalTestsPeopleAntigen :  None
# positiveTestsPeopleAntigen :  None
# totalTestsAntigen :  353605
# positiveTestsAntigen :  29373
# fips :  48
# positiveIncrease :  7516
# negativeIncrease :  29650
# total :  8328869
# totalTestResultsIncrease :  37166
# posNeg :  8328869
# deathIncrease :  97
# hospitalizedIncrease :  0
# hash :  9ac9254e2934dc683a3630f6ffaa028087fb07a5
# commercialScore :  0
# negativeRegularScore :  0
# negativeScore :  0
# positiveScore :  0
# score :  0
# grade :  