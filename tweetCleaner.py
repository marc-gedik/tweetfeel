#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import re

import nltk
from nltk.corpus import stopwords

# Liste des emojis positive
emoji_pos = ["😄", "😃", "😀", "😊", "☺", "😉", "😍", "😘", "😚", "😗", "😙", "😜", "😝", "😛", "😳", "😁", "😂", "😆",
             "😋", "😎", "😺", "😸", "😻", "😽", "💃", "👏", "👍", "👌", "👊", "👐", "✌", "🌞", "☀", "🔆", "🔅" "💡",
             "🍬", "🍭", "🍯", "🏆", "🐬"]

# Liste des emojis negative
emoji_neg = ["😔", "😌", "😒", "😞", "😣", "😭", "😪", "😢", "😪", "😥", "😰", "😓", "😩", "😫", "😨", "😱", "😠", "😡",
             "😤", "😖", "😴", "😵", "😲", "😟", "😦", "😧", "😈", "👿", "😮", "😬", "😐", "😕", "😯", "😶", "😇", "😑",
             "💔", "💩", "👎"]

# Liste des emoticones positive
emoticone_pos = [":-)", ":)", "=)", "(:", "X)", "x)", "(x", "X)", "x)", "(x", ":-P", ":-p", ":P", ":p", "=P", "=p",
                 "X-D", "XD", "x-D", "xD", ":-]", ":]", "=]", ":-d", ":8d", "8-)", "8)", "8-O", "8O", "8D", "=d", "B-)",
                 "B)", "@-)", "<3", ":3", ":-3", "=3", ":-]", ":]", "=]"]

# Liste des emoticones negative
emoticone_neg = [":-(", ":(", "=(", "):-\|", ":\|", "=\|", "\|:", ":-/", ":/", "=/", "/:", ":'-(", ":'(", "='(" "*-*",
                 "¦~(", "D:", "DX", "D=", ":-@", ":@", ">:-(", ">:(", "=@", ">=("]


def formatEmoticone(emoticones):
    '''
    Fonction qui prend en parametre une liste de string,
    assemble les elements de la liste avec le character '|'
    dans une chaine de carateres et la rentvoit
    '''
    chaine = "|".join(emoticones)
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


dict = {"en": {"good": "good", "bad": "bad"},
        "fr": {"good": "bien", "bad": "mauvais"}}


def cleanTweet(tweet, lang):
    '''
    Fonction qui permet de nettoyer un tweet de toutes les choses specifique à Twitter
    -> les URL, @User, #mot sont remplacé par URL, AT_USER et le mot du hashtag
    -> les emoticones sont rempacé par l'humeur lui correspondant
    '''

    # Convert to lower case
    tweet = tweet.lower()
    # Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    # Convert @username to AT_USER
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # trim
    tweet = tweet.strip('\'"')

    formatted_emoticone_pos = formatedPos
    tweet = applyOnTweet(tweet, formatted_emoticone_pos, dict[lang]["good"])
    formatted_emoticone_neg = formatedNeg
    tweet = applyOnTweet(tweet, formatted_emoticone_neg, dict[lang]["bad"])

    return tweet


def cleanTweets(tweets, lang):
    for tweet in tweets:
        tweet.cleaned = cleanTweet(tweet.tweet, lang)


def cleanBanalWords(allTweets, search, lang):
    '''
    Enleve dans une phrase les mots qui ne sont pas important
    '''

    if lang == "fr":
        lang = "french"
    else:
        lang = "english"

    allTweets = re.sub(r'[0-9]', '', allTweets)

    allTweets = allTweets.lower()
    allTweets = re.sub('rt', '', allTweets)
    allTweets = re.sub('at_user', '', allTweets)
    allTweets = re.sub('url', '', allTweets)
    allTweets = re.sub(search.lower(), '', allTweets)

    allTweets = ''.join([l for l in allTweets if l not in string.punctuation])
    allTweets = ' '.join([l for l in allTweets.split(" ") if l not in stopwords.words(lang)])

    return allTweets.strip()


def listFrequenceWord(listAllTweets, search, lang):
    '''
    Retourne une liste de frequence d'apparition des mots à partir d'une liste de tweet
    '''

    allTweets = [cleanBanalWords(textTweet.cleaned, search, lang) for textTweet in listAllTweets]

    allTweets = " ".join(allTweets)

    allTweets = allTweets.split(" ")

    listFrequence = nltk.FreqDist(allTweets)

    return [{"text": s, "weight": f} for (s, f) in listFrequence.most_common(listFrequence.N())]
