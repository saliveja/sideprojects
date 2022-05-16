# import wkhtmltopdf
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date, datetime, timedelta
import feedparser
import requests
import weasyprint

#
# sources = {'Hayes': 'https://cryptohayes.medium.com/',
#            'Su Zhu & Hasu': 'https://uncommoncore.co/',
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
url = 'https://cryptohayes.medium.com/'
feed = feedparser.parse("https://cryptohayes.medium.com/feed")
link_list = []

for entry in feed.entries:
    # print(entry.published)
    for item in entry.link:
        links = entry.link
        link_list.append(links)

document = link_list[0]
# index 0 is the latest article

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

for entry in feed.entries:
    if entry.published in url == today_date or one or two or three or four \
            or five or six or seven:
        name = entry.title
        name_edited = name.title()
        weasyprint.HTML(document).write_pdf(f"{name.title()}.pdf")
        # wkhtmltopdf(f"url={document}, output_file={name_edited}.pdf")
    else:
        print("sorry, nothing new.")
