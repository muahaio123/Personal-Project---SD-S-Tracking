import main_function
import os
import tkinter as tk
import main_gui 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('SD&S Tracking')
        self.geometry('800x640')

if __name__ == "__main__":
    if not os.path.exists(main_function.project_path):
        os.makedirs(main_function.project_path)
    main_function.initialize_sitename_list()

    app = App()
    frame = main_gui.GUI(app)
    app.mainloop()
