from dao.student_dao import StudentDAO

from config import config

dao = StudentDAO(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)
try:
    dao.connect()
    print("User DB connection successful")
except Exception as e:
    print("User DB (user) connection error:", e)


def add_student(index_number, name, address, gender, date_of_birth, parent_name, contact_number, grade):
    return dao.register_student(
        
    )


def get_student(index_number: str):
    return dao.query_student_details(index_number)
