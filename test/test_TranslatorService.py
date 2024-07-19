from unittest.mock import patch, MagicMock
from deep_translator.exceptions import TranslationNotFound
from src.TranslatorService import TranslatorService


def test_translateText_success():
    translator = TranslatorService()
    text = "Hello"
    src_lang = "en"
    target_lang = "es"
    expected_translation = "Hola"

    with patch('src.TranslatorService.GoogleTranslator') as MockTranslator:
        instance = MockTranslator.return_value
        instance.translate.return_value = expected_translation

        translated_text = translator.translateText(text, src_lang, target_lang)

        assert translated_text == expected_translation


def test_translateText_unsupported_language():
    translator = TranslatorService()
    text = "Hello"
    src_lang = "en"
    target_lang = "unsupported_lang"

    with patch('src.TranslatorService.GoogleTranslator') as MockTranslator:
        instance = MockTranslator.return_value
        instance.translate.side_effect = Exception("Unsupported language")

        translated_text = translator.translateText(text, src_lang, target_lang)

        assert translated_text == "An unexpected error was found: Unsupported language"


def test_translateText_translation_not_found():
    translator = TranslatorService()
    text = "Hello"
    src_lang = "en"
    target_lang = "es"

    with patch('src.TranslatorService.GoogleTranslator') as MockTranslator:
        instance = MockTranslator.return_value
        instance.translate.side_effect = TranslationNotFound("val")

        translated_text = translator.translateText(text, src_lang, target_lang)

        assert translated_text == "Translation not found"