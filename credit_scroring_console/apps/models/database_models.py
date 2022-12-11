from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel, validator, validate_email


class UserRoleEnum(str, Enum):

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return name

    staff = auto()
    client = auto()
    company = auto()


class UserModel(BaseModel):

    id: Optional[int]
    email: Optional[str]
    username: Optional[str]
    user_password: Optional[str]
    user_role: Optional[UserRoleEnum]
    is_active: Optional[bool]
    is_login: Optional[bool]

    @validator('email')
    def validate_email(cls, value: str):
        assert validate_email(value)
        return value
