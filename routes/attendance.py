from fastapi import APIRouter, Depends, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.attendance_service import mark_attendance, query_attendance_by_index, query_attendance_by_date

router = APIRouter(
    prefix="/api/attendance",
    tags=["attendance"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post('mark')
async def mark(
        index_number: str = Form(...),
        date: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    mark_attendance(index_number, date)
    return "{ message: attendance marked! }"


@router.post("search-by-index")
async def search_by_index(
        index_number: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    return query_attendance_by_index(index_number)


@router.post("search-by-date")
async def search_by_date(
        date: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    return query_attendance_by_date(date)


@router.post("search")

