from sqlalchemy import String, TIMESTAMP, func, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class ProductModel(BaseModel):
    __tablename__ = 'product'
    product_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    price: Mapped[float] = mapped_column(CheckConstraint('price > 0', name='check_price'))
    discount: Mapped[float] = mapped_column(CheckConstraint('discount > 0 AND discount < 1', name='check_discount'), default=0.00)
    icon: Mapped[str] = mapped_column()
    created_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    characteristics = relationship('CharacteristicModel', back_populates='product')
    images = relationship('ImageModel', back_populates='product')
    baskets = relationship('BasketProductModel', back_populates='product')
    wishlists = relationship('WishlistProductModel', back_populates='product')
