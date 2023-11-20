from sqlalchemy import String, TIMESTAMP, func, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user'
    user_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    email: Mapped[str] = mapped_column(String(128))
    first_name: Mapped[str] = mapped_column(String(64))
    second_name: Mapped[str] = mapped_column(String(64))
    # balance: Mapped[float] = mapped_column(Float)
    age: Mapped[int | None] = mapped_column(CheckConstraint('age > 0 AND age < 120', name='check_age'))
    role: Mapped[str] = mapped_column(default='customer')
    hashed_password: Mapped[str] = mapped_column()
    created_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    addresses = relationship('AddressModel', back_populates='user')
    wishlists = relationship('WishlistModel', back_populates='user')
    basket = relationship('BasketModel', back_populates='user')
