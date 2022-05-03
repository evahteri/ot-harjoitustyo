from tkinter import StringVar, Tk, ttk, constants
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository

class ShiftView:
    """Class that is responsible for viewing shifts
    """
    def __init__(self, root, handle_employee_view, shift_app_service, rows):
        """Constructor that establishes which rows to show and services

        Args:
            root (Tk()): Tk() object from ui
            handle_employee_view (function): Function that hides current view and shows employee view
            shift_app_service (class): Service that had been established in UI class
            rows (list): List that includes shifts
        """
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
        self._table = ttk.Treeview(master=self._frame, columns=(1,2,3,4), show="headings")

        self._table.heading(1, text="Date")
        self._table.heading(2, text="Time")
        self._table.heading(3, text="Location")
        self._table.heading(4, text="Employee")

        for row in self.rows:
            self._table.insert(parent="", index= "end", values=(row[0], row[1], row[2], row[3]))

        self._table.grid(row=0, column=0)

        self.select_shift_button = ttk.Button(master=self._frame, text="Choose selected shifts", command=self.handle_select_shift_button)
        self.select_shift_button.grid(row=1, column=0)

        self.back_button = ttk.Button(master=self._frame, text="Back", command=self.handle_back_button)
        self.back_button.grid(row=3, column=0)
    
    def handle_back_button(self):
        self._employee_view()
    
    def handle_select_shift_button(self):
        print(self._table.selection())
