import feedparser
import pdfkit
import requests, bs4
import feedparser
import urllib

def getData():
    """Downloading the latest article from 'Wrong a lot'
    and "Knower's substack"."""

    url = 'https://theknower.substack.com/p/good-crypto-bad-crypto?s=r'

    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.get_text()

    with open('knower.txt', 'w') as file:
        file.write(data)

def getDataCoops():
    """Downloading the latest article from 'Wrong a lot'
    and "Knower's substack"."""

    url = 'https://www.fwb.help/wip/what-co-ops-and-daos-can-learn-from-each-other'

    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    data = soup.get_text()

    with open('coops.txt', 'w') as file:
        file.write(data)


getDataCoops()
