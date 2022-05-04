from services.shift_app_service import ShiftAppService
from ui.create_user import CreateUserUi
from ui.login import LoginUi
from tkinter import Tk

from ui.employee_ui import CreateEmployeeUi
from ui.employer_ui import CreateEmployerUi
from ui.shift_view import ShiftView


class UI:
    """Class that controls all ui elements
    """

    def __init__(self, root):
        """Constructor that establishes ShiftAppService and current view which is at start None.

        Args:
            root (Tk() object): window that has been created in index.py.
        """
        self._root = root
        self._current_view = None
        self._shift_app_service = ShiftAppService()

    def start(self):
        """Function to handle start. In this case the first view is login view.
        """
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_create_user(self):
        self._hide_current_view()
        self._show_create_user_view()

    def _handle_login(self):
        self._hide_current_view()
        self._show_login_view()

    def _handle_employee_view(self):
        self._hide_current_view()
        self._show_employee_view()
    
    def _handle_employer_view(self):
        self._hide_current_view()
        self._show_employer_view()


    def _handle_shift_view(self, rows):
        self._hide_current_view()
        self._show_shift_view(rows)

    def _show_login_view(self):
        self._current_view = LoginUi(
            self._root,self._handle_employee_view, self._handle_create_user, self._handle_employer_view, self._shift_app_service
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        self._current_view = CreateUserUi(
            self._root, self._handle_create_user, self._handle_login, self._shift_app_service
        )
        self._current_view.pack()

    def _show_employee_view(self):
        self._current_view = CreateEmployeeUi(
            self._root, self._handle_login, self._handle_shift_view, self._shift_app_service
        )
        self._current_view.pack()
    
    def _show_employer_view(self):
        self._current_view = CreateEmployerUi(
            self._root, self._handle_login, self._handle_shift_view,None, self._shift_app_service
        )
        self._current_view.pack()
    def _show_shift_view(self, rows):
        self._current_view = ShiftView(
            self._root, self._handle_employee_view, self._shift_app_service, rows
        )
        self._current_view.pack()