from fastapi import APIRouter, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception

router = APIRouter(
    prefix="/api/student",
    tags=["student"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post('/register')
async def register_new_student(
    index_number, name, address, gender, date_of_birth, parent_name, contact_number, grade
    token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception


