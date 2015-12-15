# -*- coding: utf-8 -*-

class Tweet:
    '''
    Class qui represente un tweet.
    Contient:
    - le tweet original
    - son id
    - le tweet nettoyé
    - le sentiment du tweet
    '''

    def __init__(self, id, tweet):
        self.id = id
        self.tweet = tweet
        self.cleaned = ""
        self.sentiment = 0

    def __eq__(self, other):
        if isinstance(other, Tweet):
            return self.tweet == other.tweet
        else:
            return False

    def serialize(self):
        return {
            'tweet': self.tweet,
            'degree': self.degree,
            'sentiment': self.sentiment
        }

    @property
    def degree(self):
        degree = int(self.sentiment / 2 * 10)
        if self.sentiment < 0:
            return 5 + degree
        else:
            return 5 - degree
