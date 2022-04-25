from entities.shift import Shift
from entities.user import User
from shift_db_connection import get_shift_db_connection


def return_shift(row):
    return Shift(row["date"], row["time"], row["location"], row["employee"])



class ShiftRepository:

    def __init__(self):
        self._connection = get_shift_db_connection()

    def create_shift(self, shift):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO shift_database \
            (date, time, location, employee) \
            VALUES (?,?,?,?)",
                       (shift.date, shift.time, shift.location, shift.employee))
        self._connection.commit()
        cursor.close()

    def find_shift(self, shift):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE (date, time, location, employee)=(?,?,?,?)", (shift.date, shift.time, shift.location, shift.employee))
        row = cursor.fetchone()
        return return_shift(row)
    
    def find_user_shifts(self,user):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE employee = ?", [user.username])
        row = cursor.fetchall()
        return list(row)
    
    def find_all_shifts(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database")
        row = cursor.fetchall()
        return return_shift(row)
    
    def find_available_shifts(self):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM shift_database WHERE employee = NULL")
        row = cursor.fetchall()
        return list(row)
