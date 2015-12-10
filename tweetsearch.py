#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import tweepy
from Tweet import Tweet
import TwitterResponse

import urllib2
import urllib

import json

TWITTER_SEARCH_URL = "https://twitter.com/i/search/timeline"
TYPE_PARAM = "f";
QUERY_PARAM = "q";
SCROLL_CURSOR_PARAM = "max_position";


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

    # return list(set([Tweet(tweet.text) for tweet in api.search(text, count=100, lang="en")]))


def executeSearch(url):
    serialized_data = urllib2.urlopen(url).read()
    return json.loads(serialized_data, object_hook=TwitterResponse.as_person)


def scrapper(query, rateDelay=1):
    url = constructURL(query)
    minTweet = None
    for i in range(10):
        response = executeSearch(url)
        tweets = response.getTweets()
        if (minTweet == None):
            minTweet = tweets[0].id
        maxTweet = tweets[len(tweets) - 1].id
        sleep(rateDelay)
        maxPosition = "TWEET-" + maxTweet + "-" + minTweet
        url = constructURL(query, maxPosition)


def maxPosition(min, max):
    if min == 0 or max == 0:
        return None
    else:
        return "TWEET-" + str(max) + "-" + str(min)


def tweetLang(lang):
    return 'lang:' + str(lang) + ' '


def scrap(query, minTweet, maxTweet, lang="en"):
    return scrapMaxPosition(query, maxPosition(minTweet, maxTweet), lang)


def scrapMaxPosition(query, maxPosition, lang="en"):
    url = constructURL(tweetLang(lang) + query, maxPosition)
    response = executeSearch(url)
    return response.getTweets()


def param(key, value):
    return str(key) + "=" + str(value)


def constructURL(query, maxPosition=None):
    params = [
        param(QUERY_PARAM, urllib.quote(query)),
        param(TYPE_PARAM, "tweets")
    ]

    if (maxPosition != None and maxPosition != ""):
        params += [param(SCROLL_CURSOR_PARAM, maxPosition)]

    url = TWITTER_SEARCH_URL + '?' + "&".join(params)

    return url