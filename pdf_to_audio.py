import PyPDF2
import pyttsx3
import pdfplumber


file = 'C:/Users/meet/Desktop/final version.pdf'

#creating a PDF file Object
pdfFileObj = open(file,'rb')

#creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#get the number of pages
pages = pdfReader.numPages

#create a pdfplumber object and loop through the pages
with pdfplumber.open(file) as pdf:
    #loop through the number of pages
    for i in range(0,pages):
        page=pdf.pages[i]
        text=page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()

