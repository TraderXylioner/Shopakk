from typing import Optional

from fastapi_users import FastAPIUsers
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.v1.security.auth import auth
from fastapi import Request, Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from server.api.v1.security.models import UserAuthModel
from server.core.setup import get_session
from server.settings import Auth


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, UserAuthModel)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


class UserManager(IntegerIDMixin, BaseUserManager[UserAuthModel, int]):
    reset_password_token_secret = Auth.SECRET
    verification_token_secret = Auth.SECRET

    async def on_after_register(self, user: UserAuthModel, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserAuthModel, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserAuthModel, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


fastapi_users = FastAPIUsers[UserAuthModel, int](get_user_manager, [auth])

current_active_user = fastapi_users.current_user(active=True)
