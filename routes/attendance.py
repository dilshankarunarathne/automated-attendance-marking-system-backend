from fastapi import APIRouter, Depends, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.student_service import add_student, get_student

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post('mark')
async def mark(
        index_number: str = Form(...),
date: str = Form(...),
)
