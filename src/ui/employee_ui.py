from tkinter import StringVar, Tk, ttk
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository


class CreateEmployeeUi:

    def __init__(self, root, user):
        self.user = user
        self._root = root
        self._error_variable = None
        self._error_label = None
        self._shiftappservice = ShiftAppService()

    def base(self):
        header = ttk.Label(master=self._root, text="Choose a function")

        self.available_button = ttk.Button(
            master=self._root, text="Show available shifts", command=self.handle_available_button_click)
        
        self.my_shifts_button = ttk.Button(
            master=self._root, text="Show my shifts", command=self.handle_my_shifts_button_click)

        header.pack()
        self.available_button.pack()
        self.my_shifts_button.pack()

    def handle_available_button_click(self):
        shifts = ShiftRepository().find_available_shifts()
        print(shifts)
    
    def handle_my_shifts_button_click(self):
        shifts = ShiftRepository().find_user_shifts()
        print(shifts)

    def start():

        window = Tk()

        window.title("Shift App")

        ui = CreateEmployeeUi(window)
        ui.base()

        window.mainloop()
