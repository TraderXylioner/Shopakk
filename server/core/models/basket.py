from sqlalchemy import TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class BasketModel(BaseModel):
    __tablename__ = 'basket'
    basket_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), unique=True)
    added_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship('UserModel', back_populates='basket')
    products = relationship('BasketProductModel', back_populates='basket')
