#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import re
from nltk.corpus import stopwords

emoji_pos = ["😄", "😃", "😀", "😊", "☺", "😉", "😍", "😘", "😚", "😗", "😙", "😜", "😝", "😛", "😳", "😁", "😂", "😆",
             "😋", "😎", "😺", "😸", "😻", "😽", "💃", "👏", "👍", "👌", "👊", "👐", "✌", "🌞", "☀", "🔆", "🔅" "💡",
             "🍬", "🍭", "🍯", "🏆", "🐬"]

emoji_neg = ["😔", "😌", "😒", "😞", "😣", "😭", "😪", "😢", "😪", "😥", "😰", "😓", "😩", "😫", "😨", "😱", "😠", "😡",
             "😤", "😖", "😴", "😵", "😲", "😟", "😦", "😧", "😈", "👿", "😮", "😬", "😐", "😕", "😯", "😶", "😇", "😑",
             "💔", "💩", "👎"]

emoticone_pos = [":-)", ":)", "=)", "(:", "X)", "x)", "(x", "X)", "x)", "(x", ":-P", ":-p", ":P", ":p", "=P", "=p",
                 "X-D", "XD", "x-D", "xD", ":-]", ":]", "=]", ":-d", ":8d", "8-)", "8)", "8-O", "8O", "8D", "=d", "B-)",
                 "B)", "@-)", "<3", ":3", ":-3", "=3", ":-]", ":]", "=]"]

emoticone_neg = [":-(", ":(", "=(", "):-\|", ":\|", "=\|", "\|:", ":-/", ":/", "=/", "/:", ":'-(", ":'(", "='(" "*-*",
                 "¦~(", "D:", "DX", "D=", ":-@", ":@", ">:-(", ">:(", "=@", ">=("]

def formatEmoticone(chaine_emoticone):
    chaine = "|".join(chaine_emoticone)
    chaine = chaine.replace('(', "\\(")
    chaine = chaine.replace(')', "\\)")
    return chaine

formatedPos = formatEmoticone(emoticone_pos) + formatEmoticone(emoji_pos)
formatedNeg = formatEmoticone(emoticone_neg) + formatEmoticone(emoji_neg)


def applyOnTweet(tweet, formatted_string, replaceBy):
    replaceBy += " "
    reg_exp = re.compile(formatted_string)
    clean_tweet = re.sub(reg_exp, replaceBy, tweet)
    return clean_tweet


def cleanTweet(tweet):
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')

    formatted_emoticone_pos = formatedPos
    tweet = applyOnTweet(tweet, formatted_emoticone_pos, "happy")
    formatted_emoticone_neg = formatedNeg
    tweet = applyOnTweet(tweet, formatted_emoticone_neg, "sad")

    return tweet


def cleanTweets(tweets):
    for tweet in tweets:
        tweet.cleaned = cleanTweet(tweet.tweet)


def cleanBanalWords(allTweets):
    allTweets = re.sub(r'[0-9]', '', allTweets)
    allTweets = re.sub('RT', '', allTweets)

    allTweets = allTweets.lower()
    allTweets= ''.join([l for l in allTweets if l not in string.punctuation])
    allTweets= ' '.join([l for l in allTweets.split(" ") if l not in stopwords.words('french')])

    return allTweets





print cleanBanalWords("lire c'est refuser la chose qui a une des que mdr a a  qui  ai est")


