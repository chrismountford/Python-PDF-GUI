# TODO: Layout of app
# TODO: Dynamic UI to allow for multiple merges
# TODO: Build in PDF functionality
# TODO: Turn labels into entry boxes

from tkinter import *
from tkinter import filedialog
import PDFMethods


# Create a class for the GUI - initialise with title, close window button
class PdfGUI:
    def __init__(self, master):
        self.master = master
        master.title = 'PDF Merger'
        master.geometry("400x300")

        self.file_name_text = StringVar()
        self.file_name2_text = StringVar()

        # Quit app button
        self.quit_button = Button(master, text='Close Window', command=master.quit)

        # File 1
        self.first_file_label = Label(master, text='Select a file')

        # Command argument as a lambda function so does not run upon startup
        self.first_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser())

        self.first_select_label = Entry(master, textvariable=self.file_name_text)

        # File 2
        self.second_file_label = Label(master, text='Select a file')

        self.second_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser2())

        self.second_select_label = Entry(master, textvariable=self.file_name2_text)

        # Output naming
        self.merged_file_name = Entry(master)

        # Merge button

        self.merge_button = Button(master, text='Merge',
                                   command=lambda:
                                   PDFMethods.combine_pdf(self.file_name_text.get(), self.file_name2_text.get(),
                                                          self.merged_file_name.get()))

        # LAYOUT #

        self.first_file_label.grid(row=0, column=0)
        self.first_file_browser.grid(row=0, column=1)
        self.first_select_label.grid(row=0, column=2)

        self.second_file_label.grid(row=1, column=0)
        self.second_file_browser.grid(row=1, column=1)
        self.second_select_label.grid(row=1, column=2)

        self.merged_file_name.grid(row=2, column=0)

        self.merge_button.grid(row=3, column=0)

        self.quit_button.grid(row=10, column=1)

    # Function to open file browser
    def file_browser(self):
        file_name = filedialog.askopenfilename()
        self.file_name_text.set(file_name)

    def file_browser2(self):
        file_name2 = filedialog.askopenfilename()
        self.file_name2_text.set(file_name2)

if __name__ == '__main__':
    root = Tk()
    app = PdfGUI(master=root)
    root.mainloop()
