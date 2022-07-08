from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import feedparser
import requests, bs4


def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary


def knower_sum():
    """Summary of Knower's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Knower's substack": "https://theknower.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[9]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def knower_download():
    """Downloading latest Knower article."""

    links = []
    urls = {
        "Knower's substack": 'https://theknower.substack.com/archive',
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            links.append(article.get('href'))
        address = links[9]

        print(f"Creating PDF from address: {address}")
        pdfkit.from_url(address, f'{key}.pdf')
        # converting html to pdf and downloading
        print(f"Created PDF successfully!")

def wrong_a_lot_sum():
    """Summary of Wrong a lot's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Wrong a lot": "https://wrongalot.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[9]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def kyla_sum():
    """Summary of Kyla's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Kyla": "https://kyla.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[9]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def ansem_sum():
    """Summary of Ansem's latest article."""

    links = []
    article_to_sum = []
    urls = {
            "Ansem": "https://blknoiz06.substack.com/archive",
            }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[5]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")


def cobie_sum():
    """Summary of Ansem's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Cobie": "https://cobie.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[5]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def scarpa_sum():
    """Summary of Scarpas's latest article."""

    urls = {
        "Scarpa": "https://medium.com/@TraderScarpa/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def hayes_sum():
    """Summary of Hayes's latest article."""

    urls = {
        "Hayes": "https://cryptohayes.medium.com/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def foo69_sum():
    """Summary of Foo69's latest article."""

    urls = {
            "Foo69": "https://fooo69.medium.com/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def godcomplex182_sum():
    """Summary of Godcomplex182's latest article."""

    urls = {
        "Godcomplex182": "https://medium.com/@godcomplex182/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def cryptocreddy_sum():
    """Summary of Cryptocreddy's latest article."""

    urls = {
            "Cryptocreddy": "https://medium.com/@cryptocreddy/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def oxgodking_sum():
    """Summary of Oxgodking's latest article."""

    urls = {
        "0xgodking": "https://medium.com/@0xgodking/feed",
            }

    links = []
    names = []
    article_to_sum = []

    for key, value in urls.items():
        feed = feedparser.parse(value)
        for entry in feed.entries:
            link = entry.link
            name = entry.title
            links.append(link)
            names.append(name)

    for link in links:
        req1 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
        html = soup1.find_all('p')
        for text in html:
            article = text.text
            article_to_sum.append(article)

    article_str = ' '.join(article_to_sum)
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

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
    sum = summarize(article_str, 0.5)
    print(sum)
    print("\n\n")

def no_sleep_sum():
    """Summary of No sleep's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "No Sleep": "https://nosleep.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[6]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def kyle_sum():
    """Summary of Kyle's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Kyle's Newsletter": "https://0xfren.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[6]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def ape_sum():
    """Summary of Ape's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "The Reading Ape Newsletter": "https://thereadingape.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[10]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def nat_sum():
    """Summary of Nat's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Nat's Newsletter": "https://crypto.nateliason.com/",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[15]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def rain_and_coffee_sum():
    """Summary of Rain and coffee's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Rain And Coffee Newsletter":
               "https://rainandcoffee.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[10]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def the_macro_compass_sum():
    """Summary of Rain and coffee's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "The Macro Compass Newsletter":
               "https://themacrocompass.substack.com/archive",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[10]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

def not_boring_sum():
    """Summary of Not boring's latest article."""

    links = []
    article_to_sum = []
    urls = {
        "Not Boring Newsletter": "https://www.notboring.co/",
    }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if (each_code := soup.find_all('a')[19]):
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
    sum = summarize(article_str, 0.05)
    print(sum)
    print("\n\n")

dict = {
"Knower's substack": "https://theknower.substack.com/archive",
"Wrong a lot": "https://wrongalot.substack.com/archive",
"Kyla": "https://kyla.substack.com/archive",
"Ansem": "https://blknoiz06.substack.com/archive",
"Cobie": "https://cobie.substack.com/archive",
"Scarpa": "https://medium.com/@TraderScarpa/feed",
"Hayes": "https://cryptohayes.medium.com/feed",
"Foo69": "https://fooo69.medium.com/feed",
"Godcomplex182": "https://medium.com/@godcomplex182/feed",
"Cryptocreddy": "https://medium.com/@cryptocreddy/feed",
"0xgodking": "https://medium.com/@0xgodking/feed",
"Onchain Wizard Newsletter": "https://onchainwizard.substack.com/archive",
"No Sleep": "https://nosleep.substack.com/archive",
"Kyle's Newsletter": "https://0xfren.substack.com/archive",
"The Reading Ape Newsletter": "https://thereadingape.substack.com/archive",
"Nat's Newsletter": "https://crypto.nateliason.com/",
"Rain And Coffee Newsletter": "https://rainandcoffee.substack.com/archive",
"The Macro Compass Newsletter": "https://themacrocompass.substack.com/archive",
"Not Boring Newsletter": "https://www.notboring.co/",
}


for i, item in enumerate(dict, 1):
    print(i, '' + item.strip(), "\n")
    # 'end' is what is happening before the number (i)
    # 'sep' is what is happening after the number (i)
    print("\n\n")

try:
    knower_sum()
    wrong_a_lot_sum()
    ansem_sum()
    cobie_sum()
    medium_sum()
    hayes_sum()
    foo69_sum()
    godcomplex182_sum()
    cryptocreddy_sum()
    oxgodking_sum()
    onchainwizard_sum()
    no_sleep_sum()
    kyle_sum()
    ape_sum()
    nat_sum()
    rain_and_coffee_sum()
    the_macro_compass_sum()
    not_boring_sum()

except ValueError:
    pass

select_download = input("With index number, select the article you "
                        "would like to download:")

if select_download == 1:
    knower_download()
else:
    print("They are not existing yet.")

