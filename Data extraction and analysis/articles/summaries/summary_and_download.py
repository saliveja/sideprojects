import summary
import download as d
import summary_medium as sm
import download_medium as dm


def dictionary():

    dict = {
        "Knower's substack": {"https://theknower.substack.com/archive": 9},
        "Wrong a lot": {"https://wrongalot.substack.com/archive": 9},
        "Kyla": {"https://kyla.substack.com/archive": 9},
        "Ansem": {"https://blknoiz06.substack.com/archive": 5},
        "Cobie": {"https://cobie.substack.com/archive": 5},
        "Scarpa": {"https://medium.com/@TraderScarpa/feed": 0},
        "Hayes": {"https://cryptohayes.medium.com/feed": 0},
        "Foo69": {"https://fooo69.medium.com/feed": 0},
        "Godcomplex182": {"https://medium.com/@godcomplex182/feed": 0},
        "Cryptocreddy": {"https://medium.com/@cryptocreddy/feed": 0},
        "0xgodking": {"https://medium.com/@0xgodking/feed": 0},
        "Onchain Wizard Newsletter": {
            "https://onchainwizard.substack.com/archive": 8},
        "No Sleep": {"https://nosleep.substack.com/archive": 6},
        "Kyle's Newsletter": {"https://0xfren.substack.com/archive": 6},
        "The Reading Ape Newsletter": {
            "https://thereadingape.substack.com/archive": 10},
        "Nat's Newsletter": {"https://crypto.nateliason.com/": 15},
        "Rain And Coffee Newsletter": {
            "https://rainandcoffee.substack.com/archive": 10},
        "The Macro Compass Newsletter": {
            "https://themacrocompass.substack.com/archive": 10},
        "Not Boring Newsletter": {"https://www.notboring.co/": 19},
    }
    return dict


def article_summary():
    """Printing a list of articles and the summary of each."""

    dict = dictionary()

    for item, ln_ix in dict.items():
        for link, index in ln_ix.items():
            if link.endswith('feed'):
                name, sum, address = sm.sum_medium(item, link, index)
            else:
                name, sum, address = summary.summary(item, link, index)
        print(f"\n{name}:\n{sum}")
        print(address)

    print("\n")
    for i, item in enumerate(dict, 1):
        print(f"{i} - {item.strip()}")
            # 'end' is what is happening before the number (i)
            # 'sep' is what is happening after the number (i)
    print("\n")


def download():
    """Downloading selected article."""

    dict = dictionary()

    l_dict = []

    while True:
        for key, value in dict.items():
            dc = {key: value}
            l_dict.append(dc)

        select = int(input("\nWith index number, select the article you "
                                        "would like to download: "))
        item = l_dict[select - 1]

        for key, value in item.items():
            name = str(key)
            for url, ix in value.items():
                link = str(url)
                index = ix
                if url.endswith('feed'):
                    dm.download_medium(name, link, index)
                else:
                    d.article_download(name, link, index)

        answer_to_question = \
            input("Do you want to download another article? y/n ")

        if answer_to_question.lower() == "n":
            print("enjoy")
            quit()
        else:
            continue


article_summary()
download()
