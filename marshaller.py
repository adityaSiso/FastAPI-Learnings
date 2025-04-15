"""
This module is to define the pydantic objects.
"""
from typing import List
from pydantic import BaseModel

class UserArticleMarshaller(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode = True

class UserMarshaller(BaseModel):
    username: str
    email: str
    articles: List[UserArticleMarshaller] = []
    class Config():
        orm_mode = True

class ArticleUserMarshaller(BaseModel):
    username: str
    email: str
    id: int

class ArticlesMarshaller(BaseModel):
    title: str
    content: str
    published: bool
    user: ArticleUserMarshaller
    class Config():
        orm_mode = True