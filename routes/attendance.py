from fastapi import APIRouter, Depends, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.student_service import add_student, get_student

router = APIRouter(
    prefix="/api/student",
    tags=["student"],
    responses={404: {"description": "The requested page was not found"}},
)

