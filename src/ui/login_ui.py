from tkinter import StringVar, Tk, ttk
from services.shift_app_service import ShiftAppService


class Create_user_ui:

    def __init__(self, root):
        self._root = root
        self._username_entry = StringVar()
        self._password_entry = StringVar()
        self._shiftappservice = ShiftAppService()

    def base(self):
        header = ttk.Label(master=self._root, text="Create a user")

        username_header = ttk.Label(master=self._root, text="Username")

        self.username_entry = ttk.Entry(
            master=self._root, textvariable=self._username_entry)

        password_header = ttk.Label(master=self._root, text="Password")

        self.password_entry = ttk.Entry(
            master=self._root, textvariable=self._password_entry)

        create_button = ttk.Button(
            master=self._root, text="Create", command=self.handle_button_click)

        header.pack()
        username_header.pack()
        self.username_entry.pack()
        password_header.pack()
        self.password_entry.pack()
        create_button.pack()

    def handle_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self._shiftappservice.create_user(
            username=username, password=password, role="employee")

    def start():

        window = Tk()

        window.title("Shift App")

        ui = Create_user_ui(window)
        ui.base()

        window.mainloop()
