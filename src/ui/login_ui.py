from tkinter import Tk, ttk
from services.shift_app_service import ShiftAppService


class Create_user_ui:

    def __init__(self,root):
        self._root = root
        self._username_entry = None
        self._password_entry = None
    
    def handle_button_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        ShiftAppService.create_user(username=username, password=password, role=None)
        

        


    def base(self):
        header = ttk.Label(master=self._root, text = "Create a user")

        username_header = ttk.Label(master=self._root, text= "Username")

        username_entry = ttk.Entry(master=self._root)

        password_header = ttk.Label(master=self._root, text= "Password")

        password_entry = ttk.Entry(master=self._root)

        create_button = ttk.Button(master=self._root, text="Create", command=self.handle_button_click)

        header.pack()
        username_header.pack()
        username_entry.pack()
        password_header.pack()
        password_entry.pack()
        create_button.pack()
    
    
    def start():

        window = Tk()

        window.title("Shift App")

        ui = Create_user_ui(window)
        ui.base()

        window.mainloop()
            

