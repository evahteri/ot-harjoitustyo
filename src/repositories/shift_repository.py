from entities.shift import Shift
from shift_db_connection import get_shift_db_connection


class NoShiftsError(Exception):
    pass


def return_shift(row):
    return Shift(row["date"], row["time"], row["location"], row["employee"])


def return_multiple_shifts(rows):
    data = []
    for row in rows:
        data.append((row["shift_id"], row["date"], row["time"],
                    row["location"], row["employee"]))
    return data


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
            row (list): a list that includes a tuple with shift information
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE (date, time, location, employee)=(?,?,?,?)",
            (shift.date, shift.time, shift.location, shift.employee))
        row = cursor.fetchone()
        cursor.close()
        return return_shift(row)

    def find_user_shifts(self, user):
        """Finds all user's shifts from the table

        Args:
            user (string): name of the user which shifts are searched

        Returns:
            Shifts in a list through another function
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE employee = ?", [user.username])
        rows = cursor.fetchall()
        cursor.close()
        return return_multiple_shifts(rows)

    def find_all_shifts(self):
        """Find all shifts from the table

        Returns:
            Shifts in a list through another function
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database")
        rows = cursor.fetchall()
        cursor.close()
        return return_multiple_shifts(rows)

    def find_available_shifts(self):
        """Finds all shifts that are not assigned to any employee

        Returns:
            list: list of all shifts that have employee column as NULL
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE employee IS NULL")
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return return_multiple_shifts(rows)
        raise NoShiftsError("No available shifts")

    def choose_shift(self, shift_id, user):
        """Sets shifts column "employee" to user

        Args:
            shift_id (int): integer that matches a shift in  the table
            user (User): User object that is the current user
        """
        cursor = self._connection.cursor()
        cursor.execute("UPDATE shift_database SET employee = ? \
            WHERE shift_id = ?",
                       (user.username, shift_id))
        self._connection.commit()
        cursor.close()

    def delete_data(self):
        """Deletes all data from the database
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM shift_database")
        self._connection.commit()
