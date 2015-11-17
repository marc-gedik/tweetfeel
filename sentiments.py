#!usr/bin/pyhton
# -*- coding: utf-8 -*-

from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

class Sentiments():

	def __init__(self):
		''' constructeur '''
		# créé des objet de type Textblob en 
		# se servant de l'analyseur passé en argument 
		self.tb = Blobber(analyzer=NaiveBayesAnalyzer())

	def pos_or_neg_one(self , sentence):
		''' prend en argument une phrase propre et dit si elle est négative ou
			positive sous la forme d'un couple : (phrase , 'pos'/'neg').
			Exemple : ('je suis beau' , 'pos') '''
			
		blob = self.tb(sentence)
		return sentence,blob.sentiment[0]

	def pos_or_neg_many(self, sentences):
		''' prend en argument une liste de phrases propres et indique si elles
			sont positives ou négatives (cf. fonction pos_or_neg_one()) '''

		return [self.pos_or_neg_one(sentence) for sentence in sentences]

	def nb_pos_neg(self , sentences):
		''' prend en argument une liste de phrases et retourne 
			un couple (# phrases_positives , # phrases_négatives) '''

		positives = 0
		negatives = 0
		analyzed_sentences = self.pos_or_neg_many(sentences)
		for a_sentence in analyzed_sentences :
			if a_sentence[1] == 'pos':
				positives += 1
			elif a_sentence[1] == 'neg':
				negatives += 1
		return positives , negatives

	def percentage_pos_neg(self , sentences):
		''' prend en argument une liste de phrases et retourne un couple
			(pourcentage_phrases_positives , pourcentage_phrases_négatives) '''

		nombre_pos_neg = self.nb_pos_neg(sentences)
		nb_total = nombre_pos_neg[0] + nombre_pos_neg[1]
		return nombre_pos_neg[0]/nb_total , nombre_pos_neg[1]/nb_total



