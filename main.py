from fastapi import FastAPI
from router import blog_router
from db.db_api import engine
from db import models

app = FastAPI()

app.include_router(blog_router)

@app.get('/')
def index():
    return "Welcome to FastAPI Application!"

models.Base.metadata.create_all(engine)

# uvicorm command `uvicorn file_name:object_name [options]`