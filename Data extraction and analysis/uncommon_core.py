# import requests, bs4
# from urllib.request import Request, urlopen
# from datetime import date, datetime, timedelta
# import feedparser
# import requests
# import pdfkit
# import time
# import calendar
# import lxml.html
import requests, os, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://uncommoncore.co/blog')
tag_list = []
linkElem = driver.find_elements(By.CLASS_NAME, 'elementor-post_title')
tag_list.append(linkElem)
print(linkElem)




# url = 'https://uncommoncore.co/blog'
# os.makedirs('UncommonCore', exist_ok=True)
# # making the folder xkcd
# # or making an exception if the folder already exists
# headers = {'Accept': 'audio/mpeg'}
#
#
# # # downloading url
# # print(res.headers)
# while not url.endswith('#'):
# # the loop ends when the url ends with #
#     print('Downloading page %s...' % url)
#     # printing the url, so we know which page we are downloading
#     res = requests.get(url, headers=headers)
#     # downloading url
#     print(res.headers)
#     res.raise_for_status()
#     # calling raise_the_status so that the download is stopped if
#     # something went wrong
#
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     # download page
#     # find url
#     # download image
#     # save image to ./xkcd
#     # get previous buttons url
#
#     audioElem = soup.select('#wp-block-audio audio')
#
#     if audioElem == []:
#         print('Could not find the podcast.')
#     else:
#         audioUrl = 'https:' + audioElem[0].get('src')
#         # download image
#         print('Downloading image %s...' f'{audioUrl}')
#         res = requests.get(audioUrl)
#         res.raise_for_status()
#         audioFile = open(os.path.join('UncommonCore', os.path.basename(audioUrl)), 'wb')
#         # 'wb' --> write binary
#
#         for chunk in res.iter_content(100000):
#             imageFile.write(chunk)
#         imageFile.close()
#
#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = 'https://xkcd.com' + prevLink.get('href')
#
# print("Done.")


# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.text, 'html.parser')
# song_title = soup.find('channel')
# print(soup)
        # the -13 is removing the GMT part of the date
# print(date_rss)
# #
# for name, link in links.items():
#     url = 'https://uncommoncore.co/blog/feed'
#     # if date_rss[name] == today_date or date_rss[name] == one or \
#     #             date_rss[name] == two or date_rss[name] == three or \
#     #             date_rss[name] == four or date_rss[name] == five or \
#     #             date_rss[name] == six or date_rss[name] == seven or \
#     #             date_rss[name] == eight or date_rss[name] == nine or \
#     #             date_rss[name] == ten or date_rss[name] == eleven or \
#     #             date_rss[name] == twelve or date_rss[name] == thirteen or \
#     #             date_rss[name] == fourteen or date_rss[name] == fifteen:
#         # comparing with every date from todays date and - 15 days

#
# today_date = date.today()
# # printing the date of today
#
# fifteen = today_date - timedelta(days=15)
# fourteen = today_date - timedelta(days=14)
# thirteen = today_date - timedelta(days=13)
# twelve = today_date - timedelta(days=12)
# eleven = today_date - timedelta(days=11)
# ten = today_date - timedelta(days=10)
# nine = today_date - timedelta(days=9)
# eight = today_date - timedelta(days=8)
# seven = today_date - timedelta(days=7)
# # displaying the date seven days before today's date
# six = today_date - timedelta(days=6)
# five = today_date - timedelta(days=5)
# four = today_date - timedelta(days=4)
# three = today_date - timedelta(days=3)
# two = today_date - timedelta(days=2)
# one = today_date - timedelta(days=1)