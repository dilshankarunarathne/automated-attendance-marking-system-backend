from config import config
from dao.attendance_dao import AttendanceDAO

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


def query_attendance_by_index(index):
    
