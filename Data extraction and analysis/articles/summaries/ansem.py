from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import feedparser
import requests, bs4
import summarize
import pdfkit

def ansem_sum():
    """Summary of Ansem's latest article."""

    links = []
    article_to_sum = []
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

    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def ansem_download():
    """Downloading the latest 'Ansem' and 'Cobie' newsletters."""

    links = []
    urls = {
        "Ansem": "https://blknoiz06.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))
        address = links[5]

        print(f"Creating PDF from address: {address}")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()