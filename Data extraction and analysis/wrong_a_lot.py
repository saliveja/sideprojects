from datetime import date, datetime, timedelta
import feedparser
import pdfkit
import time
import calendar
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, bs4
from urllib.request import Request, urlopen

links = []

res = requests.get("https://wrongalot.substack.com/archive", headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
dateElem = soup.find_all("div", class_="post-meta-item post-date")

# the date of each article
for date in dateElem:
    print(date['title'])

linkElem = soup.find_all("div", class_="post-preview-content")

for link in soup.find_all('a'):
    links.append(link.get('href'))

url = links[9]

print(f"Creating PDF")
pdfkit.from_url(url, 'wrongALot.pdf')
# converting html to pdf and downloading
print(f"Created PDF successfully!")



