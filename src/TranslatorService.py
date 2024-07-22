from deep_translator import (GoogleTranslator)
from deep_translator.exceptions import TranslationNotFound


class TranslatorService:

    def __init__(self):
        pass

    def translateText(self, text, src_lang, target_lang):
        try:
            translatedText = GoogleTranslator(source=src_lang, target=target_lang).translate(text)
            return translatedText
        except TranslationNotFound:
            return "Traducción no encontrada"
        except Exception as e:
            return f"Error: {e}"

