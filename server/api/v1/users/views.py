from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from server.api.v1.users.setup import UserSetup
from server.core.setup import get_session

router = APIRouter(prefix='/users', tags=['user'])


@router.get('/{user_id}')
async def get_user(user_id: int,
                   session: AsyncSession = Depends(get_session)):
    async with session.begin():
        data = await UserSetup(session=session).get_user(user_id=user_id)
    return {'status': status.HTTP_200_OK, 'data': data}
