# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from Tweet import Tweet


class TwitterResponse(object):
    def __init__(self):
        self.has_more_items = None
        self.items_html = None
        self.refresh_cursor = None
        self.focused_refresh_interval = None

    def getTweets(self):
        tweets = []
        html = self.items_html.encode('ascii', 'ignore').decode('ascii')
        parsed_html = BeautifulSoup(html, "html.parser")
        for element in parsed_html.select("li.js-stream-item"):
            id = element['data-item-id']
            text = element.select("p.tweet-text")[0].get_text()
            tweets += [Tweet(id, text)]
        print(tweets)
        return tweets

def as_person(json):
    response = TwitterResponse()
    response.__dict__.update(json)
    return response
