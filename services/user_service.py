from models.user_model import User

from services.database_service import dao


def add_new_user(user: User):
    dao.create_user(user)


def user_exists(email: str) -> bool:
    if get_user(email) is None:
        return False
    return True


def get_user(email: str):
    return dao.get_user_by_email(email)
