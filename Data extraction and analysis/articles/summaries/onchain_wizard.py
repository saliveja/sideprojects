from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import feedparser
import requests, bs4
import summarize
import pdfkit

def onchainwizard_sum():
    """Summary of Onchain wizard's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Onchain Wizard Newsletter": "https://onchainwizard.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[8]):
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
    print(article_str)
    sum = summarize.summarize(article_str, 0.5)
    print(sum)
    print("\n\n")

def onchainWizard_download():
    """Downloading the latest 'Onchain Wizard' newsletter."""

    links = []
    url = {
        'Onchain Wizard Newsletter': 'https://onchainwizard.substack.com/archive'
            }

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))
        address = links[8]

        print(f"Creating PDF from address: {address}")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()