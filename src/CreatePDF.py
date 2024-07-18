import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class SaveFile:
    def __init__(self, text):
        self.text = text
    def saveAsPdf(self, fileName):
        try:
            c = canvas.Canvas(fileName, pagesize=letter)
            width, height = letter
            x = 72
            y = height - 72
            c.drawString(x, y, self.text)
            c.save()
        except Exception as e:
            return f"An expected error was found: {e}"
    def saveAsTxt(self, fileName):
        try:
            with open(fileName, 'w') as file:
                file.write(self.text)
        except Exception as e:
            return f"An expected error was found: {e}"


text = "Aquí irá el texto enriquecido y traducido."
save_file = SaveFile(text)

fileNamePdf = "file.pdf"
save_file.saveAsPdf(fileNamePdf)

fileNameTxt = "file.txt"
save_file.saveAsTxt(fileNameTxt)
