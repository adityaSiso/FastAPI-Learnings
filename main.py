from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from router.users import user_router
from router.endpoint import blog_router
from db.db_api import engine
from db import models
from exceptions import CustomException

app = FastAPI()

app.include_router(blog_router)
app.include_router(user_router)

@app.get('/')
def index():
    return "Welcome to FastAPI Application!"

@app.exception_handler(CustomException)
def custom_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        exc.detail,
        status_code=status.HTTP_418_IM_A_TEAPOT
    )


models.Base.metadata.create_all(engine)

# uvicorm command `uvicorn file_name:object_name [options]`