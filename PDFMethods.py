from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import messagebox


def append_pdf(input, output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]


def combine_pdf(file1, file2, dir_name, output_name):
    output = PdfFileWriter()

    try:
        append_pdf(PdfFileReader(open(file1, 'rb')), output)
        append_pdf(PdfFileReader(open(file2, 'rb')), output)

    except FileNotFoundError:
        messagebox.showwarning(title="Error Opening File",
                               message="Please select a file that exists")

    try:
        output.write(open(dir_name + '/' + output_name + '.pdf', 'wb'))

    except PermissionError:
        messagebox.showerror(title="Error in Merged File Name",
                             message="Please enter a legal file name")
