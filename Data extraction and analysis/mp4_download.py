import feedparser
import pdfkit
import requests, bs4
import re
from urllib.request import Request, urlopen
import wget
import os
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# url = 'https://events.coindesk.com/ce7f61f6-ebb9-44af-b326-7612613af9f0"'
# ext = 'mp4'
# wget.download(url, 'x.mp4')

def getAllPaths():
    # url = 'https://events.coindesk.com/consensus2022/agenda/session/902857'
    # ext = 'mp4'
    # fileUrl = []
    #
    # page = requests.get(url)
    # soup = bs4.BeautifulSoup(page.content, 'html5lib')
    #
    # element = soup.findAll('a')
    # print(element)
    #
    #

    browser = webdriver.Firefox()


    browser.get('https://events.coindesk.com/consensus2022/agenda/session/902857')
    button = browser.find_element(By.CLASS_NAME, 'broadcast-record-play-icon')
    button.click()
    # page_cookie = browser.find_element(By.ID, "CybotCookiebotDialogBody")
    # close_cookie = browser.find_element(By.ID, "CybotCookiebotBannerCloseButtonE2E")
    # close_cookie.click()
    close = browser.find_element(By.CLASS_NAME, "CybotCookiebotBannerCloseButton")
    close.click()

    # button_cookie = browser.find_element(By.ID,
    #                                      "CybotCookiebotDialogBodyLevelButtonAccept")
    #
    # for element in 'https://events.coindesk.com/consensus2022/agenda/session/902857':
    #     if element == page_cookie:
    #         button_cookie.click()

    time.sleep(5)

    login_button = browser.find_element(By.CLASS_NAME, "cta-button cta-button-large font-size-13 custom-color color-1-background  margin-top-medium color-1-hover-opacity")
    login_button.click()

# username_field = browser.find_element(By.CLASS_NAME, 'flex-item-fluid')
# username_field.send_keys('samuel.erixson@protonmail.com')
#
# password_field = browser.find_element(By.ID, 'password')
# password_field.send_keys('="`ZMwZ]L.~74M^%x_A\AS%PX>')
#
# username_field.send_keys('samuel.erixson@protonmail.com')
#
# next = browser.find_elements(By.CSS_SELECTOR, "css-901oao r-1awozwy "
#                                             "r-6koalj r-18u37iz r-16y2uox "
#                                             "r-37j5jr r-a023e6 r-b88u0q "
#                                             "r-1777fci r-rjixqe r-bcqeeo "
#                                             "r-q4m81j r-qvutc0")
#
# next.click()

#
# html
# body.color - 1 - background - opacity
# div.react - main
# div
# div.main - react - view.trade
# div.agenda - view.top - agenda - margin - double.agenda - view - -session

#
#         if (element.get('href').endswith(ext)):
#             fileUrl.append(node.get('href'))
#     print(fileUrl)
#
#     return fileUrl
#
#
# def downloadFile(downloadlink, fileName):
#     with requests.get(downloadlink, stream=True) as r:
#         r.raise_for_status()
#         filePath = os.path.join(destinationFolder, fileName)
#
#         print("Downloading to", os.path.abspath(filePath))
#         with open(filePath, 'wb') as f:
#
#             for chunk in r.iter_content(chunk_size=8 * 1024):
#
#                 if chunk:
#                     f.write(chunk)
#                     f.flush()
#         f.close()
# #
#
# result = getAllPaths(url, ext)
#
# for fileName in result:
#     downloadFile(url + fileName, fileName)
#     print(fileName + " Downloaded")


# def wrongALotKnower():
#     """Downloading the latest article from 'Wrong a lot'
#     and "Knower's substack"."""
#
#     links = []
#     urls = {
#         "Knower's substack": 'https://theknower.substack.com/archive',
#         "Wrong a lot": "https://wrongalot.substack.com/archive",
#         "Kyla": "https://kyla.substack.com/archive",
#            }
#
#     for key, value in urls.items():
#         res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
#         res.raise_for_status()
#         soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
#         for article in soup.find_all('a'):
#             links.append(article.get('href'))
#         address = links[9]
#         video = []
#
#        with open('texas_talk.mp4', 'wb') as t:
#                 t.write(f.read())
        #
        # print(f"Creating PDF from address: {address}")
        # pdfkit.from_url(address, f'{key}.pdf')
        # # converting html to pdf and downloading
        # print(f"Created PDF successfully!")
        # links.clear()

#
# mport
# requests
# from bs4 import BeautifulSoup
#
# Video_url = "https://file-examples.com/index.php/sample-video-files/sample-mp4-files/"
#
#
# def get_video_links():
#     # create response object
#     r = requests.get(Video_url)
#
#     # create beautiful-soup object
#     soup = BeautifulSoup(r.content, 'html5lib')
#
#     # find all links on web-page
#     links = soup.findAll('a')
#
#     # filter the link ending with .mp4
#     video_links = [Video_url + link['href'] for link in links if
#                    link['href'].endswith('mp4')]
#
#     return video_links
#
#
# def download_video():
#     '''Downloading video'''
#     link = "https://events.coindesk.com/ce7f61f6-ebb9-44af-b326-7612613af9f0"
#
#     file_name = link.split('/')[-1]
#     print("Downloading file:%s" % file_name)
#     r = requests.get(link, stream=True)
#
#     with open(file_name, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024 * 1024):
#             if chunk:
#                 f.write(chunk)
#
#     print("%s downloaded!\n" % file_name)

# getAllPaths('https://events.coindesk.com/consensus2022/agenda/session/902857', 'mp4')
#
# download_video()
getAllPaths()

# import re
# import json
# import requests
#
# url = "https://likee.video/hashtag/CuteHeadChallenge?lang=en"
# api_url = "https://api.like-video.com/likee-activity-flow-micro/videoApi/getEventVideo"
#
# payload = {
#     "country": "US",
#     "page": 1,
#     "pageSize": 28,
#     "topicId": "",
# }
#
# html_doc = requests.get(url).text
# data = re.search(r"window\.data = ({.*});", html_doc)[1]
# data = json.loads(data)
#
# payload["topicId"] = data["topicId"]
#
#
# data = requests.post(api_url, json=payload).json()
#
# # uncomment this to print all data:
# # print(json.dumps(data, indent=4))
#
# # print/save each videoUrl:
# for i, video in enumerate(data["data"]["videoList"], 1):
#     print("Downloading {} as {}.mp4".format(video["videoUrl"], i))
#     # download video
#     with open("{}.mp4".format(i), "wb") as f_out:
#         f_out.write(requests.get(video["videoUrl"]).content)

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
# making the folder xkcd
# or making an exception if the folder already exists

while not url.endswith('#'):
# the loop ends when the url ends with #
    print('Downloading page %s...' % url)
    # printing the url so we know which page we are downloading
    res = requests.get(url)
    # downloading url
    res.raise_for_status()
    # calling raise_the_status so that the download is stopped if
    # something went wrong

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # download page
    # find url
    # download image
    # save image to ./xkcd
    # get previous buttons url

    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # download image
        print('Downloading image %s...' f'{comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        # 'wb' --> write binary

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print("Done.")
