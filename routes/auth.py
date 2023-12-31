from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends

from auth.authorize import authenticate_user, oauth2_scheme
from auth.hashing import get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, blacklist_token
from models.user_model import UserInDB
from services.user_service import user_exists, add_new_user

"""
    API router for auth endpoint
    
    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        [POST] /api/auth/register
        register_user: the endpoint for registering a new user

        [POST] /api/auth/login
        login_for_access_token: the endpoint for logging in a user

        [POST] /api/auth/logout
        logout: the endpoint for logging out a user
"""

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/register")
async def register_user(
        firstname: str = Form(...),
        lastname: str = Form(...),
        email: str = Form(...),
        contact_number: str = Form(...),
        password: str = Form(...),
        is_admin=False
):
    """
    The endpoint for registering a new user

    Args:
        firstname (str):
        lastname (str):
        email (str): the email of the user
        contact_number (str):
        password (str): the password of the user
        is_admin (bool): whether the user is an admin

    Returns:
        (UserInDB) The user that was registered

    Raises:
        HTTPException: if the username already exists
    """

    if user_exists(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    hashed_password = get_password_hash(password)
    user = UserInDB(
        firstname=firstname,
        lastname=lastname,
        email=email,
        contact_number=contact_number,
        hashed_password=hashed_password,
        is_admin=is_admin,
    )
    add_new_user(user)
    return user


@router.post("/login")
async def login_for_access_token(
        email: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    """
    The endpoint for logging in a user

    Args:
        email:
        password:

    Returns:
        (dict) The access token for the user

    Raises:
        HTTPException: if the username or password is incorrect
    """
    user = authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires.seconds
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    """
    The endpoint for logging out a user

    Args:
        token (oauth2 bearer token): the token for the user

    Returns:
        (dict) The message for logging out
    """
    blacklist_token(token)
    return {"message": "Successfully logged out"}
