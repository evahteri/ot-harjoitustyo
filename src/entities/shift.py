class Shift:
    """Class for shift object
    """

    def __init__(self, date, time, location, employee):
        """Constructor that creates a shift type object

        Args:
            date (string): date of the shift (e.g. 30.4.2022)
            time (string): time of day (e.g. 6:30-12:00)
            location (string): location of the shift
            employee (string/None): assigned employee for the shift.

        """

        self.date = date
        self.time = time
        self.location = location
        self.employee = employee
