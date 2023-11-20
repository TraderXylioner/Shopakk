from fastapi import APIRouter

from server.api.v1.security.auth import auth
from server.api.v1.security.manager import fastapi_users
from server.api.v1.security.schemas import UserRead, UserCreate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
