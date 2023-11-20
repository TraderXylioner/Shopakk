from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ImageQuery(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    url: str


class ImageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    image_id: int
    product_id: int
    url: str
    added_time: datetime
