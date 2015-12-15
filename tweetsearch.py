#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json

import TwitterResponse

TWITTER_SEARCH_URL = "https://twitter.com/i/search/timeline"
TYPE_PARAM = "f"
QUERY_PARAM = "q"
SCROLL_CURSOR_PARAM = "max_position"


def executeSearch(url):
    '''
    Execute une requete url (de recherche Twitter)
    et attend en reponse un objet de type TwitterResponse
    '''
    serialized_data = urllib2.urlopen(url).read()
    return json.loads(serialized_data, object_hook=TwitterResponse.as_response)


def maxPosition(min, max):
    if min == 0 or max == 0:
        return None
    else:
        return "TWEET-" + str(max) + "-" + str(min)


def tweetLang(lang):
    '''
    paramametre de la langue Twitter au bon format
    '''
    return 'lang:' + str(lang) + ' '


def scrap(query, minTweet, maxTweet, lang="en"):
    return scrapMaxPosition(query, maxPosition(minTweet, maxTweet), lang)


def scrapMaxPosition(query, maxPosition, lang="en"):
    url = constructURL(tweetLang(lang) + query, maxPosition)
    response = executeSearch(url)
    return response.getTweets()


def param(key, value):
    '''
    Creer un parametre d'url
    '''
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
