import pytest
from unittest.mock import patch, MagicMock
from src.ContentEnricher import ContentEnricher

@pytest.fixture
def setup_content_enricher():
    # Crear instancias mock de las dependencias
    ui_mock = MagicMock()
    scraper_mock = MagicMock()
    translator_mock = MagicMock()
    
    # Configurar el objeto de la clase principal
    content_enricher_instance = ContentEnricher()
    content_enricher_instance.ui = ui_mock
    content_enricher_instance.scraper = scraper_mock
    content_enricher_instance.translator = translator_mock
    
    return ui_mock, scraper_mock, translator_mock, content_enricher_instance

def test_content_enricher_success(setup_content_enricher):
    ui_mock, scraper_mock, translator_mock, content_enricher_instance = setup_content_enricher
    
    # Configurar los mocks para devolver valores esperados
    ui_mock.generateSearchTerm.return_value = "Python_(programming_language)"
    ui_mock.translator.return_value = "y"
    ui_mock.saveFile.return_value = ("test_output", "pdf")

    scraper_mock.scrapebot.return_value = [
        "Python is a programming language.",
        "It is used widely."
    ]
    translator_mock.translateText.return_value = "Python es un lenguaje de programación."

    with patch('src.ContentEnricher.SaveFile') as MockSaveFile:
        mock_save_file_instance = MockSaveFile.return_value
        
        content_enricher_instance.process()
        
        # Verificar que los métodos del scraper y del traductor se llamaron
        scraper_mock.scrapebot.assert_called_once_with('https://es.wikipedia.org/wiki/Python_(programming_language)')
        translator_mock.translateText.assert_called_once_with(
            "Python is a programming language.\nIt is used widely.",
            "auto", "en"
        )
        
        # Verificar que se llamó al método de guardado del archivo PDF
        mock_save_file_instance.saveAsPdf.assert_called_once_with("test_output.pdf")
