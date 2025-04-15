from typing import List
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session

from marshaller import UserMarshaller
from parser import UserParser
from db.db_api import connect
from db import db_user

user_router = APIRouter(prefix='/api/v1', tags=["user"])


# Get all users
@user_router.get('/users', response_model=List[UserMarshaller])
def get(db: Session = Depends(connect)):
    return db_user.get_users(db)

# Create User
@user_router.post('/user', response_model=UserMarshaller)
def post(request: UserParser, db: Session = Depends(connect)):
    return db_user.create_user(db, request)

# Get on user
@user_router.get('/user/{id}', response_model=UserMarshaller)
def get(id: int, db: Session = Depends(connect)):
    return db_user.get_user(db, id)

# Update user
@user_router.post('/user/{id}', response_model=UserMarshaller)
def post(id: int, request: UserParser, db: Session = Depends(connect)):
    db_user.update_user(db, id, request)
    return "ok"

# Delete user
@user_router.delete('/user/{id}')
def delete(id: int, db: Session = Depends(connect)):
    db_user.delete_user(db, id)
    return "ok"