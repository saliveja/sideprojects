
import summary
import download as d

def article_summary():
    """Printing a list of articles and the summary of each."""

    dict = {
        "Knower's substack": "https://theknower.substack.com/archive",
        "Wrong a lot": "https://wrongalot.substack.com/archive",
        "Kyla": "https://kyla.substack.com/archive",
        "Ansem": "https://blknoiz06.substack.com/archive",
        "Cobie": "https://cobie.substack.com/archive",
        "Scarpa": "https://medium.com/@TraderScarpa/feed",
        "Hayes": "https://cryptohayes.medium.com/feed",
        "Foo69": "https://fooo69.medium.com/feed",
        "Godcomplex182": "https://medium.com/@godcomplex182/feed",
        "Cryptocreddy": "https://medium.com/@cryptocreddy/feed",
        "0xgodking": "https://medium.com/@0xgodking/feed",
        "Onchain Wizard Newsletter": "https://onchainwizard.substack.com/archive",
        "No Sleep": "https://nosleep.substack.com/archive",
        "Kyle's Newsletter": "https://0xfren.substack.com/archive",
        "The Reading Ape Newsletter": "https://thereadingape.substack.com/archive",
        "Nat's Newsletter": "https://crypto.nateliason.com/",
        "Rain And Coffee Newsletter": "https://rainandcoffee.substack.com/archive",
        "The Macro Compass Newsletter": "https://themacrocompass.substack.com/archive",
        "Not Boring Newsletter": "https://www.notboring.co/",
            }

    for i, item in enumerate(dict, 1):
        print(f"{i} - {item.strip()}")
            # 'end' is what is happening before the number (i)
            # 'sep' is what is happening after the number (i)
    print("\n")

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

    index_9 = {
        "Knower's substack": "https://theknower.substack.com/archive",
        "Wrong a lot": "https://wrongalot.substack.com/archive",
        "Kyla": "https://kyla.substack.com/archive",
               }

    index_5 = {
        "Ansem": "https://blknoiz06.substack.com/archive",
        "Cobie": "https://cobie.substack.com/archive",
            }

    for key, value in index_9.items():
        name,sum = summary.summary(key, value, 9)
        print(f"\n{name}:\n{sum}")
    for key, value in index_9.items():
        name,sum = summary.summary(key, value, 5)
        print(f"\n{name}:\n{sum}")





def download():
    """Selecting articles and downloading."""

    d.article_download( "Knower's substack",
                               "https://theknower.substack.com/archive", 9)

while True:
    index = int(input("With index number, select the article you "
                                   "would like to download: "))
    for k, v in dict.items():
            for index in articles:
                if index == k:
                    n[k] = v
        answer_to_question = \
            input("Do you want to download another article? y/n ")
        if answer_to_question == 'n':
            print("enjoy")
            quit()
        else:
            continue


article_summary()
# download()


# def print_letter(letter):
#     print(f"this is the letter: {letter}")
#
#
# letters = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
# ]
#
#
# def return_letter(index):
#     letter = letters[index]
#
#
# index = 3  # the users input()
#
# letter = return_letter(index)
# print_letter(letter)