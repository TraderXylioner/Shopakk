from sqlalchemy import String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from base import BaseModel


class CharacteristicModel(BaseModel):
    __tablename__ = 'characteristic'
    characteristic_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'))
    name: Mapped[str] = mapped_column(String(128))
    value: Mapped[str] = mapped_column(String(128))
    added_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    product = relationship('ProductModel', back_populates='characteristics')
