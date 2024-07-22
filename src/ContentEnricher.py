from .UserInteraction import UserInteraction
from .Scraper import Scraper
from .TranslatorService import TranslatorService
from .SaveFile import SaveFile

class ContentEnricher:
    WikiBaseUrl = 'https://es.wikipedia.org/wiki/'

    def __init__(self):
        self.ui = UserInteraction()
        self.scraper = Scraper()
        self.translator = TranslatorService()
        self.saveFile = None

    def process(self):
        try:
            searchTerm = self.ui.generateSearchTerm()
        except Exception as e:
            print(f"Search input error: {e}")
            return

        try:
            translate = self.ui.translator()
        except Exception as e:
            print(f"Translate input error: {e}")
            return

        try:
            fileName, userFileExtension = self.ui.saveFile()
        except Exception as e:
            print(f"Filename or extension input error: {e}")
            return

        searchUrl = self.WikiBaseUrl + searchTerm

        try:
            texts = self.scraper.scrapebot(searchUrl)
            if texts is None:
                print("No information found.")
                return
            fullText = "\n".join(texts)
        except Exception as e:
            print(f"Error scraping: {e}")
            return

        print("===============================================")

        try:
            if translate.lower() == "y":
                translatedText = self.translator.translateText(fullText, "auto", "en")
                print("=== TEXTO TRADUCIDO A INGLÉS ===")
                print(translatedText)
                print("================================")
                self.saveFile = SaveFile(translatedText)
            else:
                self.saveFile = SaveFile(fullText)
        except Exception as e:
            print(f"Error translating: {e}")
            return

        try:
            if userFileExtension == "pdf":
                self.saveFile.saveAsPdf(fileName + ".pdf")
            elif userFileExtension == "txt":
                self.saveFile.saveAsTxt(fileName + ".txt")
            else:
                print("Could not create file.")
        except Exception as e:
            print(f"Error saving file: {e}")
            return

        fileSaved = True
