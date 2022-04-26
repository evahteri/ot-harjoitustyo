from tkinter import StringVar, Tk, ttk, constants, messagebox
from services.shift_app_service import ShiftAppService



class CreateUserUi:

    def __init__(self, root, handle_create_user):
        self._root = root
        self._handle_create_user = handle_create_user
        self._frame = None
        self._role = StringVar()
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

        header = ttk.Label(master=self._frame, text="Create a user")
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

        
        self.employee_button = ttk.Radiobutton(master=self._frame, text="Employee",variable=self._role, value="Employee")
        self.employee_button.grid(row= 7, column=0)


        self.employer_button = ttk.Radiobutton(master=self._frame, text="Employer",variable=self._role, value="Employer")
        self.employer_button.grid(row= 8, column=0)

        create_button = ttk.Button(
            master=self._frame, text="Create", command=self.handle_button_click)
        create_button.grid(row= 10, column=0)
        



    def handle_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self._role = self._role.get()
        self._shiftappservice.create_user(
            username=username, password=password, role=self._role)
        messagebox.showinfo(title="User created", message="User created succesfully!")

