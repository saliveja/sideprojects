from datetime import date, datetime, timedelta
import feedparser
import pdfkit
import time
import calendar
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, bs4
from urllib.request import Request, urlopen

def wrongALotKnower():
    """Downloading the latest article from 'Wrong a lot'
    and "Knower's substack"."""

    links = []
    urls = {
        "Knower's substack": 'https://theknower.substack.com/archive',
        "Wrong a lot": "https://wrongalot.substack.com/archive",
        "Kyla": "https://kyla.substack.com/archive",
           }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))
        address = links[9]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def ansemCobie():
    """Downloading the latest 'Ansem' and 'Cobie' newsletters."""

    links = []
    urls = {
        'Cobie': 'https://cobie.substack.com/archive',
        'Ansem': 'https://blknoiz06.substack.com/archive',
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))
        address = links[5]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def mediumArticles():
    """Downloading the latest 'Scarpa', 'Hayes', 'Foo69', 'Godcomplex182',
     'Cryptocreddy', '0xgodking' articles."""

    urls = {'Scarpa': 'https://medium.com/@TraderScarpa/feed',
            'Hayes': 'https://cryptohayes.medium.com/feed',
            'Foo69': 'https://fooo69.medium.com/feed',
            'Godcomplex182': 'https://medium.com/@godcomplex182/feed',
            'Cryptocreddy': 'https://medium.com/@cryptocreddy/feed',
            '0xgodking': 'https://medium.com/@0xgodking/feed',
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

def onchainWizard():
    """Downloading the latest 'Onchain Wizard' newsletter."""

    links = []
    url = {'Onchain Wizard Newsletter': 'https://onchainwizard.substack.com/archive'}

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))
        address = links[8]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def noSleepKyle():
    """Downloading 'No sleep' and "Kyle's" newsletters"""

    links = []
    url = {'No Sleep': 'https://nosleep.substack.com/archive',
           "Kyle's Newsletter": 'https://0xfren.substack.com/archive'
           }

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[6]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def ape():

    links = []
    url = {'The Reading Ape Newsletter': 'https://thereadingape.substack.com/archive',
           }

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[10]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def nat():
    links = []
    url = {"Nat's Newsletter": 'https://crypto.nateliason.com/',
           }

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[15]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def rainMacro():
    links = []
    url = {"Rain And Coffee Newsletter":
               'https://rainandcoffee.substack.com/archive',
           "The Macro Compass Newsletter":
               'https://themacrocompass.substack.com/archive',
           }

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[10]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()

def notBoring():
    links = []
    url = {"Not Boring Newsletter":
               'https://www.notboring.co/',
           }

    for key, value in url.items():
        res = requests.get(url[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[19]

        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()








wrongALotKnower()
ansemCobie()
onchainWizard()
noSleepKyle()
ape()
nat()
rainMacro()
notBoring()
mediumArticles()