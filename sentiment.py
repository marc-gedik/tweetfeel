#!usr/bin/pyhton
# -*- coding: utf-8 -*-

from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from textblob_fr import PatternTagger, PatternAnalyzer
from sentiment_lang import *


class Sentiment():
    def __init__(self, lang=Lang.EN):
        ''' constructeur '''
        # créé des objet de type Textblob en
        # se servant de l'analyseur passé en argument
        self.lang = lang
        if self.lang == Lang.EN:
            self.tb = Blobber(analyzer=NaiveBayesAnalyzer())
        elif self.lang == Lang.FR:
            self.tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

    def pos_or_neg_one(self, sentence):
        ''' prend en argument une phrase propre et dit si elle est négative ou
            positive sous la forme d'un couple : (phrase , 'pos'/'neg').
            Exemple : ('je suis beau' , 'pos') '''

        blob = self.tb(sentence)
        return sentence, blob.sentiment[0]

    def pos_or_neg_many(self, sentences):
        ''' prend en argument une liste de phrases propres et indique si elles
            sont positives ou négatives (cf. fonction pos_or_neg_one()) '''

        return [self.pos_or_neg_one(sentence) for sentence in sentences]

    def nb_pos_neg(self, sentences):
        ''' prend en argument une liste de phrases et retourne
            un couple (# phrases_positives , # phrases_négatives) '''

        positives = 0
        negatives = 0
        analyzed_sentences = self.pos_or_neg_many(sentences)
        for a_sentence in analyzed_sentences:
            if a_sentence[1] == 'pos':
                positives += 1
            else:
                # if a_sentence[1] == 'neg'
                negatives += 1
        return positives, negatives

    def percentage_pos_neg(self, sentences):
        ''' prend en argument une liste de phrases et retourne un couple
            (pourcentage_phrases_positives , pourcentage_phrases_négatives) '''

        nombre_pos_neg = self.nb_pos_neg(sentences)
        nb_pos = nombre_pos_neg[0]
        nb_neg = nombre_pos_neg[1]
        nb_total = nb_pos + nb_neg
        return (nb_pos / float(nb_total)) * 100., nb_neg / float(nb_total) * 100.
