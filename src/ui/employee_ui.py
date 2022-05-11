from tkinter import ttk, constants, messagebox
from repositories.shift_repository import ShiftRepository, NoShiftsError


class CreateEmployeeUi:
    """Class responsible for employee ui
    """

    def __init__(self, root, handle_login, handle_shift_view, shift_app_service):
        """Constructor for CreateEmployeeUi Class

        Args:
            root (Tk()): Tk() window from ui
            handle_login (function): Function that handles the view for login
            handle_shift_view (function): Function that handles the view for shifts
            shift_app_service (class): Class the whole ui uses
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_shift_view = handle_shift_view
        self._frame = None
        self._shiftappservice = shift_app_service
        self._shift_repository = ShiftRepository()

        self._base()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Closes the view
        """
        self._frame.destroy()

    def _handle_logout_button(self):
        self._shiftappservice.logout()
        self._handle_login()

    def _handle_available_button_click(self):
        try:
            rows = self._shift_repository.find_available_shifts()
            self._handle_shift_view(rows, True)

        except NoShiftsError:
            messagebox.showerror(title="No available shifts",
                                 message="There are no available shifts right now"
                                 )

    def _handle_my_shifts_button_click(self):
        shifts = self._shift_repository.find_user_shifts(
            self._shiftappservice.get_current_user)
        self._handle_shift_view(shifts, False)

    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Choose a function")
        header.grid(row=0, column=0)

        self.available_button = ttk.Button(
            master=self._frame, text="Show available shifts", command=self._handle_available_button_click)
        self.available_button.grid(row=2, column=0)

        self.my_shifts_button = ttk.Button(
            master=self._frame, text="Show my shifts", command=self._handle_my_shifts_button_click)

        self.my_shifts_button.grid(row=4, column=0)

        self.log_out_button = ttk.Button(
            master=self._frame, text="Log out", command=self._handle_logout_button)
        self.log_out_button.grid(row=7, column=0)
