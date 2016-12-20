import tweepy
from textblob import TextBlob

consumer_key = '9QRtdigr8IiO4lJsqM2RpBWQa'
consumer_secret = 'B9QBMlIJQn3hhv8N51witM26G6vAZaOoINrkHkPHkYtRa9VSVZ'

access_token = '260612693-m036cgKK7UFc5WYyzhJNihtw5gmkw2DrARpHcQ0J'
access_secret = 'ByA8KS39svd8Rqu2kHRvg5f6LBbg9D7Sou2ummQweZKDz'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

public_tweets = api.search('@ManUtd')

for tweet in public_tweets:
	print tweet.text.encode('utf-8')
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


