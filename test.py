#!usr/bin/pyhton
# -*- coding: utf-8 -*-

from sentiment import Sentiment
from sentiment_lang import *

S = Sentiment(Lang.EN)

sentences = ["I'm happy!!",
	" I'm so tired."]

#print S.pos_or_neg_many(sentences)
print S.percentage_pos_neg(sentences)

