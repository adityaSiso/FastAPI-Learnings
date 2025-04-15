"""
This module is to perform DB operations on article table.
"""
from sqlalchemy.orm.session import Session

from db.models import Article
from parser import ArticleParser

def create_article(db: Session, request: ArticleParser):
    pass

def get_articles(db: Session):
    pass

def get_article(db: Session, id: int):
    pass