from tkinter import StringVar, Tk, ttk, constants, messagebox
from services.shift_app_service import InvalidShiftInformation


class CreateShift:
    """Reponsible for shift creation ui view
    """

    def __init__(self, root, handle_employer_ui, shiftappservice):
        """Constructor that creates the view

        Args:
            root (TK()): Tk() element from ui.py
            handle_employer_ui (function): Function that handles the employer view
            shiftappservice (class): The established class that the whole ui uses
        """
        self._root = root
        self._handle_employer_ui = handle_employer_ui
        self._frame = None
        self._date = StringVar()
        self._time = StringVar()
        self._location = StringVar()
        self._employee = StringVar()
        self._shiftappservice = shiftappservice

        self._base()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Closes the view
        """
        self._frame.destroy()
    
    def _handle_back_button(self):
        self._handle_employer_ui()

    def _handle_button_click(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        location = self.location_entry.get()
        employee = self.employee_entry.get()
        if employee == "":
            employee = None
        try:
            self._shiftappservice.create_shift(
                date=date, time=time, location=location, employee=employee)
            messagebox.showinfo(title="Shift created",
                                message="Shift created succesfully!")
        except InvalidShiftInformation:
            messagebox.showinfo(
                title="Invalid info", message="Please provide all required information")

    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Create a shift")
        header.grid(row=0, column=0)

        date_header = ttk.Label(master=self._frame, text="Date")
        date_header.grid(row=2, column=0)

        self.date_entry = ttk.Entry(
            master=self._frame, textvariable=self._date)
        self.date_entry.grid(row=3, column=0)

        time_header = ttk.Label(master=self._frame, text="Time")
        time_header.grid(row=4, column=0)

        self.time_entry = ttk.Entry(
            master=self._frame, textvariable=self._time)
        self.time_entry.grid(row=5, column=0)

        self.location_header = ttk.Label(master=self._frame, text="Location")
        self.location_header.grid(row=6, column=0)

        self.location_entry = ttk.Entry(
            master=self._frame, textvariable=self._location)
        self.location_entry.grid(row=7, column=0)

        self.employee_header = ttk.Label(master=self._frame, text="Employee")
        self.employee_header.grid(row=8, column=0)

        self.employee_entry = ttk.Entry(
            master=self._frame, textvariable=self._employee)
        self.employee_entry.grid(row=9, column=0)

        create_button = ttk.Button(
            master=self._frame, text="Create", command=self._handle_button_click)
        create_button.grid(row=10, column=0)

        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._handle_back_button
        )
        back_button.grid(row=12, column=0)
