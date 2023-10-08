from fastapi import APIRouter, Depends, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.student_service import add_student

router = APIRouter(
    prefix="/api/student",
    tags=["student"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post('/register')
async def register_new_student(
        index_number: str = Form(...),
        name: str = Form(...),
        address: str = Form(...),
        gender: str = Form(...),
        date_of_birth: str = Form(...),
        parent_name: str = Form(...),
        contact_number: str = Form(...),
        grade: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    return add_student(index_number, name, address, gender, date_of_birth, parent_name, contact_number, grade)


@router.post('/search')
async def query_student(
        
)
