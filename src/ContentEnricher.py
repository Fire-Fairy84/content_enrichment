import UserInteraction
from .Scraper import Scraper
from .Translator import Translator
from .CreateFile import SaveFile

class ContentEnricher:
    WikiBaseUrl = 'https://es.wikipedia.org/wiki/'

    def __init__(self):
        self.ui = UserInteraction()
        self.scraper = Scraper()
        self.translator = Translator()
        self.saveFile = None

    def process(self):
        searchTerm = self.ui.generateSearchTerm()
        translate = self.ui.translator()
        fileName, userFileExtension = self.ui.saveFile()

        searchUrl = self.WikiBaseUrl + searchTerm
        texts = self.scraper.scrapebot(searchUrl)
        print("===============================================")
        if translate.lower() == "y":
            translatedText = self.translator.translateText("\n".join(texts), "auto", "en")
            print("=== TEXTO TRADUCIDO A INGLÉS ===")
            print(translatedText)
            print("================================")
        elif translate.lower() == "n":
            self.saveFile = SaveFile("\n".join(texts))
            if userFileExtension == "pdf":
                self.saveFile.saveAsPdf(fileName + ".pdf")
            elif userFileExtension == "txt":
                self.saveFile.saveAsTxt(fileName + ".pdf")
            else:
                print("Unable to create file.")
            fileSaved = True