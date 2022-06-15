import feedparser
import pdfkit
import requests, bs4
import summarize
import pprint
from newspaper import Article
import spacy
import sys
# !{sys.executable} -m spacy download en
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import string
from spacy.lang.en import English
from heapq import nlargest
from spacy.language import Language

punctuations = string.punctuation
nlp = English()
nlp.add_pipe('sentencizer')
parser = English()
# spacy.load('en_core_web_sm')

def summarize(text, per):
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
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
    text = soup1.find('p')
    print(text.get_text())
            #
            # file = 'summary.txt'
            # with open(file, 'a') as f:
            #     gen = summarize(text_str, 0.5)
            #
            # print(gen)
            #     f.write(gen_str)
            # # print(text_str)
            # links.clear()


knower()