"""
This module is to perform DB operations on user table.
"""
import base64
from sqlalchemy.orm.session import Session

from parser import UserParser
from db.models import User


def create_user(db: Session, request: UserParser):
    new_user = User(
        username = request.username,
        email = request.email,
        password = base64.b64encode(request.password.encode())
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def update_user(db: Session, id: int, request: UserParser):
    user = get_user(db, id)
    user.update({
        User.email: request.email,
        User.username: request.username,
        User.password: base64.b64encode(request.password.encode())
    })
    db.commit()

def delete_user(db: Session, id: int):
    user = get_user(db, id)
    db.delete(user)
    db.commit()