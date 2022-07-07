from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import feedparser
import requests, bs4


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


def knower_sum():
    """Summary of Knower's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Knower's substack": 'https://theknower.substack.com/archive',
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[9]):
            x = each_code.get('href')
            links.append(x)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)
    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def wrong_a_lot_sum():
    """Summary of Wrong a lot's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Wrong a lot": "https://wrongalot.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[9]):
            x = each_code.get('href')
            links.append(x)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)
    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def kyla_sum():
    """Summary of Kyla's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Kyla": "https://kyla.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[9]):
            x = each_code.get('href')
            links.append(x)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)
    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def ansem_sum():
    """Summary of Ansem's latest article."""

    links = []
    urls = {
        "Ansem": "https://blknoiz06.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[5]):
            x = each_code.get('href')
            links.append(x)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")


def cobie_sum():
    """Summary of Ansem's latest article."""

    links = []
    urls = {
        "Cobie": "https://cobie.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[5]):
            x = each_code.get('href')
            links.append(x)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def medium_sum():
    """Summary of Scarpas's latest article."""

    urls = {
        "Scarpa": "https://medium.com/@TraderScarpa/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def hayes_sum():
    """Summary of Hayes's latest article."""

    urls = {
        "Hayes": "https://cryptohayes.medium.com/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ''.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")
#
# knower_sum()
# wrong_a_lot_sum()
# ansem_sum()
# cobie_sum()
# medium_sum()
hayes_sum()




#
#
# ,
#             'Foo69': 'https://fooo69.medium.com/feed',
#             'Godcomplex182': 'https://medium.com/@godcomplex182/feed',
#             'Cryptocreddy': 'https://medium.com/@cryptocreddy/feed',
#             '0xgodking': 'https://medium.com/@0xgodking/feed',
#
#
#
#










# def save_summary():
#     """Summarizing the article and saving to a file"""
#     article_str = str(article_to_sum)
#     sum = summarize(article_str, 0.05)
#     print(sum)
#
#     # file = 'article.txt'
#     # with open(file, 'r') as fx:
#     #     text_to_sum = fx.read()
#     #     file_sum = 'summary.txt'
#     #     with open(file_sum, 'a+') as fs:
#     #         sum = summarize(text_to_sum, 0.05)
#     #         fs.write(sum)
#     #         fs.write("\n\n")

# def truncate():
#     article = 'article.txt'
#     with open(article, 'w') as f:
#         f.truncate()


# def knower():
#     article = 'article.txt'
#     with open(article, 'w') as f:
#         f.truncate()
#
#     links = []
#     urls = {
#         "Knower's substack": 'https://theknower.substack.com/archive',
#         "Wrong a lot": "https://wrongalot.substack.com/archive",
#         "Kyla": "https://kyla.substack.com/archive",
#     }
#
#     for key, value in urls.items():
#         res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
#         res.raise_for_status()
#         soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
#         for article in soup.find_all('a'):
#             link = article.get('href')
#             links.append(link)
#
#     req1 = requests.get(links[9], headers={'User-Agent': 'Mozilla/5.0'})
#     soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
#     html = soup1.find_all('p')
#
#     for text in html:
#         article = 'article.txt'
#         with open(article, 'a+') as f:
#             text_str = str(text.text)
#             f.write(text_str)
#     links.clear()
#
#     bullet_points = []
#     article_file = open('article.txt', "r")
#     article_new = open("article_new.txt", "w")
#
#     tags = soup1.find_all("li")
#     for content in tags:
#         # nltk.download('punkt')
#         text = content.text
#         string_to_list_items = nltk.tokenize.sent_tokenize(text)[0]
#         bullet_points.append(string_to_list_items)
#
#     print(bullet_points)
#
#     for article in article_file:
#         for line in bullet_points:
#             line_new_2 = f" {line}."
#             article = article.replace(line, line_new_2)
#
#         article_new.write(article)
#
#     file = 'article_new.txt'
#     with open(file, 'r') as fx:
#         text_to_sum = fx.read()
#         file_sum = 'summary.txt'
#         with open(file_sum, 'a+') as fs:
#             sum = summarize(text_to_sum, 0.05)
#             fs.write(sum)
#             fs.write("\n\n")
#

# "Wrong a lot": "https://wrongalot.substack.com/archive",
# "Kyla": "https://kyla.substack.com/archive",


# for text in html:
#     article_file = 'article.txt'
#     article = text.text
#     article_str = str(article)
#     with open(article_file, 'w+') as f:
#             # text_str = str(text.text)
#             f.write(article_str)

#
# article_file = open('article.txt', "r+")
# article_new = open("article_new.txt", "w")
#
# req1 = requests.get(links[9], headers={'User-Agent': 'Mozilla/5.0'})
# soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
# html = soup1.find_all('p')
#
# bullet_points = []
# tags = soup1.find_all("li")
# for key, value in urls.items():
#     res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
#     for content in tags:
#         if tags in soup:
#         # nltk.download('punkt')
#             text = content.text
#             string_to_list_items = nltk.tokenize.sent_tokenize(text)[0]
#             bullet_points.append(string_to_list_items)
#
# for article in article_file:
#     for line in bullet_points:
#         line_new_2 = f" {line}."
#         article = article.replace(line, line_new_2)
#
#     article_new.write(article)