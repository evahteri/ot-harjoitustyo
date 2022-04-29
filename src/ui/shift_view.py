from tkinter import StringVar, Tk, ttk, constants
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository

class ShiftView:
    def __init__(self, root, handle_employee_view, shift_app_service, rows):
        self._root = root
        self._employee_view = handle_employee_view
        self.rows = rows
        self._frame = None
        self._shift_app_service = shift_app_service
        self._shift_repository = ShiftRepository()

        self._base()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _base(self):
        self._frame = ttk.Frame(master=self._root)
        self._table = ttk.Treeview(master=self._root, columns=(1,2,3,4), show="headings")
        self._table.grid(row=0, column=0)

        self._table.heading(1, text="Date")
        self._table.heading(2, text="Time")
        self._table.heading(3, text="Location")
        self._table.heading(4, text="Employee")

        for row in self.rows:
            self._table.insert(parent="", index= "end", values=(row[0], row[1], row[2], row[3]))
