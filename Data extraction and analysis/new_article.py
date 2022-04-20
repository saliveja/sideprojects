from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://cryptohayes.medium.com/energy-cancelled-e9f9e53a50cd'

# Initialize html variable where html from url is stored
# html = ''

# Pretend we're running firefox to fool Medium into allowing us to scrape
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

filename = 'beautiful.txt'
with open(filename, 'a') as f:
    with urlopen(req) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        #  is where a string of commands – usually a program –
        #  is separated into more easily processed components,
        #  which are analyzed for correct syntax and
        #  then attached to tags that define each component.
        extracted_text = soup.get_text()
        # The get_text() method returns the text inside the Beautiful Soup
        # or Tag object as a single Unicode string.
        pretty_text = soup.prettify()
        f.write(pretty_text)

# Parse with beautiful soup

#
# print(soup.get_text())
#
# import urllib.request
# with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
#
# import shutil
# import tempfile
# import urllib.request
#
# with urllib.request.urlopen('http://python.org/') as response:
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         shutil.copyfileobj(response, tmp_file)
#
# with open(tmp_file.name) as html:
#     pass