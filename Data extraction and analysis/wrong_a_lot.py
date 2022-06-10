from datetime import date, datetime, timedelta
import feedparser
import pdfkit
import time
import calendar
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, bs4
from urllib.request import Request, urlopen

def wrongALot():
    """Downloading the latest article from Wrong a lot."""
    links = []

    res = requests.get("https://wrongalot.substack.com/archive",
                       headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # dateElem = soup.find_all("div", class_="post-meta-item post-date")
    #
    # # the date of each article
    # for date in dateElem:
    #     print(date['title'])
    #     name = f'Wrong a lot' + date['title']

    # linkElem = soup.find_all("div", class_="post-preview-content")

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    url = links[9]

    print(f"Creating PDF")
    pdfkit.from_url(url, 'wrongALot.pdf')
    # converting html to pdf and downloading
    print(f"Created PDF successfully!")

def ansem():
    """Downloading the latest Ansem and Cobie newsletter."""

    links = []
    urls = {
        'Cobie': 'https://cobie.substack.com/archive',
        'Ansem': 'https://blknoiz06.substack.com/archive',
    }

    # linkElem = soup.find_all("div", class_="post-preview-content")

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

def hayes():
    """Downloading the latest Hayes article."""
    today_date = date.today()
    # printing the date of today

    fifteen = today_date - timedelta(days=15)
    fourteen = today_date - timedelta(days=14)
    thirteen = today_date - timedelta(days=13)
    twelve = today_date - timedelta(days=12)
    eleven = today_date - timedelta(days=11)
    ten = today_date - timedelta(days=10)
    nine = today_date - timedelta(days=9)
    eight = today_date - timedelta(days=8)
    seven = today_date - timedelta(days=7)
    # displaying the date seven days before today's date
    six = today_date - timedelta(days=6)
    five = today_date - timedelta(days=5)
    four = today_date - timedelta(days=4)
    three = today_date - timedelta(days=3)
    two = today_date - timedelta(days=2)
    one = today_date - timedelta(days=1)

    url_hayes = 'https://cryptohayes.medium.com/feed'
    # rss feed

    feed = feedparser.parse(url_hayes)
    # processing data with feedparser

    links = {}
    # dictionary to saves the name and links from the url
    date_rss = {}
    # dictionary with the name and the date of publication of the articles

    for entry in feed.entries:
        name = entry.title
        links[name] = entry.link
        # key == name, value is the value in entry.link
        # this means the web address
        date_rss[name] = date.fromtimestamp \
            (calendar.timegm(time.strptime(entry.published[:-13],
                                           "%a, %d %b %Y")))
        # the -13 is removing the GMT part of the date

    for name, link in links.items():
        if date_rss[name] == today_date or date_rss[name] == one or \
                date_rss[name] == two or date_rss[name] == three or \
                date_rss[name] == four or date_rss[name] == five or \
                date_rss[name] == six or date_rss[name] == seven or \
                date_rss[name] == eight or date_rss[name] == nine or \
                date_rss[name] == ten or date_rss[name] == eleven or \
                date_rss[name] == twelve or date_rss[name] == thirteen or \
                date_rss[name] == fourteen or date_rss[name] == fifteen:
            # comparing with every date from todays date and - 15 days
            print(f"Creating PDF, {name}")
            pdfkit.from_url(link, f"{name}.pdf")
            # converting html to pdf and downloading
            print(f"Created PDF {name} successfully!")
        else:
            print(f'There is no new publications.')

def onchainWizard():
    """Downloading the latest Onchain Wizard newsletter."""

    links = []
    url = {'Onchain Wizard': 'https://onchainwizard.substack.com/archive'}

    # linkElem = soup.find_all("div", class_="post-preview-content")
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    for article in soup.find_all('a'):
        links.append(article.get('href'))
    address = links[8]
    
    for key, value in url.items():
        print(f"Creating PDF")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")
        links.clear()



# wrongALot()
# ansem()
# hayes()
# cobie()
onchainWizard()