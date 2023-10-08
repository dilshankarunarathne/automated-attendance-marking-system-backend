from config import config
from dao.attendance_dao import AttendanceDAO
from models.attendance_model import Attendance

dao = AttendanceDAO(
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


def mark_attendance(index, date):
    return dao.insert_attendance(index, date)


def query_attendance_by_index(index) -> list[Attendance]:
    rows = dao.check_attendance_by_index(index)
    arr = []
    for row in rows:
        arr.append(
            Attendance(row[0], row[1])
        )
    return arr


def query_attendance_by_date(date) -> list[Attendance] | str:
    rows = dao.check_attendance_by_date(date)
    if rows is None:
        return "{ message: Nothing was found }"
    
    arr = []
    for row in rows:
        arr.append(
            Attendance(row[0], row[1])
        )
    return arr


def query_attendance(index, date) -> Attendance | None:
    return dao.check_attendance_for_student_day(index, date)
