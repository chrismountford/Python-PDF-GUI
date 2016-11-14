# TODO: Layout of app
# TODO: Dynamic UI to allow for multiple merges
# TODO: Set file names to labels

from tkinter import *
from tkinter import filedialog


# Create a class for the GUI - initialise with title, close window button
class PdfGUI:
    def __init__(self, master):
        self.master = master
        master.title = 'PDF Merger'
        master.geometry("800x600")

        self.file_name_text = StringVar()
        self.file_name2_text = StringVar()

        # Quit app button
        self.quit_button = Button(master, text='Close Window', command=master.quit)

        # File 1 label
        self.first_file_label = Label(master, text='Select a file')

        # File 1 browse button - Command argument as a lambda function so does not run upon startup
        self.first_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser())

        # File 1 selected
        self.first_select_label = Label(master, textvariable=self.file_name_text)

        # File 2 label
        self.second_file_label = Label(master, text='Select a file')

        # File 2 browse button
        self.second_file_browser = Button(master, text='Browse...', command=lambda: self.file_browser2())

        # File 2 selected
        self.second_select_label = Label(master, textvariable=self.file_name2_text)

        # LAYOUT #

        self.first_file_label.grid(row=0, column=0)
        self.first_file_browser.grid(row=0, column=1)
        self.first_select_label.grid(row=0, column=2)
        self.second_file_label.grid(row=1, column=0)
        self.second_file_browser.grid(row=1, column=1)
        self.second_select_label.grid(row=1, column=2)
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


