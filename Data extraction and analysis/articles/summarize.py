# https://medium.com/fintechexplained/using-python-to-summarize-text-articles-7f1b248d9b43

from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

url = 'https://entrepreneurshandbook.co/number-three-511f334d8fae'
article = Article(url)
article.download()
article.parse()

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
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

file_sum = 'summary.txt'
with open(file_sum, 'a+') as fs:
    sum = summarize(article.text, 0.005)
    fs.write(sum)






# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation
# import string
# from spacy.lang.en.stop_words import STOP_WORDS
# from spacy.lang.en import English
# from heapq import nlargest
# from spacy.language import Language
# import feedparser
# import pdfkit
# import requests, bs4
#
# punctuations = string.punctuation
# nlp = English()
# nlp.add_pipe('sentencizer') # updated
# parser = English()
#
#
# def pre_process(document):
#     clean_tokens = [token.lemma_.lower().strip() for token in document]
#     clean_tokens = [token for token in clean_tokens if
#                     token not in STOP_WORDS and token not in punctuations]
#     tokens = [token.text for token in document]
#     lower_case_tokens = list(map(str.lower, tokens))
#
#     return lower_case_tokens
#
# def generate_numbers_vector(tokens):
#     frequency = [tokens.count(token) for token in tokens]
#     token_dict = dict(list(zip(tokens,frequency)))
#     maximum_frequency=sorted(token_dict.values())[-1]
#     normalised_dict = {token_key:token_dict[token_key]/maximum_frequency for token_key in token_dict.keys()}
#     return normalised_dict
#
# def sentences_importance(text, normalised_dict):
#     importance ={}
#     for sentence in nlp(text).sents:
#         for token in sentence:
#             target_token = token.text.lower()
#             if target_token in normalised_dict.keys():
#                 if sentence in importance.keys():
#                     importance[sentence]+=normalised_dict[target_token]
#                 else:
#                     importance[sentence]=normalised_dict[target_token]
#     return importance
#
# def generate_summary(rank, text):
#     target_document = parser(text)
#     importance = sentences_importance(text, generate_numbers_vector(pre_process(target_document)))
#     summary = nlargest(rank, importance, key=importance.get)
#     return summary
