from entities.shift import Shift
from shift_db_connection import get_shift_db_connection


def return_shift(row):
    return Shift(row["date"], row["time"], row["location"], row["employee"])


class ShiftRepository:
    """Class for handling shifts

    """

    def __init__(self):
        """Establishes connection to shift database

        """
        self._connection = get_shift_db_connection()

    def create_shift(self, shift):
        """Creates a shift

        Args:
            shift (Shift): a shift object that will be saved to the table
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO shift_database \
            (date, time, location, employee) \
            VALUES (?,?,?,?)",
                       (shift.date, shift.time, shift.location, shift.employee))
        self._connection.commit()
        cursor.close()

    def find_shift(self, shift):
        """Finds shift from the table

        Args:
            shift (Shift): a shift object that is searched

        Returns:
            row: desired row object that includes the shift
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE (date, time, location, employee)=(?,?,?,?)",
            (shift.date, shift.time, shift.location, shift.employee))
        row = cursor.fetchone()
        return return_shift(row)

    def find_user_shifts(self, user):
        """Finds all user's shifts from the table

        Args:
            user (string): name of the user which shifts are searched

        Returns:
            list: list of the shifts (PLACEHOLDER)
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE employee = ?", [user.username])
        row = cursor.fetchall()
        return list(row)

    def find_all_shifts(self):
        """Find all shifts from the table

        Returns:
            list: list object including all shifts (PLACEHOLDER)
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database")
        row = cursor.fetchall()
        return list(return_shift(row))

    def find_available_shifts(self):
        """Finds all shifts that are not assigned to any employee

        Returns:
            list: list of all shifts that have employee column as NULL
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE employee = NULL")
        row = cursor.fetchall()
        return list(row)
