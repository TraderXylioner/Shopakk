from sqlalchemy import TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from base import BaseModel


class ImageModel(BaseModel):
    __tablename__ = 'image'
    image_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'))
    url: Mapped[str] = mapped_column()
    added_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now())
    update_time: Mapped[int] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    product = relationship('ProductModel', back_populates='images')
