from deep_translator import (GoogleTranslator)
from deep_translator.exceptions import TranslationNotFound


class Translator:

    def __init__(self):
        pass

    def translateText(self, text, src_lang, target_lang):
        try:
            translatedText = GoogleTranslator(source=src_lang, target=target_lang).translate(text)
            return translatedText
        except TranslationNotFound:
            return "Translation not found"
        except Exception as e:
            return f"An unexpected error was found: {e}"

