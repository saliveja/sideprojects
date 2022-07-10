import feedparser
import pdfkit
import requests, bs4

def article_download(name, link, index):
    """Downloading the latest article."""

    res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    links = []
    for article in soup.find_all('a'):
        links.append(article.get('href'))

    address = links[index]

    print(f"Creating PDF from address: {address}")
    pdfkit.from_url(address, f'{name}.pdf')
    # converting html to pdf and downloading
    print(f"Created PDF successfully!")
