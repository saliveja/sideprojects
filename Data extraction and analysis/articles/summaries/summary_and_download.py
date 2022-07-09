# from newspaper import Article
# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation
# from heapq import nlargest
# import feedparser
# import requests, bs4
# import summarize
# import ansem as a
# import ape
# import cobie as c
# import cryptocreddy as cr
# import foo69 as f
# import godcomplex182 as god
# import hayes as h
# import knower as k
# import kyla
# import kyle
# import macro_compass as mc
# import nat
# import no_sleep as ns
# import not_boring as nb
# import onchain_wizard as ow
# import oxgodking as ox
# import rain_and_coffee as rc
# import scarpa as s
# import wrong_a_lot as w
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

    name,sum = summary.summary("Knower","https://theknower.substack.com/archive", 9)
    print(f"\n{name}:\n{sum}")


def download():
    """Selecting articles and downloading."""

    d.article_download( "Knower's substack",
                               "https://theknower.substack.com/archive", 9)

# articles = [
#         k.knower_download(),
#         w.wrong_download(),
#         a.ansem_download(),
#         c.cobie_download(),
#         s.scarpa_download(),
#         h.hayes_download(),
#         f.foo69_download(),
#         god.godcomplex182_download(),
#         cr.cryptocreddy_download(),
#         ox.oxgodking_download(),
#         ow.onchainWizard_download(),
#         ns.noSleep_download(),
#         kyle.kyle_download(),

    #     nat.nat_download(),
    #     rc.rainCoffee_download(),
    #     mc.macroCompass_download(),
    #     nb.notBoring_download(),
    #     kyla.kyla_download(),
    # ]


# while True:
#     index = int(input("With index number, select the article you "
#                                    "would like to download: "))
#     for k, v in dict.items():
#             for index in articles:
#                 if index == k:
#                     n[k] = v
#         answer_to_question = \
#             input("Do you want to download another article? y/n ")
#         if answer_to_question == 'n':
#             print("enjoy")
#             quit()
#         else:
#             continue
#






    #     if select_article == "1":
    #         k.knower_download()
    #         answer_to_question = "Do you want to download another article? y/n "
    #         if answer_to_question == 'n':
    #             print("enjoy")
    #             quit()
    #         else:
    #             download()
    #     elif select_article == "2":
    #         w.wrong_download()
    #         answer_to_question = "Do you want to download another article? y/n "
    #         if answer_to_question == 'n':
    #             print("enjoy")
    #             quit()
    #         else:
    #             download()
    #     elif select_article == "3":
    #         w.wrong_download()
    #         answer_to_question = "Do you want to download another article? y/n "
    #         if answer_to_question == 'n':
    #             print("enjoy")
    #             quit()
    #         else:
    #             download()

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