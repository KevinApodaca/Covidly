import requests
import json

#Obtain list of articles from API
def getArticles(endpoint, params):
	response = requests.get(endpoint, params=params)
	news_data = response.json()
	articles = news_data['articles']
	return articles

if __name__ == '__main__':
	endpoint = 'http://newsapi.org/v2/top-headlines?'
	params = {
		'country': 'us', 
		'category': 'health',
		'category': 'science',
		'sortBy': 'popularity',
		'apiKey': 'KEY'
	}
	
	#Save articles
	articles = getArticles(endpoint, params)
	#How to access needed fields for News feed component
	for article in articles:
		print(article['source']['name'])
		print(article['title'])
		print(article['description'])
		print(article['url'])
		print(article['urlToImage'])