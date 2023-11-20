from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from server.core.models.user import UserModel


class UserAuthModel(SQLAlchemyBaseUserTable[int], UserModel):
    __table_args__ = {"extend_existing": True}
