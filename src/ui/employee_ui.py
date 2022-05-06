from tkinter import StringVar, Tk, ttk, constants, messagebox
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository, NoShiftsError


class CreateEmployeeUi:

    def __init__(self, root, handle_login, handle_shift_view, shift_app_service):
        self._root = root
        self._handle_login = handle_login
        self._handle_shift_view = handle_shift_view
        self._frame = None
        self._shiftappservice = shift_app_service
        self._shift_repository = ShiftRepository()

        self._base()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Choose a function")
        header.grid(row=0, column=0)

        self.available_button = ttk.Button(
            master=self._frame, text="Show available shifts", command=self.handle_available_button_click)
        self.available_button.grid(row=2, column=0)

        self.my_shifts_button = ttk.Button(
            master=self._frame, text="Show my shifts", command=self.handle_my_shifts_button_click)

        self.my_shifts_button.grid(row=4, column=0)

        self.log_out_button = ttk.Button(
            master=self._frame, text="Log out", command=self.handle_logout_button)
        self.log_out_button.grid(row=7, column=0)
    
    def handle_logout_button(self):
        self._shiftappservice.logout()
        self._handle_login()

    def handle_available_button_click(self):
        try:
            rows = self._shift_repository.find_available_shifts()
            self._handle_shift_view(rows, True)

        except NoShiftsError:
            messagebox.showerror(title="No available shifts",
            message= "There are no available shifts right now"
            )


    def handle_my_shifts_button_click(self):
        shifts = self._shift_repository.find_user_shifts(self._shiftappservice.get_current_user)
        self._handle_shift_view(shifts, False)
