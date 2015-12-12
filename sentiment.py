#!usr/bin/pyhton
# -*- coding: utf-8 -*-

import pattern.en as en
import pattern.fr as fr


class Sentiment():
    def __init__(self, lang="en"):
        """ constructeur """
        # créé des objet de type Textblob en
        # se servant de l'analyseur passé en argument
        if lang == "en":
            
            self.tb = en.sentiment
        elif lang == "fr":
            self.tb = fr.sentiment

    def pos_or_neg_one(self, tweet):
        """ prend en argument une phrase propre et dit si elle est négative ou
            positive sous la forme d'un couple : (phrase , 'pos'/'neg').
            Exemple : ('je suis beau' , 'pos') """

        polarity, subjectivity = self.tb(tweet.cleaned)
        tweet.sentiment = polarity
        if polarity > 0:
            return 'pos'
        elif polarity == 0:
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
