import requests, bs4
import summarize


def summary(name, link, index):
    """Summary of chosen articles."""

    article_to_sum = []

    res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    links = []
    for article in soup.find_all('a'):
        links.append(article.get('href'))

    address = links[index]

    req1 = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    html = soup1.find_all('p')
    for text in html:
        article = text.text
        article_to_sum.append(article)
    article_str = ' '.join(article_to_sum)
    sum = summarize.summarize(article_str, 0.05)
    return name, sum, address