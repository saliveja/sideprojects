# import wkhtmltopdf
import requests, bs4
from urllib.request import Request, urlopen
from datetime import date, datetime, timedelta
import feedparser
import requests
import pdfkit
# from django.http import HttpResponse


sources = ['https://cryptohayes.medium.com/feed',
           'https://uncommoncore.co/feed/']
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
# url = 'https://cryptohayes.medium.com/'

today_date = date.today()
# print(today_date)
# printing the date of today

seven = today_date + timedelta(days=-7)
# displaying the date seven days before today's date
six = today_date + timedelta(days=-6)
five = today_date + timedelta(days=-5)
four = today_date + timedelta(days=-4)
three = today_date + timedelta(days=-3)
two = today_date + timedelta(days=-2)
one = today_date + timedelta(days=-1)

link_list = []

for thing in sources:
    feed = feedparser.parse(thing)
    for entry in feed.entries:
        # print(entry.published)
        for item in entry.link:
            links = entry.link
            link_list.append(links)

        document = link_list[0]
        # index 0 is the latest article

        for item in entry.published:
            if item == today_date or one or two or three or four \
                    or five or six or seven:
                name = entry.title
                # read_text = entry.content
                pdfkit.from_url(document, f"{name}.pdf")
            else:
                print("There are no new articles published.")