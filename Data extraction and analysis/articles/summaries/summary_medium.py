import feedparser
import requests, bs4
import summarize

def sum_medium(name, link, index):
    """Summary of selected medium articles."""

    links = []
    article_to_sum = []

    feed = feedparser.parse(link)
    for entry in feed.entries:
        link_selection = entry.link
        links.append(link_selection)

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

