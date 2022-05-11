from tkinter import ttk, constants, messagebox, TclError
from repositories.shift_repository import ShiftRepository


class ShiftView:
    """Class that is responsible for viewing shifts
    """

    def __init__(self, root, handle_employee_view, handle_employer_view, shift_app_service, rows, choose_button):
        """Constructor that establishes which rows to show and services

        Args:
            root (Tk()): Tk() object from ui
            handle_employee_view (function): Function that hides current view and shows employee view
            shift_app_service (class): Service that had been established in UI class
            rows (list): List that includes shifts
        """
        self._root = root
        self._employee_view = handle_employee_view
        self._employer_view = handle_employer_view
        self.rows = rows
        self._frame = None
        self._shift_app_service = shift_app_service
        self._shift_repository = ShiftRepository()
        self._choose_button = choose_button

        self._base()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Closes the view
        """
        self._frame.destroy()

    def _initialize_select_shift_button(self):
        self.select_shift_button = ttk.Button(
            master=self._frame, text="Choose selected shift", command=self._handle_select_shift_button)
        self.select_shift_button.grid(row=1, column=0)

    def _handle_back_button(self):
        if self._shift_app_service.get_current_user.role == "Employee":
            self._employee_view()
        else:
            self._employer_view()

    def _handle_select_shift_button(self):
        try:
            row = self._table.item(self._table.selection())
            shift_id = row["values"][0]
            self._shift_app_service.choose_shift(shift_id)
            messagebox.showinfo(title="Shift chosen",
                                message="The shift is now yours!")
            self._employee_view()
        except IndexError:
            messagebox.showerror(title="No shift chosen",
                                 message="You did not select any shift"
                                 )
        except TclError:
            messagebox.showerror(title="Multiple shifts chosen",
                                 message="Please choose one shift at a time"
                                 )


    def _base(self):
        self._frame = ttk.Frame(master=self._root)
        self._table = ttk.Treeview(
            master=self._frame, columns=(0, 1, 2, 3, 4), show="headings")

        self._table.heading(0, text="id")
        self._table.heading(1, text="Date")
        self._table.heading(2, text="Time")
        self._table.heading(3, text="Location")
        self._table.heading(4, text="Employee")

        for row in self.rows:
            self._table.insert(parent="", index="end", values=(
                row[0], row[1], row[2], row[3], row[4]))

        self._table.grid(row=0, column=0)

        if self._choose_button is True:
            self._initialize_select_shift_button()

        self.back_button = ttk.Button(
            master=self._frame, text="Back", command=self._handle_back_button)
        self.back_button.grid(row=3, column=0)
