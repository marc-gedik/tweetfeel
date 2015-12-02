#!/usr/bin/env python

import tweepy



def search(text):
      # Authentification

    consumer_key = "wSWkHDSbWDp7Nwu8lsYUb8bw8"
    consumer_secret = "MWdrqQXPSIGWLkrCt0mOy1aGXqupUbsTzZCXFxhZWr4eO6MTzr"

    access_token = "4253365096-JhijcM9BJh1iXPapRKUmBmNe7U6964pHSuxtd1Z"
    access_token_secret = "SEyxzN3G4GlciJLYUJ3tBxKcqakobSwtrgW5AsxMlyorf"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Construct the API instance
    api = tweepy.API(auth)

    return [tweet.text for tweet in api.search(text, count=100, lang="en")]

