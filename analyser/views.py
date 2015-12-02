from django.shortcuts import render

from sentiment import Sentiment
import tweetCleaner
from form import SearchForm
import tweetsearch

# -*- coding: utf-8 -*-

# Create your views here.
def home(request):
    return render(request, 'analyser/analyser.html', {'date': 12})


def analyze(request):
    form = SearchForm(request.GET)
    print(form)
    if form.is_valid():
        search = form.cleaned_data['search']

        tweets = tweetsearch.search(search)
        cleanedTweets = tweetCleaner.cleanTweets(tweets)
        pos, neg = Sentiment().percentage_pos_neg(cleanedTweets)

        return render(request, 'analyser/analyser.html', {"search": search, "pos": pos, "neg": neg, "tweets": tweets})
    return render(request, 'analyser/analyser.html')
