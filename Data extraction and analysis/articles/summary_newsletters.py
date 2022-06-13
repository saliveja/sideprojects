import feedparser
import pdfkit
import requests, bs4
import summarize as s
import pprint

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
        # print(key)
        # print(value)
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))

        address = links[9]

        req = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 =bs4.BeautifulSoup(req.text, 'html.parser')
        pElems = soup1.select('p')

        text = pElems[0].getText()
        text_str = str(text)
        with open("summary.txt", "a") as f:
            num_sentences_to_generate = 5
            gen = s.generate_summary(num_sentences_to_generate, text_str)
            gen_str = str(gen)
            f.write(key)
            f.write('\n\n')
            f.write(gen_str)
            f.write('\n\n')
        links.clear()


wrongALotKnower()