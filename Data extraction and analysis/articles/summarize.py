# https://medium.com/fintechexplained/using-python-to-summarize-text-articles-7f1b248d9b43
import sys
#!{sys.executable} -m spacy download en
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import string
from spacy.lang.en import English
from heapq import nlargest
from spacy.language import Language
import feedparser
import pdfkit
import requests, bs4


punctuations = string.punctuation
nlp = English()
nlp.add_pipe('sentencizer')
parser = English()


def pre_process(document):
    clean_tokens = [token.lemma_.lower().strip() for token in document]
    clean_tokens = [token for token in clean_tokens if
                    token not in STOP_WORDS and token not in punctuations]
    tokens = [token.text for token in document]
    lower_case_tokens = list(map(str.lower, tokens))

    return lower_case_tokens

def generate_numbers_vector(tokens):
    frequency = [tokens.count(token) for token in tokens]
    token_dict = dict(list(zip(tokens,frequency)))
    maximum_frequency = sorted(token_dict.values())[-1]
    normalised_dict = {token_key:token_dict[token_key]/maximum_frequency
                       for token_key in token_dict.keys()}
    return normalised_dict

def sentences_importance(text, normalised_dict):
    importance ={}
    for sentence in nlp(text).sents:
        for token in sentence:
            target_token = token.text.lower()
            if target_token in normalised_dict.keys():
                if sentence in importance.keys():
                    importance[sentence] += normalised_dict[target_token]
                else:
                    importance[sentence] = normalised_dict[target_token]
    return importance

def generate_summary(rank, text):
    target_document = parser(text)
    importance = sentences_importance(text, generate_numbers_vector(pre_process(target_document)))
    summary = nlargest(rank, importance, key=importance.get)
    return summary

def mediumArticles():
    """Downloading the latest 'Scarpa', 'Hayes', 'Foo69', 'Godcomplex182',
     'Cryptocreddy', '0xgodking' articles."""

    urls = {'Scarpa': 'https://medium.com/@TraderScarpa/feed',
            # 'Hayes': 'https://cryptohayes.medium.com/feed',
            # 'Foo69': 'https://fooo69.medium.com/feed',
            # 'Godcomplex182': 'https://medium.com/@godcomplex182/feed',
            # 'Cryptocreddy': 'https://medium.com/@cryptocreddy/feed',
            # '0xgodking': 'https://medium.com/@0xgodking/feed',
            }

    links = []
    names = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)
    print(links)
    for link in links:
        res1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        res1.raise_for_status()
        soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')

        text_str = soup1.get_text()

        file = 'summary.txt'
        with open(file, 'a') as f:
            gen = generate_summary(3, text_str)
            gen_str = str(gen)
            print(gen_str)
            f.write(gen_str)
            # print(text_str)
            links.clear()
            names.clear()

mediumArticles()

