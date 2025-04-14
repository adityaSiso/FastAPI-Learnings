"""
This module is to define the pydantic objects.
"""
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str