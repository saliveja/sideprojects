import feedparser
import pdfkit
import requests, bs4

def article_download(name, link, index):

    # url = {
    #     "The Reading Ape Newsletter": "https://thereadingape.substack.com/archive",
    #        }

    res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    links = []
    for article in soup.find_all('a'):
        links.append(article.get('href'))

    address = links[index]

    print(f"Creating PDF from address: {address}")
    pdfkit.from_url(address, f'{name}.pdf')
    # converting html to pdf and downloading
    print(f"Created PDF successfully!")





    # links = []
    # urls = {
    #     "Knower's substack": 'https://theknower.substack.com/archive',
    #     "Wrong a lot": "https://wrongalot.substack.com/archive",
    #     "Kyla": "https://kyla.substack.com/archive",
    #     "Cobie": "https://cobie.substack.com/archive",
    #     "Ansem": "https://blknoiz06.substack.com/archive",
    #     'Onchain Wizard Newsletter': 'https://onchainwizard.substack.com/archive',
    #     'No Sleep': 'https://nosleep.substack.com/archive',
    #     "Kyle's Newsletter": 'https://0xfren.substack.com/archive',
    #     "The Reading Ape Newsletter": "https://thereadingape.substack.com/archive,",
    #     "Nat's Newsletter": 'https://crypto.nateliason.com/',
    #     "Rain And Coffee Newsletter": 'https://rainandcoffee.substack.com/archive',
    #     "The Macro Compass Newsletter": 'https://themacrocompass.substack.com/archive',
    #     "Not Boring Newsletter": "https://www.notboring.co/",
    #            }
    #
    # urls_medium = {
    #     'Scarpa': 'https://medium.com/@TraderScarpa/feed',
    #     'Hayes': 'https://cryptohayes.medium.com/feed',
    #     'Foo69': 'https://fooo69.medium.com/feed',
    #     'Godcomplex182': 'https://medium.com/@godcomplex182/feed',
    #     'Cryptocreddy': 'https://medium.com/@cryptocreddy/feed',
    #     '0xgodking': 'https://medium.com/@0xgodking/feed',
    #             }
    #
    # for key, value in urls.items():
    #     res = requests.get(urls[key], headers={'User-Agent': 'Mozilla/5.0'})
    #     res.raise_for_status()
    #     soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #
    #     for each_article in soup.find_all('a'):
    #         x = each_article.get('href')
    #
    #
    # for key, value in urls_medium.items():
    #     feed = feedparser.parse(value)
    #     for entry in feed.entries:
    #         latest_article = entry.link
    #         name = entry.title
    #         links.append(latest_article)
    #
    # print(links)
    #
    # #
    # #     links = {
    # #         "Knower's substack": soup.find_all('a')[9],
    # #         "Wrong a lot": soup.find_all('a')[9],
    # #         "Kyla": soup.find_all('a')[9],
    # #         "Cobie": "https://cobie.substack.com/archive",
    # #         "Ansem": "https://blknoiz06.substack.com/archive",
    # #         'Onchain Wizard Newsletter': 'https://onchainwizard.substack.com/archive',
    # #         'No Sleep': 'https://nosleep.substack.com/archive',
    # #         "Kyle's Newsletter": 'https://0xfren.substack.com/archive',
    # #         "The Reading Ape Newsletter": "https://thereadingape.substack.com/archive,",
    # #         "Nat's Newsletter": 'https://crypto.nateliason.com/',
    # #         "Rain And Coffee Newsletter": 'https://rainandcoffee.substack.com/archive',
    # #         "The Macro Compass Newsletter": 'https://themacrocompass.substack.com/archive',
    # #         "Not Boring Newsletter": "https://www.notboring.co/",
    # #     }
    #     knower = soup.find_all('a')[9]
    #     wrong = soup.find_all('a')[9]
    #     Kyla = soup.find_all('a')[9]
    #     cobie = soup.find_all('a')[5]
    #     ansem = soup.find_all('a')[5]
    #     owizard = soup.find_all('a')[8]
    #     nosleep = soup.find_all('a')[6]
    #     Kyle = soup.find_all('a')[6]
    #     ape = soup.find_all('a')[10]
    #     rain = soup.find_all('a')[10]
    #     macro = soup.find_all('a')[10]
    #     nat = soup.find_all('a')[15]
    #     notboring = soup.find_all('a')[19]
    #     scarpa = soup.find_all('a')[0]
    #     hayes = soup.find_all('a')[0]
    #     foo69 = soup.find_all('a')[0]
    #     godcomplex182 = soup.find_all('a')[0]
    #     cryptocreddy = soup.find_all('a')[0]
    #     oxgodking = soup.find_all('a')[0]
    #     #
    #     # for key, value in links.items():
    #     #     print(value)