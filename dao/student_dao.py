import mysql.connector
from mysql.connector import errorcode

from models.student_model import Student

"""
    middleware for accessing the attendance database and performing CRUD operations on the student table
"""


class StudentDAO:
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

    def register_student(self, student: Student):
        cursor = self.cnx.cursor()
        add_user = ("INSERT INTO student "
                    "(index_number, name, address, gender, "
                    "date_of_birth, parent_name, contact_number, grade) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        data_student = (student.index_number, student.name, student.address, student.gender,
                        student.date_of_birth, student.parent_name, student.contact_number, student.grade)
        cursor.execute(add_user, data_student)
        self.cnx.commit()
        cursor.close()

    def query_student_details(self, index_number: str):
        cursor = self.cnx.cursor()
        query = ("SELECT * "
                 "FROM  student "
                 "WHERE index_number = %s")
        cursor.execute(query, (index_number,))
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
