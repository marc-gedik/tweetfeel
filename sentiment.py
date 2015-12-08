#!usr/bin/pyhton
# -*- coding: utf-8 -*-

from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
##from textblob_fr import PatternTagger, PatternAnalyzer
from utils import Sentiment, Lang


class Sentiment():
    def __init__(self, lang=Lang.EN):
        """ constructeur """
        # créé des objet de type Textblob en
        # se servant de l'analyseur passé en argument
        if lang == Lang.EN:
            self.tb = TextBlob
            ##      elif lang == Lang.FR:

    ##        self.tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

    def pos_or_neg_one(self, tweet):
        """ prend en argument une phrase propre et dit si elle est négative ou
            positive sous la forme d'un couple : (phrase , 'pos'/'neg').
            Exemple : ('je suis beau' , 'pos') """

        blob = self.tb(tweet.cleaned)

        tweet.sentiment = blob.sentiment.polarity
        if blob.sentiment.polarity > 0:
            return 'pos'
        elif blob.sentiment.polarity == 0:
            return 'neutre'
        else:
            return 'neg'

    def pos_or_neg_many(self, tweets):
        """ prend en argument une liste de phrases propres et indique si elles
            sont positives ou négatives (cf. fonction pos_or_neg_one()) """

        return [self.pos_or_neg_one(sentence) for sentence in tweets]

    def nb_pos_neg(self, tweets):
        """ prend en argument une liste de phrases et retourne
            un couple (# phrases_positives , # phrases_négatives) """

        positives = 0
        negatives = 0
        neutre = 0
        analyzed_sentences = self.pos_or_neg_many(tweets)
        for a_sentence in analyzed_sentences:
            if a_sentence == 'pos':
                positives += 1
            elif a_sentence == 'neg':
                negatives += 1
            else:
                neutre += 1

        return positives, negatives, neutre

    def percentage_pos_neg(self, tweets):
        ''' prend en argument une liste de phrases et retourne un couple
            (pourcentage_phrases_positives , pourcentage_phrases_négatives) '''

        nombre_pos_neg = self.nb_pos_neg(tweets)
        nb_pos, nb_neg, nb_neutre = nombre_pos_neg
        nb_total = nb_pos + nb_neg + nb_neutre
        return nb_pos / float(nb_total) * 100., \
               nb_neg / float(nb_total) * 100., \
               nb_neutre / float(nb_total) * 100.
