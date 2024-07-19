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
            lines = self.text.split('\n')

            for line in lines:
                wrapped_lines = self.wrap_text(line, width - 2 * x)
                for wrapped_line in wrapped_lines:
                    if y < 72:
                        c.showPage()
                        y = height - 72
                    c.drawString(x, y, wrapped_line)
                    y -= 12

            c.save()
            print(f"PDF file '{fileName}' created successfully.")
        except Exception as e:
            return f"An expected error was found: {e}"

    def saveAsTxt(self, fileName):
        try:
            with open(fileName, 'w', encoding='utf-8') as file:
                file.write(self.text)
            print(f"TXT file '{fileName}' created successfully.")
        except Exception as e:
            return f"An expected error was found: {e}"

    def wrap_text(self, text, max_width):
        from reportlab.pdfbase.pdfmetrics import stringWidth
        wrapped_lines = []
        words = text.split()
        line = ""
        for word in words:
            if stringWidth(line + " " + word, 'Helvetica', 12) <= max_width:
                line += " " + word if line else word
            else:
                wrapped_lines.append(line)
                line = word
        if line:
            wrapped_lines.append(line)
        return wrapped_lines