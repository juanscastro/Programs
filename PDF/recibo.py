

from PyPDF2 import PdfReader

pdfFileObj = open('PDF\\recibo.pdf')

reader = PdfReader('PDF\\recibo.pdf')

paginas = len(reader.pages)
print(paginas)

page = reader.pages[0]
text = page.extract_text()
print(text)
