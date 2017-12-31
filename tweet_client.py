import os
import sys
import tweepy
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
	

	try:
		consumer_key = os.environ['TWITTER_CONSUMER_KEY']
		consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
		access_token = os.environ['TWITTER_ACCESS_KEY']
		access_secret = os.environ['TWITTER_ACCESS_SECRET']
	except KeyError:
		sys.stderr.write("TWITTER_' environment variables not set\n")
		sys.exit(1)
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token, access_secret)
	return auth

def get_twitter_client():


	auth = get_twitter_auth()
	client = tweepy.API(auth)
	return client