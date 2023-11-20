from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from base import BaseModel


class BasketProductModel(BaseModel):
    __tablename__ = 'basket_product'
    basket_product_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    basket_id: Mapped[int] = mapped_column(ForeignKey('basket.basket_id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'))
