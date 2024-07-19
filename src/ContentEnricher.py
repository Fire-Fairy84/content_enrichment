from .UserInteraction import UserInteraction
from .Scraper import Scraper
from .TranslatorService import TranslatorService
from .CreateFile import SaveFile

class ContentEnricher:
    WikiBaseUrl = 'https://es.wikipedia.org/wiki/'

    def __init__(self):
        self.ui = UserInteraction()
        self.scraper = Scraper()
        self.translator = TranslatorService()
        self.saveFile = None

    def process(self):
        searchTerm = self.ui.generateSearchTerm()
        translate = self.ui.translator()
        fileName, userFileExtension = self.ui.saveFile()

        searchUrl = self.WikiBaseUrl + searchTerm
        texts = self.scraper.scrapebot(searchUrl)
        fullText = "\n".join(texts)
        print("===============================================")

        if translate.lower() == "y":
            translatedText = self.translator.translateText(fullText, "auto", "en")
            print("=== TEXTO TRADUCIDO A INGLÉS ===")
            print(translatedText)
            print("================================")
            self.saveFile = SaveFile(translatedText)
        else:
            self.saveFile = SaveFile(fullText)

        if userFileExtension == "pdf":
            self.saveFile.saveAsPdf(fileName + ".pdf")
        elif userFileExtension == "txt":
            self.saveFile.saveAsTxt(fileName + ".txt")
        else:
            print("Unable to create file.")
        fileSaved = True