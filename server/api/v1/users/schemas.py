from typing import List

from pydantic import BaseModel, ConfigDict


class UserResult(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: str
    first_name: str | None
    second_name: str | None
    age: int | None
    role: str | None
    addresses: List[dict | None]
    basket: List[dict | None]
    wishlists: List[dict | None]


class RegisterUserRequest(BaseModel):
    email: str
    first_name: str
    second_name: str
    age: int
    password: str


class LoginUserRequest(BaseModel):
    email: str
    password: str
