from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class WishlistProductModel(BaseModel):
    __tablename__ = 'wishlist_product'
    wishlist_product_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    wishlist_id: Mapped[int] = mapped_column(ForeignKey('wishlist.wishlist_id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'))

    wishlist = relationship('WishlistModel', back_populates='products')
    product = relationship('ProductModel', back_populates='wishlists')
