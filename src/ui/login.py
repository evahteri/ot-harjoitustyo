from tkinter import StringVar, Tk, ttk, constants
from services.shift_app_service import ShiftAppService
from ui import create_user



class LoginUi:

    def __init__(self, root, handle_employee_view, handle_login):
        self._root = root
        self._handle_employee_view = handle_employee_view
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = StringVar()
        self._password_entry = StringVar()
        self._shiftappservice = ShiftAppService()

        self._base()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Login")
        header.grid(row=0, column=0)

        username_header = ttk.Label(master=self._frame, text="Username")
        username_header.grid(row=2, column=0)

        self.username_entry = ttk.Entry(
            master=self._frame, textvariable=self._username_entry)
        
        self.username_entry.grid(row= 3, column=0)
        


        password_header = ttk.Label(master=self._frame, text="Password")
        password_header.grid(row= 4, column=0)


        self.password_entry = ttk.Entry(
            master=self._frame, textvariable=self._password_entry)
        
        self.password_entry.grid(row= 5, column=0)

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self.handle_button_click)
        login_button.grid(row= 10, column=0)

        create_user_button = ttk.Button(
            master = self._frame, text= "Create new user", command = self._handle_login
        )
        create_user_button.grid(row = 11, column = 0)
        


    def handle_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self._shiftappservice.login(username, password)
        self._handle_employee_view()
    

