from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *


# Create a class for the GUI - initialise with title, close window button
class PdfGUI:
    def __init__(self, master):
        self.master = master
        master.title = 'PDF Merger'

        self.quit_button = Button(master, text="Close Window", command=master.quit)
        self.quit_button.pack()

root = Tk()
app = PdfGUI(master=root)
root.mainloop()


