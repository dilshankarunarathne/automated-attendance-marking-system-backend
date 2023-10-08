import mysql.connector
from mysql.connector import errorcode

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

    def check_attendance_for_student_day(self, index_no):
