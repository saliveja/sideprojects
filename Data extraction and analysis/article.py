from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://cryptohayes.medium.com/energy-cancelled-e9f9e53a50cd'

# Initialize html variable where html from url is stored
html = ''

# Pretend we're running firefox to fool Medium into allowing us to scrape
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(req) as response:
   html = response.read()


# Parse with beautiful soup
soup = BeautifulSoup(html, 'html.parser')

print(soup.get_text())
