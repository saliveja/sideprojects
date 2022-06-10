import requests, bs4

# res = requests.get("https://nostarch.com")
# # downloads the main page from No Starch
# res.raise_for_status()
# # checking for errors
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# # parse = analysera. Processing information
# type(noStarchSoup)

# url = 'https://cryptohayes.medium.com/energy-cancelled-e9f9e53a50cd'
#
# # Initialize html variable where html from url is stored
# html = ''
#
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# with urlopen(req) as response:
#    html = response.read()
arthurHtml = requests.get('https://cryptohayes.medium.com/')
arthurHtml.raise_for_status()
htmlSoup = bs4.BeautifulSoup(arthurHtml.text, 'html.parser')
elems = htmlSoup.select('rss')
print(elems)
print(type(elems))
# returns <class 'list>
len(elems)
# number of items
# type(elems[0])
# # what type index 0 is: <class 'bs4.element.Tag'>
# str(elems[0])
# # returns string including tags and author
# # <span id="author>Al Sweigart</span>
# elems[0].gettext()
# # returns the name of the author
# elems[0].attrs
# # returns the id