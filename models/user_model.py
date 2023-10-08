from pydantic import BaseModel


class User(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    email: str | None = None
    contact_number: str | None = None
    is_admin: bool | None = None


class UserInDB(User):
    hashed_password: str
