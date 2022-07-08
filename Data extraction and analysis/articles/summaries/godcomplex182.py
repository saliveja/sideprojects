from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import feedparser
import requests, bs4
import summarize
import pdfkit

def godcomplex182_sum():
    """Summary of Godcomplex182's latest article."""

    urls = {
        "Godcomplex182": "https://medium.com/@godcomplex182/feed",
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

    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def godcomplex182_download():
    """Downloading the latest 'Godcomplex182' article."""

    urls = {
        'Godcomplex182': 'https://medium.com/@godcomplex182/feed',
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

        print(f"Creating PDF, {names[0]}")
        pdfkit.from_url(links[0], f"{key}, {names[0]}.pdf")
        # converting html to pdf and downloading
        print(f"Created PDF {names[0]} successfully!")
        links.clear()
        names.clear()