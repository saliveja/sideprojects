# scraping web pages

## Tags

There a different categories such as parent (the main in this case html), child (under parent) and if there are several inside the parent category, they are called siblings.
    • <html></html>
    • a – hyperlink
    • p – paragraph
    • <head> </head>
    • <body></body>
    • div — indicates a division, or area, of the page. 
    • b — bolds any text inside. 
    • i — italicizes any text inside. 
    • table — creates a table. 
    • form — creates an input form. 
requests.get() will download the contents of a web page
 
**Example:**
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page

We will get a response object after running this code:
page.status_code
200

This means it was successful
A code starting with 2 generally indicated success. Code starting with 4 or 5 indicates an error.

**This prints the html content:**

page.content

# beautiful soup

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
**importing the library beautiful soup and creating an instance of the class

**to print the content we use prettify method**

print(soup.prettify())

**get_text()**
This will get only the text we wish to scrape while prettify displays all html content
print(soup.get_text())

**Finding all instances of a tag**

- returns a list
- this uses the index method to to extract text
soup.find_all('p')[0].get_text()


**Finding first instance of a tag**

- will return a single beautiful soup object
soup.find('p')

**Downloading and creating a beautiful soup object**

page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup

## classes

**finding any parapgrapthat has the class outer_text**

soup.find_all('p', class_='outer-text')

**looking for tag that has the class outer-text**

soup.find_all(class_="outer-text")

**searching for elements by id**

soup.find_all(id="first")


**css selectors**

- p a — finds all a tags inside of a p tag.
- body p a — finds all a tags inside of a p tag inside of a body tag.
- html body — finds all body tags inside of an html tag.
- p.outer-text — finds all p tags with a class of outer-text.
- p#first — finds all p tags with an id of first.
- body p.outer-text — finds any p tags with a class of outer-text inside of a body tag.


**using CSS selectors to find all the p tags in our page that are inside of a div**

- select method returns a list
soup.select("div p")
 
**extracting info from the page**

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

# Panda

- pandas is a data analysis tool
import pandas as pd

- we can make a dictionary of the values we got from the web page by using panda DataFrame

import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
weather

## mean() function

- can be used to calculate mean/average of a given list of numbers
- if we work with dictionaries, mean only considers keys

import statistics
 
**list of positive integer numbers**

data1 = [1, 3, 4, 5, 7, 9, 2]
 
x = statistics.mean(data1)
 
**printing the mean**

print(f"Mean is :, {x}")
-  output: mean is : 4.428571428571429






