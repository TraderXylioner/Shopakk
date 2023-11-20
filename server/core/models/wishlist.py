from sqlalchemy import String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class WishlistModel(BaseModel):
    __tablename__ = 'wishlist'
    wishlist_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(256))
    created_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship('UserModel', back_populates='wishlists')
    products = relationship('WishlistProductModel', back_populates='wishlist')
