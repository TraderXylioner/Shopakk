from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from server.api.v1.products.schemas import ProductQuery
from server.api.v1.products.setup import ProductSetup
from server.core.setup import get_session

router = APIRouter(prefix='/products', tags=['product'])


@router.get('/{product_id}')
async def get_product(product_id: int,
                      session: AsyncSession = Depends(get_session)):
    async with session.begin():
        data = await ProductSetup(session=session).get_product(product_id=product_id)
    return {'status': status.HTTP_200_OK, 'data': data}


@router.post('/create_product')
async def create_product(params: ProductQuery,
                         session: AsyncSession = Depends(get_session)):
    async with session.begin():
        data = await ProductSetup(session=session).create_product(params=params)
    return {'status': status.HTTP_200_OK, 'data': {'product_id': data}}
