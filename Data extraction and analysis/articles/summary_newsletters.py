import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from heapq import nlargest
from spacy.language import Language
import feedparser
import pdfkit
import requests, bs4

punctuations = string.punctuation
nlp = English()
nlp.add_pipe('sentencizer') # updated
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
    maximum_frequency=sorted(token_dict.values())[-1]
    normalised_dict = {token_key:token_dict[token_key]/maximum_frequency for token_key in token_dict.keys()}
    return normalised_dict

def sentences_importance(text, normalised_dict):
    importance ={}
    for sentence in nlp(text).sents:
        for token in sentence:
            target_token = token.text.lower()
            if target_token in normalised_dict.keys():
                if sentence in importance.keys():
                    importance[sentence]+=normalised_dict[target_token]
                else:
                    importance[sentence]=normalised_dict[target_token]
    return importance

def generate_summary(rank, text):
    target_document = parser(text)
    importance = sentences_importance(text, generate_numbers_vector(pre_process(target_document)))
    summary = nlargest(rank, importance, key=importance.get)
    return summary


def knower():

    article = 'article.txt'
    with open(article, 'w') as f:
        f.truncate()

    links = []
    urls = {
                "Knower's substack": 'https://theknower.substack.com/archive',
                # "Wrong a lot": "https://wrongalot.substack.com/archive",
                # "Kyla": "https://kyla.substack.com/archive",
                   }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            link = article.get('href')
            links.append(link)

    req1 = requests.get(links[9], headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    html = soup1.find_all('p')

    for text in html:
        article = 'article.txt'
        with open(article, 'a+') as f:
            text_str = str(text.text)
            f.write(text_str)

    file = 'article.txt'
    with open(file, 'r+') as fx:
        file_sum = 'summary.txt'
        text_to_sum = fx.read()
        with open(file_sum, 'a+') as fs:
            gen = generate_summary(3, text_to_sum)
            gen_str = str(gen)
            fs.write(gen_str)

    # article = 'article.txt'
    # with open(article, 'r+') as f:
    #     f.read()
    #     tags = soup1.find_all("li")
    #     for text in f:
    #         for content in tags:
    #             lines = content.text
    #             f.write(text.replace(lines, f"\n* {lines}"))
    # links.clear()



knower()


# file = 'article.txt'
# with open(file, 'r') as fx:
#     file_sum = 'summary.txt'
#     text_to_sum = fx.read()
#     with open(file_sum, 'a') as fs:
#         gen = generate_summary(3, text_to_sum)
#         gen_str = str(gen)
#         fs.write(gen_str)






# res1 = urllib.request.urlopen(links[9],
#                              headers={'User-Agent': 'Mozilla/5.0'})
# soup1 = bs4.BeautifulSoup(res1, 'html.parser')
# # getting all the paragraphs
# for para in soup1.find_all("p"):
#     print(para.get_text())
#
# text_str = soup1.getText()
# text_strip = text_str.strip()
# text = soup1.find('p').text
# # text_str = text.getText()
# print(text)
#
