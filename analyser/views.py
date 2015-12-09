# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.serializers import serialize

from sentiment import Sentiment
import tweetCleaner
from form import SearchForm
import tweetsearch


# Create your views here.
def home(request):
    return render(request, 'analyser/analyser.html')


def analyze(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        search = form.cleaned_data['search']

        tweets = tweetsearch.search(search)
        tweetCleaner.cleanTweets(tweets)
        pos, neg, neutre = Sentiment().percentage_pos_neg(tweets)
        tweets.sort(lambda x, y: int(( y.sentiment - x.sentiment)*100))

        wordFrequencie = tweetCleaner.listFrequenceWord(tweets)
        return render(request, 'analyser/analyser.html',
                      {"search": search, "pos": pos, "neg": neg, "neutre": neutre, "tweets": tweets, "wordFrequencie": wordFrequencie})
    return render(request, 'analyser/analyser.html')

