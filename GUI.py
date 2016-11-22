# TODO: Layout of app
# TODO: Dynamic UI to allow for multiple merges
# TODO: Add in error handling
# TODO: Default select file text in select labels

from tkinter import *
from tkinter import filedialog
import PDFMethods


bg_col = '#DCDCDC'
font_style = 'Helvetica'


# Create a class for the GUI
class PdfGUI:
    def __init__(self, master):
        self.master = master
        master.title('PDF Merger')
        master.geometry("500x300")

        master.configure(background=bg_col)

        # Make these instances of a class?
        self.frame0 = Frame(master, bg=bg_col)
        self.frame1 = Frame(master, bg=bg_col)
        self.frame2 = Frame(master, bg=bg_col)
        self.frame3 = Frame(master, bg=bg_col)

        self.file_name_text = StringVar()
        self.file_name_text.set('')
        self.file_name2_text = StringVar()
        self.save_dir_text = StringVar()

        self.sel_file_text = StringVar()
        self.sel_file_text.set('Please select a file')

        # Title
        self.title_label = Label(self.frame0, text='PDF Merger', font=(font_style, 16), bg=bg_col)

        # File 1
        self.first_file_label = Label(self.frame1, text='Select a file:', bg=bg_col)
        # Command argument as a lambda function so does not run upon startup
        self.first_file_browser = Button(self.frame1, text='Select a file', command=lambda: self.file_browser())
        self.first_select_label = Label(self.frame1, textvariable=self.file_name_text, bg=bg_col)

        # File 2
        self.second_file_label = Label(self.frame1, text='Select a file:', bg=bg_col)
        self.second_file_browser = Button(self.frame1, text='Select a file', command=lambda: self.file_browser2())
        self.second_select_label = Label(self.frame1, textvariable=self.file_name2_text, bg=bg_col)

        # Output naming
        self.merged_file_name = Entry(self.frame2)
        self.merged_file_label = Label(self.frame2, text='Select a directory:', bg=bg_col)
        self.merged_directory_browser = Button(self.frame2, text='Select a directory', command=lambda: self.save_dir())
        self.merged_directory_label = Label(self.frame2, textvariable=self.save_dir_text, bg=bg_col)
        self.save_file_name = Label(self.frame2, text='Name of file to be created:', bg=bg_col)

        # Merge button
        self.merge_button = Button(self.frame3, text='Merge',
                                   command=lambda:
                                   PDFMethods.combine_pdf(self.file_name_text.get(), self.file_name2_text.get(),
                                                          self.save_dir_text.get(), self.merged_file_name.get()))

        # Quit app button
        self.quit_button = Button(self.frame3, text='Quit', command=master.quit)

        # LAYOUT #

        # Build master frame - 4 frames so 4 rows, only need 1 column in parent frame
        for row in range(4):
            master.rowconfigure(row, weight=1)

        master.columnconfigure(1, weight=1)

        # Configure all child frames - 20 cols for nice layout. Must be a better way?
        self.frame0.grid(row=0, column=0, columnspan=2, sticky=N+E+S+W)
        for row in range(3):
            self.frame0.rowconfigure(row, weight=1)
            self.frame1.rowconfigure(row, weight=1)
            self.frame2.rowconfigure(row, weight=1)
            self.frame3.rowconfigure(row, weight=1)

        for col in range(20):
            self.frame0.columnconfigure(col, weight=1)
            self.frame1.columnconfigure(col, weight=1)
            self.frame2.columnconfigure(col, weight=1)
            self.frame3.columnconfigure(col, weight=1)

        self.title_label.grid(row=1, column=1)

        self.frame1.grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)
        # self.first_file_label.grid(row=1, column=0)
        self.first_file_browser.grid(row=1, column=1, sticky=W)
        self.first_select_label.grid(row=1, column=3, sticky=W)
        # self.second_file_label.grid(row=2, column=0)
        self.second_file_browser.grid(row=2, column=1, sticky=W)
        self.second_select_label.grid(row=2, column=3, sticky=W)

        self.frame2.grid(row=2, column=0, columnspan=2, sticky=N+E+S+W)
        # self.merged_file_label.grid(row=1, column=1, sticky=W)
        self.merged_directory_browser.grid(row=1, column=1, sticky=W)
        self.merged_directory_label.grid(row=1, column=2, sticky=W)
        self.save_file_name.grid(row=2, column=1, sticky=W)
        self.merged_file_name.grid(row=2, column=2, sticky=W)

        self.frame3.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.merge_button.grid(row=1, column=1, sticky=W)
        self.quit_button.grid(row=1, column=2)

    # Function to open file browser
    def file_browser(self):
        file_name = filedialog.askopenfilename()
        self.file_name_text.set(file_name)

    def file_browser2(self):
        file_name2 = filedialog.askopenfilename()
        self.file_name2_text.set(file_name2)

    def save_dir(self):
        save_dir_text = filedialog.askdirectory()
        self.save_dir_text.set(save_dir_text)

if __name__ == '__main__':
    root = Tk()
    app = PdfGUI(master=root)
    root.mainloop()
