import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class SaveFile:
    def __init__(self, text):
        self.text = text
    def saveAsPdf(self, fileName):
        c = canvas.Canvas(fileName, pagesize=letter)
        width, height = letter
        x = 72
        y = height - 72
        c.drawString(x, y, self.text)
        c.save()
    def saveAsTxt(self, fileName):
        with open(fileName, 'w') as file:
            file.write(self.text)


text = "Aquí irá el texto enriquecido y traducido."
save_file = SaveFile(text)

fileNamePdf = "file1.pdf"
save_file.saveAsPdf(fileNamePdf)

fileNameTxt = "file1.txt"
save_file.saveAsTxt(fileNameTxt)
