from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import feedparser
import pdfkit
import requests, bs4
import nltk

# url = 'https://entrepreneurshandbook.co/number-three-511f334d8fae'
# article = Article(url)
# article.download()
# article.parse()

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


def save_article_to_file():

    article = 'article.txt'
    with open(article, 'w') as f:
        f.truncate()

    links = []
    urls = {
                "Knower's substack": 'https://theknower.substack.com/archive',
                # "Wrong a lot": "https://wrongalot.substack.com/archive",
                # "Kyla": "https://kyla.substack.com/archive",
                   }

    for key, value in urls.items():
        res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for article in soup.find_all('a'):
            link = article.get('href')
            links.append(link)

    req1 = requests.get(links[9], headers={'User-Agent': 'Mozilla/5.0'})
    soup1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    html = soup1.find_all('p')

    for text in html:
        article = 'article.txt'
        with open(article, 'a+') as f:
            text_str = str(text.text)
            f.write(text_str)
    links.clear()

    article = open('article.txt', "rt")
    article_new = open("article_new.txt", "wt")
    for line in article:
        tags = soup1.find_all("li")
        for content in tags:
            nltk.download('punkt')
            text = content.text
            new_list = nltk.tokenize.sent_tokenize(text)


            # for each_item in new_list:
            #     print(new_list[1])
                # if each_item == new_list[0]:
                #     article_new.write(each_item.replace(new_line, f". {new_line}. "))
                # else:
                #     article_new.write(
                #         each_item.replace(new_line, f" {new_line}. "))

        #     article.close()
        #     article_new.close()

def save_summary():
    """Summarizing the article and saving to a file"""
    file = 'article.txt'
    with open(file, 'r') as fx:
        text_to_sum = fx.read()
        file_sum = 'summary.txt'
        with open(file_sum, 'a+') as fs:
            sum = summarize(text_to_sum, 0.05)
            fs.write(sum)




save_article_to_file()
# save_summary()



# res1 = urllib.request.urlopen(links[9],
#                              headers={'User-Agent': 'Mozilla/5.0'})
# soup1 = bs4.BeautifulSoup(res1, 'html.parser')
# # getting all the paragraphs
# for para in soup1.find_all("p"):
#     print(para.get_text())
#
# text_str = soup1.getText()
# text_strip = text_str.strip()
# text = soup1.find('p').text
# # text_str = text.getText()
# print(text)
#
