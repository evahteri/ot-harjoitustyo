from ui.create_user import CreateUserUi
from tkinter import Tk

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_create_user_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_create_user(self):
        self._show_create_user_view()
    
    def _handle_employee_view(self):
        pass

    def _handle_employer_view(self):
        pass

    

    def _show_create_user_view(self):

        self._current_view = CreateUserUi(
            self._root, self._handle_create_user
        )
        
        self._current_view.pack()
