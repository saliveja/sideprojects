import requests, bs4
from urllib.request import Request, urlopen
from datetime import date, datetime, timedelta
import feedparser
import requests
import pdfkit
import time
import calendar

url_feed = {'hayes':'https://cryptohayes.medium.com/feed',
           'uncommoncore':'https://uncommoncore.co/feed',}
#            'Our network': 'https://ournetwork.substack.com/',
#            'Messari': 'https://messari.io/research',
#            '0xparc': 'https://0xparc.org/blog',
#            'Mycelium': 'https://mycelium.xyz/research',
#            'Paradigm': 'https://www.paradigm.xyz/writing',
#            'Credit Suisse': 'https://www.credit-suisse.com/marketinsights'
#                             '/nl/en.html',
#            'Metagovernance project': 'https://metagov.org/',
#            'Bitmex': 'https://blog.bitmex.com/?lang=en_us',
# }

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
date_rss = {}

for entry in feed.entries:
        name = entry.title
        links[name] = entry.link
        # key is name, value is the value in entry.link
        date_rss[name] = date.fromtimestamp\
            (calendar.timegm(time.strptime(entry.published[:-13],
                                           "%a, %d %b %Y")))
        # the -13 is removing the GMT part of the date

# for each_value in date_rss.values():
#     print(each_value)
print(links)
# print(date_rss)
# print(today_date)


for name, link in links.items():
    if date_rss[name] == today_date or date_rss[name] == one or \
                date_rss[name] == two or date_rss[name] == three or \
                date_rss[name] == four or date_rss[name] == five or \
                date_rss[name] == six or date_rss[name] == seven or \
                date_rss[name] == eight or date_rss[name] == nine or \
                date_rss[name] == ten or date_rss[name] == eleven or \
                date_rss[name] == twelve or date_rss[name] == thirteen or \
                date_rss[name] == fourteen or date_rss[name] == fifteen:
        # print(f'{name} published {date_rss[name]}, checking dates: '
        #       f'{one}, {two}, {three}, {four}, {five}, {six}, {seven}, '
        #       f'{eight}, {nine}, {ten}, {eleven}, {twelve}, {thirteen}, '
        #       f'{fourteen}, {fifteen}')
        print(f"Creating PDF, {name}")
        pdfkit.from_url(link, f"{name}.pdf")
        print(f"Created PDF {name} successfully!")
    else:
        print(f'There is no new publications.')

# url_ucc = 'https://uncommoncore.co/blog/feed'
#
# link_list_ucc = []
#
# feed = feedparser.parse(url_ucc)
# for entry in feed.entries:
#     # print(entry.published)
#     # print(entry.link)
#     link_list_ucc.append(entry.link)
#
#     documentUcc = link_list_ucc[0]
#     # index 0 is the latest article
#     print(documentUcc)
#
#     for dates in entry.published
#         print(dates)
#         if dates == today_date or one or two or three or four \
#                 or five or six or seven:
#             name = entry.title
#             # read_text = entry.content
#             pdfkit.from_url(documentUcc, f"{name}.pdf")
#         else:
#             print("There are no new articles published.")