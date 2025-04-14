"""
This module is to perform DB operations.
"""
import base64
from sqlalchemy.orm.session import Session

from schemas import UserBase
from db.models import User


def create_user(db: Session, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = base64.encode(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user