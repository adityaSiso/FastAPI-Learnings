from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from router.users import user_router
from router.endpoint import blog_router
from db.db_api import engine
from db import models

app = FastAPI()

app.include_router(blog_router)
app.include_router(user_router)

@app.get('/')
def index():
    return "Welcome to FastAPI Application!"

models.Base.metadata.create_all(engine)

# uvicorm command `uvicorn file_name:object_name [options]`