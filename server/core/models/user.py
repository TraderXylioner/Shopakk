from sqlalchemy import String, TIMESTAMP, func, CheckConstraint, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    second_name: Mapped[str] = mapped_column(String(64), nullable=True)
    # balance: Mapped[float] = mapped_column(Float)
    age: Mapped[int | None] = mapped_column(CheckConstraint('age > 0 AND age < 120', name='check_age'), nullable=True)
    role: Mapped[str] = mapped_column(default='customer')
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    addresses = relationship('AddressModel', back_populates='user')
    wishlists = relationship('WishlistModel', back_populates='user')
    basket = relationship('BasketModel', back_populates='user')
