from tkinter import Tk, ttk


class Create_user_ui:

    def __init__(self,root):
        self._root = root

    def start(self):
        header = ttk.Label(master=self._root, text = "Create a user")

        username_header = ttk.Label(master=self._root, text= "Username")

        username_entry = ttk.Entry(master=self._root)

        password_header = ttk.Label(master=self._root, text= "Password")

        password_entry = ttk.Entry(master=self._root)

        create_button = ttk.Button(master=self._root, text="Create")

        header.pack()
        username_header.pack()
        username_entry.pack()
        password_header.pack()
        password_entry.pack()
        create_button.pack()

window = Tk()

window.title("Shift App")

ui = Create_user_ui(window)
ui.start()

window.mainloop()
    

