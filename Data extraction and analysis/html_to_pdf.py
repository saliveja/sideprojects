from wkhtmltopdf import WKHtmlToPdf
import datetime

sources = {'Hayes': 'https://cryptohayes.medium.com/',
           'Su Zhu & Hasu': 'https://uncommoncore.co/',
           'Our network': 'https://ournetwork.substack.com/',
           'Messari': 'https://messari.io/research',
           '0xparc': 'https://0xparc.org/blog',
           'Mycelium': 'https://mycelium.xyz/research',
           'Paradigm': 'https://www.paradigm.xyz/writing',
           'Credit Suisse': 'https://www.credit-suisse.com/marketinsights'
                            '/nl/en.html',
           'Metagovernance project': 'https://metagov.org/',
           'Bitmex': 'https://blog.bitmex.com/?lang=en_us',
}
print(sources)

for key, value in sources.items():
    wkhtmltopdf = WKHtmlToPdf(url = value, output_file= f"/home/sage/Desktop/Python"
                                                  f"/sideprojects/{key}.pdf",)
    for info in value:
        today = datetime.date.today()
        past_week = today + datetime.timedelta(days=-7)
        wkhtmltopdf.render()


import bs4
soup = bs4.BeautifulSoup(page.content, 'lxml')
table = soup.find(name='table', attrs={'id':'tableID'})
