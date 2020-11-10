# Covidly's APIs

Covidly takes advantage of four APIs to report its data - NewsAPI, Twitter, AviationStack and the Covid Tracking Project.

## News API

Covidly uses the News API, a simple HTTP REST API that retrieves live articles with endpoint options such as 'top-headlines' and 'everything.' The fields that covidly makes use of through the request are: 
 - source
 - title
 - description
 - url
 - urlToImage

More documentation on the request parameters are available here:

[Documentation](https://newsapi.org/docs)

[Top headlines](https://newsapi.org/docs/endpoints/top-headlines)

[Everything](https://newsapi.org/docs/endpoints/everything)

## Twitter API

Covidly uses Twitter's v2 API to fetch recent tweets. This endpoint require a bearer token from an approved Twitter Developer account.

More documentation on the query params are available here:

[API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)

[Tweet Fields](https://developer.twitter.com/en/docs/twitter-api/fields)

[Tweet Object Model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)

[Tweet Expansions](https://developer.twitter.com/en/do)

## Aviation Stack API

```To be filled out with Trello-15```

## Covid Tracking Project API

The Covid Tracking Project's API works through a simple GET request to the endpoint of the corresponding US state. The requested information arrives with the following fields:
```
- date :  20201103
- state :  TX
- positive :  916773
- probableCases :  None
- negative :  7412096
- pending :  None
- totalTestResultsSource :  posNeg
- totalTestResults :  8328869
- hospitalizedCurrently :  5936
- hospitalizedCumulative :  None
- inIcuCurrently :  1734
- inIcuCumulative :  None
- onVentilatorCurrently :  None
- onVentilatorCumulative :  None
- recovered :  792286
- dataQualityGrade :  A
- lastUpdateEt :  11/2/2020 19:10
- dateModified :  2020-11-02T19:10:00Z
- checkTimeEt :  11/02 14:10
- death :  18194
- hospitalized :  None
- dateChecked :  2020-11-02T19:10:00Z
- totalTestsViral :  8328869
- positiveTestsViral :  None
- negativeTestsViral :  None
- positiveCasesViral :  916773
- deathConfirmed :  None
- deathProbable :  None
- totalTestEncountersViral :  None
- totalTestsPeopleViral :  None
- totalTestsAntibody :  491876
- positiveTestsAntibody :  48506
- negativeTestsAntibody :  None
- totalTestsPeopleAntibody :  None
- positiveTestsPeopleAntibody :  None
- negativeTestsPeopleAntibody :  None
- totalTestsPeopleAntigen :  None
- positiveTestsPeopleAntigen :  None
- totalTestsAntigen :  353605
- positiveTestsAntigen :  29373
- fips :  48
- positiveIncrease :  7516
- negativeIncrease :  29650
- total :  8328869
- totalTestResultsIncrease :  37166
- posNeg :  8328869
- deathIncrease :  97
- hospitalizedIncrease :  0
- hash :  9ac9254e2934dc683a3630f6ffaa028087fb07a5
- commercialScore :  0
- negativeRegularScore :  0
- negativeScore :  0
- positiveScore :  0
- score :  0
- grade :  
```
and is stored an in array with the first index being the most recent recorded day.