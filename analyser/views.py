# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render

from sentiment import Sentiment
import tweetCleaner
from form import SearchForm
import tweetsearch


# Create your views here.
def home(request):
    return render(request, 'analyser/analyser.html')


def index(request):
    return render(request, 'analyser/analyser.html')


def analyze(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        search = form.cleaned_data['search']
        min = form.cleaned_data['min']
        max = form.cleaned_data['max']

        tweets = tweetsearch.scrap(search, min, max)
        tweetCleaner.cleanTweets(tweets)

        pos, neg, neutre = Sentiment().percentage_pos_neg(tweets)
        if(min == 0):
            min = tweets[0].id
        max = tweets[len(tweets) - 1].id
        tweets = [tweet.serialize() for tweet in tweets]

        ## tweets.sort(lambda x, y: int(( y.sentiment - x.sentiment)*100))

        return JsonResponse(
            {"pos": pos,
             "neg": neg,
             "neutre": neutre,
             "tweets": tweets,
             "min": min,
             "max": max
             }
        )
    print("---Non--")
    return HttpResponse('')
