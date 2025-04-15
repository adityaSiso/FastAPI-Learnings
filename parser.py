"""
This module is to define the pydantic objects.
"""
from pydantic import BaseModel


class UserParser(BaseModel):
    username: str
    email: str
    password: str

class ArticleParser(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int