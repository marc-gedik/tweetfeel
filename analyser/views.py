# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from sentiment import Sentiment
import tweetCleaner
from form import SearchForm
import tweetSearch


# Create your views here.
def index(request):
    return render(request, 'analyser/analyser.html')


def analyze(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        search = form.cleaned_data['search']
        min = form.cleaned_data['min']
        max = form.cleaned_data['max']
        lang = form.cleaned_data['lang']

        tweets = tweetSearch.scrap(search, min, max, lang)
        tweetCleaner.cleanTweets(tweets, lang)
        wordFrequencies = tweetCleaner.listFrequenceWord(tweets, search, lang)

        pos, neg, neutre = Sentiment(lang).nb_pos_neg(tweets)
        if (min == 0):
            min = tweets[0].id
        max = tweets[len(tweets) - 1].id

        tweets = [tweet.serialize() for tweet in tweets]

        return JsonResponse(
            {
                "search": search,
                "pos": pos,
                "neg": neg,
                "neutre": neutre,
                "tweets": tweets,
                "min": min,
                "max": max,
                "wordFrequencies": wordFrequencies
            }
        )
    return HttpResponse('')
