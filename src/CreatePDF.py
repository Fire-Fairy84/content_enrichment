from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from reportlab.pdfgen import canvas
from src.Scraper import Scraper

class SaveFile:
    def __init__(self, text):
        self.text = text

    def saveAsPdf(self, fileName):
        try:
            c = canvas.Canvas(fileName, pagesize=letter)
            width, height = letter
            x = 72
            y = height - 72
            margin_right = 72  # margen derecho
            max_width = width - x - margin_right  # ancho máximo del texto

            # Ajuste del texto al ancho máximo permitido
            lines = self.text.split('\n')
            wrapped_lines = []
            for line in lines:
                wrapped_line = utils.simpleSplit(line, c._fontname, c._fontsize, max_width)
                wrapped_lines.extend(wrapped_line)

            for line in wrapped_lines:
                if y < 72:  # Verificar si queda espacio suficiente para escribir
                    c.showPage()
                    y = height - 72
                c.drawString(x, y, line)
                y -= 12

            c.save()
            return f"Archivo PDF guardado exitosamente como {fileName}"
        except Exception as e:
            return f"Se encontró un error inesperado: {e}"

    def saveAsTxt(self, fileName):
        try:
            with open(fileName, 'w', encoding='utf-8') as file:
                file.write(self.text)
            return f"Archivo de texto guardado exitosamente como {fileName}"
        except Exception as e:
            return f"Se encontró un error inesperado: {e}"

# Crear una instancia del scraper y obtener los datos
scraper = Scraper()
url = "https://es.wikipedia.org/wiki/Inteligencia_artificial"
result = scraper.scrapebot(url)

# Verificar que result es una lista
if result and isinstance(result, list):
    # La primera entrada de la lista es el título
    title = result[0]
    # Las siguientes entradas son los párrafos
    paragraphs = result[1:]

    # Unir el título y los párrafos en un solo texto
    full_text = f"{title}\n\n" + "\n\n".join(paragraphs)

    # Guardar el texto en PDF y TXT
    save_file = SaveFile(full_text)

    fileNamePdf = "file.pdf"
    print(save_file.saveAsPdf(fileNamePdf))

    fileNameTxt = "file.txt"
    print(save_file.saveAsTxt(fileNameTxt))
else:
    print("Error: el scraping no devolvió un resultado válido.")


"""
text = "Aquí irá el texto enriquecido y traducido."
save_file = SaveFile(text)

fileNamePdf = "file.pdf"
save_file.saveAsPdf(fileNamePdf)

fileNameTxt = "file.txt"
save_file.saveAsTxt(fileNameTxt)
"""
