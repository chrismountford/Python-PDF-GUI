from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

def combine_pdf(file1, file2):
    output = PdfFileWriter()

    append_pdf(PdfFileReader(open(file1, 'rb')), output)
    append_pdf(PdfFileReader(open(file2, 'rb')), output)

    output.write(open(file1 + file2, 'wb'))
