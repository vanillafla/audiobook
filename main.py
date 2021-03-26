import pyttsx3
import PyPDF2

book = open('BTOM.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(15, pages):
    page = pdfReader.getPage(15)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()