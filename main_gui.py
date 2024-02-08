# Import Module
from tkinter import *
import main_function as mf
from tkinter import messagebox

windows_size = '800x640'
class GUI(Frame):
    root: Tk
    login_frame: Frame
    sitename_frame: Frame
    am_file_frame: Frame
    am_detail_frame: Frame
    existing_sitename_frame: Frame
    existing_site_list: list[str] = mf.initialize_sitename_list()
    filtered_list: list[str] = existing_site_list
    
    def __init__(self, root: Tk) -> None:
        super().__init__(root)
        self.root = root
        # root window title and dimension
        root.title("KwickPOS SD&S Tracking App")
        # Set window size (widthxheight)
        root.geometry(windows_size)
        self.login_screen()
    
    def clearFrame(self, ref_frame: Frame):
        # destroy all widgets from frame
        for widget in ref_frame.winfo_children():
            widget.destroy()
        # this will clear frame and frame will be empty if you want to hide the empty panel then
        ref_frame.pack_forget()
    
    def login_screen(self):
        # Initialize the login screen - FRAME
        self.login_frame = Frame(self.root)
        self.login_frame.pack()

        # Create a label for the title of the login page
        title_label = Label(self.login_frame, text="USER NAME", font=("Arial", 20))

        # Create a label and an entry for the username
        username_label = Label(self.login_frame, text="Enter your name: ")
        username_entry = Entry(self.login_frame)

        # Create a button to submit the login details
        login_button = Button(self.login_frame, text="SUBMIT", command=lambda: mf.set_current_user(username_entry.get()))

        # Use the grid method to position the widgets
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        username_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
        username_entry.grid(row=1, column=1, padx=10, pady=10)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.sitename_screen()

    def sitename_screen(self):
        # Initialize the sitename screen - FRAME
        self.sitename_frame = Frame(self.root)
        self.sitename_frame.pack()

        # Create a label for the title of the sitename page
        title_label = Label(self.login_frame, text="SITENAME", font=("Arial", 20))
        title_label.grid(row=3, column=0, columnspan=2, pady=10)

        add_sitename_label = Label(self.login_frame, text="New sitename: ")
        add_sitename_entry = Entry(self.login_frame)
        add_sitename_label.grid(row=4, column=0, padx=10, pady=10, sticky=E)
        add_sitename_entry.grid(row=4, column=1, padx=10, pady=10)

        # button to initialize new site
        add_sitename_button = Button(self.sitename_frame, text="ADD SITE",
                                     command=lambda: mf.initialize_sitename(add_sitename_entry.get()))
        add_sitename_button.grid(row=5, column=0, columnspan=2, pady=10)

        my_sitename_list = mf.sitename_list

        # create a list of site name
        for index, sitename in enumerate(mf.sitename_list):
            print(index, sitename)
        
        self.existing_sitename()
    
    def apply_search_filter(self, word: str):
        self.filtered_list = [sites for sites in self.existing_site_list if word in sites]
        return self.filtered_list
    
    def existing_sitename(self):
        self.existing_sitename_frame = Frame(self.root)
        self.existing_sitename_frame.pack()

        # Create a label for the title of the sitename page
        title_label = Label(self.existing_sitename_frame, text="EXISTING SITES", font=("Arial", 18))
        title_label.grid(row=6, column=0, columnspan=2, pady=10)

        # Create search field and button
        search_sitename_entry = Entry(self.existing_sitename_frame)
        search_sitename_entry.grid(row=7, column=0, padx=10, pady=10, sticky=E)

        search_sitename_button = Button(self.existing_sitename_frame, text="SEARCH", 
                                        command=lambda: self.apply_search_filter(search_sitename_entry.get()))
        search_sitename_button.grid(row=7, column=1, padx=10, pady=10, sticky=E)



        self.am_file_screen()

    def am_file_screen(self):
        self.am_file_frame = Frame(self.root)
        self.am_file_frame.pack()

        self.am_detail_screen()

    def am_detail_screen(self):
        self.am_detail_frame = Frame(self.root)
        self.am_detail_frame.pack()

        empty_label = Label(self.login_frame, text="")
        empty_label.grid(row=0, column=2)
        
