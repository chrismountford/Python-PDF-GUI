# TODO: Layout of app
# TODO: Dynamic UI to allow for multiple merges

from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog


# Create a class for the GUI - initialise with title, close window button
class PdfGUI:
    def __init__(self, master):
        self.master = master
        master.title = 'PDF Merger'

        # Quit app button
        self.quit_button = Button(master, text='Close Window', command=master.quit)

        # File 1 label
        self.first_file_label = Label(master, text='Select a file')

        # File 1 browse button - Command argument as a lambda function so does not run upon startup
        self.first_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser())

        # File 2 label
        self.second_file_label = Label(master, text='Select a file')

        # File 2 browse button
        self.second_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser())

        # Layout

        self.first_file_label.grid(row=0, column=0)
        self.first_file_browser.grid(row=0, column=1)
        self.second_file_label.grid(row=1, column=0)
        self.second_file_browser.grid(row=1, column=1)
        self.quit_button.grid(row=10, column=1)

    # Function to open file browser
    def file_browser(self):
        self.file_name = filedialog.askopenfilename()

    # def create_button(self):

if __name__ == '__main__':
    root = Tk()
    app = PdfGUI(master=root)
    root.mainloop()


