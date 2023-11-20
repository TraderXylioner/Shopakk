from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CharacteristicQuery(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    value: str


class CharacteristicResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    characteristic_id: int
    product_id: int
    name: str
    value: str
    added_time: datetime
