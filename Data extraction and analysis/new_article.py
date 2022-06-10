from bs4 import BeautifulSoup as bs
import requests
from urllib.request import Request, urlopen

url = 'https://cryptohayes.medium.com/energy-cancelled-e9f9e53a50cd'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

filename = 'beautiful.txt'
with open(filename, 'a') as f:
    with urlopen(req) as response:
        html = response.read()
        soup = bs(html, 'html.parser')
        #  is where a string of commands – usually a program –
        #  is separated into more easily processed components,
        #  which are analyzed for correct syntax and
        #  then attached to tags that define each component.
        # extracted_text = soup.get_text()
        # # The get_text() method returns the text inside the Beautiful Soup
        # # or Tag object as a single Unicode string.
        # string_text = str(extracted_text)
        pretty_text = soup.prettify()
        f.write(pretty_text)

        print(soup.title)
        print(soup.title.name)
        print(soup.title.parent.name)
        s = soup.find('section', class_ ='pw-post-body-paragraph jf jg ii jh b ji '
                                    'll jk jl jm lm jo jp jq ln js jt ju lo '
                                    'jw jx jy lp ka kb kc ib gj')

        contents = s.find_all('p')
        for content in contents:
            print(content.text)

