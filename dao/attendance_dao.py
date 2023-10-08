import mysql.connector
from mysql.connector import errorcode

from models.attendance_model import Attendance

"""
    middleware for accessing the attendance database and performing CRUD operations on the attendance table
"""


class AttendanceDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        if self.cnx is not None:
            self.cnx.close()

    def insert_attendance(self, index_no, date):
        cursor = self.cnx.cursor()
        add_user = ("INSERT INTO attendance "
                    "(student_index_number , date "
                    "VALUES (%s, %s)")
        data = (index_no, date)
        cursor.execute(add_user, data)
        self.cnx.commit()
        cursor.close()

    def check_attendance_for_student_day(self, index_no, date):
        cursor = self.cnx.cursor()
        query = ("SELECT * "
                 "FROM  attendance "
                 "WHERE student_index_number = %s "
                 "AND date = %s")
        cursor.execute(query, (index_no, date))
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return Attendance(row[0], row[1])

    def check_attendance_by_index(self, index_no):
        try:
            cursor = self.cnx.cursor()
            query = ("SELECT * FROM attendance "
                     "WHERE student_index_number = %s")
            cursor.execute(query, (index_no, ))
            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return None
            return rows
        except mysql.connector.Error as err:
            print(err)

    def check_attendance_by_date(self, date):
        try:
            cursor = self.cnx.cursor()
            query = "SELECT * FROM attendance WHERE date = %s"
            cursor.execute(query, (date, ))
            rows = cursor.fetchall()
            cursor.close()
            if not rows:
                return None
            return rows
        except mysql.connector.Error as err:
            print(err)
