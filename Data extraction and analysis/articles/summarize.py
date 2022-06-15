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

def knower():
    links = []
    urls = {
                "Knower's substack": 'https://theknower.substack.com/archive',
                # "Wrong a lot": "https://wrongalot.substack.com/archive",
                # "Kyla": "https://kyla.substack.com/archive",
                   }

    for key, value in urls.items():
        # print(key)
        # print(value)
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[9]

        res1 = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
        res1.raise_for_status()
        soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')
        for text in soup1.findAll('p'):
            text_str = text.getText()
            # print(text_str)


            file = 'summary.txt'
            with open(file, 'a') as f:
                gen = generate_summary(20, text_str)

            print(gen)
            #     f.write(gen_str)
            # # print(text_str)
            # links.clear()

knower()

