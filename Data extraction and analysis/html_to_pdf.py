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
links = {}

feed = feedparser.parse(url_hayes)
# print(feed.entries)

numDays = 30
date_list = []
date_rss = {}
#
# for x in range(numDays):
#     date_list.append(today_date - timedelta(days = x))
#     # appending all past 30 days to date_list

for entry in feed.entries:
        name = entry.title
        links[name] = entry.link
        # key is name, value is the value in entry.link
        # print(entry.published)
        date_rss[name] = date.fromtimestamp(calendar.timegm(time.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")))
print(links)
print(date_rss)
# print(today_date)

dates = today_date - timedelta(days=30)
print(dates)
#
for name, date in date_rss.items():
    if date_rss[name] == today_date or one or two or three or four or \
            five or six or seven or eight or nine or ten or eleven or twelve \
            or thirteen or fourteen or fifteen:
        print(f'{name} published {date_rss[name]}, checking < {today_date}, '
              f'{one}, {two}, {three}, {four}, {five}, {six}, {seven}, {eight},'
              f'{nine}, {ten}, {eleven}, {twelve}, {thirteen}, {fourteen}, '
              f'{fifteen}')
        print(f"Creating PDF , {name}")
        pdfkit.from_url(links[name], f"{name}.pdf")
        print(f"Created PDF {name} successfully!")
    else:
        print(f"{date_rss}")


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