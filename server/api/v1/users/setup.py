from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from server.api.v1.users.schemas import UserResult
from server.core.models.user import UserModel


class UserSetup:
    def __init__(self, session: AsyncSession):
        self.__table = UserModel
        self.session = session

    async def get_user(self, user_id: int) -> UserResult:
        query = select(self.__table).options(joinedload(self.__table.addresses),
                                             joinedload(self.__table.basket),
                                             joinedload(self.__table.wishlists),
                                             ).where(self.__table.id == user_id)
        result = await self.session.execute(query)
        user = result.first()[0]
        return [UserResult.model_validate(user)]
