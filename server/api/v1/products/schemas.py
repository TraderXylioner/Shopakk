from datetime import datetime
from typing import List, Union

from pydantic import BaseModel, ConfigDict

from server.api.v1.characteristics.schemas import CharacteristicQuery, CharacteristicResponse
from server.api.v1.images.schemas import ImageQuery, ImageResponse


class ProductQuery(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    price: int
    discount: float
    icon: str
    characteristics: List[CharacteristicQuery]
    images: List[ImageQuery]


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    name: str
    price: int
    discount: float
    icon: str
    created_time: datetime
    characteristics: Union[List[CharacteristicResponse], None]
    images: Union[List[ImageResponse], None]
