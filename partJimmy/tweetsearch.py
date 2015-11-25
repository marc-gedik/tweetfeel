#!/usr/bin/env python

import tweepy
import sys


if __name__ == '__main__':

        #Test
        if(len(sys.argv)==1):
                print 'expected one argument for search\nexample: to search tweets in relation with #PSG, put in argument only PSG'
                sys.exit(0)

        searching=sys.argv[1]
        

	#Authentification 

	consumer_key 	= "wSWkHDSbWDp7Nwu8lsYUb8bw8"
	consumer_secret = "MWdrqQXPSIGWLkrCt0mOy1aGXqupUbsTzZCXFxhZWr4eO6MTzr"
	access_token    = "4253365096-JhijcM9BJh1iXPapRKUmBmNe7U6964pHSuxtd1Z"
	access_token_secret = "SEyxzN3G4GlciJLYUJ3tBxKcqakobSwtrgW5AsxMlyorf"

	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	#Construct the API instance
	api = tweepy.API(auth)

	
	public_tweets =  api.home_timeline(count=200)

	my_search = api.search(q='#psg',rpp=1500,since=None,count=15000)

	for tweet in my_search:
		print tweet.text
		print '********'
	"""
	for tweet in tweepy.Cursor(api.search,
                       q="#"+searching,
                       count=100,
                       result_type="recent",
                       include_entities=True,
                       lang="fr"
                       ).items():
		print tweet.text


