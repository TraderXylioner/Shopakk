from sqlalchemy import String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import BaseModel


class AddressModel(BaseModel):
    __tablename__ = 'address'
    address_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id = mapped_column(ForeignKey('user.id'))
    name: Mapped[str] = mapped_column(String(64))
    city: Mapped[str] = mapped_column(String(64))
    street: Mapped[str] = mapped_column(String(64))
    house: Mapped[int] = mapped_column()
    apartment: Mapped[int] = mapped_column()
    selected: Mapped[bool] = mapped_column()
    added_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship('UserModel', back_populates='addresses')
