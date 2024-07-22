import pytest
import os
from src.SaveFile import SaveFile

@pytest.fixture
def sample_text():
    return "Este es un texto de prueba.\nTiene varias líneas.\nFin del texto."

@pytest.fixture
def save_file(sample_text):
    return SaveFile(sample_text)

def test_save_as_pdf(save_file):

    fileName = "test_output.pdf"
    save_file.saveAsPdf(fileName)
    assert os.path.exists(fileName), "El archivo PDF no se creó correctamente."
    os.remove(fileName)

def test_save_as_txt(save_file):

    fileName = "test_output.txt"
    save_file.saveAsTxt(fileName)
    assert os.path.exists(fileName), "El archivo TXT no se creó correctamente."
    os.remove(fileName)
