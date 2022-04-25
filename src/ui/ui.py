from services.shift_app_service import ShiftAppService
from ui.create_user import CreateUserUi
from ui.login import LoginUi
from tkinter import Tk

from ui.employee_ui import CreateEmployeeUi

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_create_user(self):
        self._current_view.destroy()
        self._show_create_user_view()

    
    def _handle_login(self):
        self._current_view.destroy()
        self._show_login_view()
    
    def _handle_employee_view(self):
        self._current_view.destroy()
        self._show_create_employee_view()

    def _handle_employer_view(self):
        pass

    
    def _show_login_view(self):
        self._current_view = LoginUi(
            self._root, self._handle_employee_view, self._handle_login
        )
        self._current_view.pack()
    

    def _show_create_user_view(self):

        self._current_view = CreateUserUi(
            self._root, self._handle_create_user
        )
        self._current_view.pack()
    
    def _show_create_employee_view(self):
        self._current_view = CreateEmployeeUi(
            self._root, self._handle_employee_view,
        )
        self._current_view.pack()
