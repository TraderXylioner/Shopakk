from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from server.api.v1.products.schemas import ProductResponse
from server.core.models.characteristic import CharacteristicModel
from server.core.models.image import ImageModel
from server.core.models.product import ProductModel


class ProductSetup:
    def __init__(self, session: AsyncSession):
        self.__table = ProductModel
        self.characteristic_table = CharacteristicModel
        self.image_table = ImageModel
        self.session = session

    async def create_product(self, params):
        product = ProductModel(name=params.name, price=params.price, discount=params.discount, icon=params.icon)
        self.session.add(product)

        characteristics = [self.characteristic_table(product=product, name=char.name, value=char.value)
                           for char in params.characteristics]
        self.session.add_all(characteristics)

        images = [self.image_table(product=product, url=img.url) for img in params.images]
        self.session.add_all(images)

        await self.session.flush()
        product_id = product.product_id
        await self.session.commit()

        return product_id

    async def get_product(self, product_id: int) -> ProductResponse:
        query = select(self.__table).options(joinedload(self.__table.characteristics),
                                             joinedload(self.__table.images)
                                             ).where(self.__table.product_id == product_id)
        result = await self.session.execute(query)
        product = result.first()[0]
        return [ProductResponse.model_validate(product)]
