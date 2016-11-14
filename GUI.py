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
        self.quit_button.pack()

        # File 1 label
        self.first_file_label = Label(master, text='Select a file')
        self.first_file_label.pack()

        # File 1 browse button - Command argument as a lambda function so does not run upon startup
        self.first_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser())
        self.first_file_browser.pack()

        # File 2 label
        self.second_file_label = Label(master, text='Select a file')
        self.second_file_label.pack()

        # File 2 browse button
        self.second_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser())
        self.second_file_browser.pack()

    # Function to open file browser
    def file_browser(self):
        self.file_name = filedialog.askopenfilename()


if __name__ == '__main__':
    root = Tk()
    app = PdfGUI(master=root)
    root.mainloop()


