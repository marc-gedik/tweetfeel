# -*- coding: utf-8 -*-

class Tweet:
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

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.tweet.__hash__()

    def __str__(self):
        return self.tweet


