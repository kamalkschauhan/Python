import PyPDF2
pdfFileObj = open('TrainingTranscriptReport.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
txt = pageObj.extractText()
print(txt)
