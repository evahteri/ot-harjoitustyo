from tkinter import StringVar, Tk, ttk, constants
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository


class CreateEmployerUi:
    """Class responsible for employer view
    """

    def __init__(self, root, handle_login, handle_shift_view, handle_create_new_shift, shift_app_service):
        """Constructor for CreateEmployerUi class

        Args:
            root (Tk()): Tk() window from ui
            handle_login (function): Function that handles the login view
            handle_shift_view (function): Function that handles the shift view
            handle_create_new_shift (function): Function that handles the create shift view
            shift_app_service (class): Class that the whole ui uses
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_shift_view = handle_shift_view
        self._handle_create_new_shift = handle_create_new_shift
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

    def _handle_show_all_button_click(self):
        rows = self._shift_repository.find_all_shifts()
        self._handle_shift_view(rows, False)

    def _handle_create_new_shift_button_click(self):
        self._handle_create_new_shift()

    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Choose a function")
        header.grid(row=0, column=0)

        self.show_all_button = ttk.Button(
            master=self._frame, text="Show all shifts", command=self._handle_show_all_button_click)
        self.show_all_button.grid(row=2, column=0)

        self.create_new_shift_button = ttk.Button(
            master=self._frame, text="Create a new shift", command=self._handle_create_new_shift_button_click)

        self.create_new_shift_button.grid(row=4, column=0)

        self.log_out_button = ttk.Button(
            master=self._frame, text="Log out", command=self._handle_logout_button)
        self.log_out_button.grid(row=7, column=0)
