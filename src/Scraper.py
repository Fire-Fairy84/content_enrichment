import string
import requests
from bs4 import BeautifulSoup
import lxml

userInput = input("Search topic: ")
capsInput = string.capwords(userInput)
lists = capsInput.split()
searchTerm = "_".join(lists)

url = 'https://en.wikipedia.org/wiki/'+searchTerm

def scrapebot(url):
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('header', class_='mw-body-header')
    title = box.find(id='firstHeading').get_text()
    print(title)
    for paragraph in soup.select('p', limit=5):
        print(paragraph.getText())

scrapebot(url)

