import requests
from bs4 import BeautifulSoup
import lxml

class Scraper:
    def __init__(self):
        pass
    def scrapebot(self, url):
        try:
            texts = []
            page = requests.get(url)
            content = page.text
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('header', class_='mw-body-header')
            title = box.find(id='firstHeading').get_text()
            print("===== INFORMACIÓN ENCONTRADO SOBRE EL TEMA =====")
            print(title)
            for paragraph in soup.select('p', limit=5):
                texts.append(paragraph.getText())
                print(paragraph.getText())
            return texts
        except requests.RequestException as e:
            print(f'Request error: {e}')
            return None
        except Exception as e:
            print(f'Error: {e}')
            return None
