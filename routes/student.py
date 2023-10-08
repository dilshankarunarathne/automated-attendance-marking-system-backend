from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends

from auth.authorize import authenticate_user, oauth2_scheme, get_current_user, credentials_exception
from auth.hashing import get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, blacklist_token

router = APIRouter(
    prefix="/api/student",
    tags=["student"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post('/register')
async def register_new_student(
    token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception
