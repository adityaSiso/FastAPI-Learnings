from fastapi import FastAPI
from enum import Enum
from router import blog_router

app = FastAPI()

app.include_router(blog_router)

@app.get('/')
def index():
    return "hello world"

# uvicorm command `uvicorn file_name:object_name [options]`

# Here the order of endpoints is important.
@app.get('/blog/all')
def get(page: int = 1, items: int = 10):    # Query Params
    return "All blocks returned"

@app.get('/blog/{id}')      # Path Params
def get(id: int):           # This is not type annotation this is
    return f'Hello {id}!'   # is an actual validation via pydantic

class BlogType(Enum):
    short = 'short'
    long = 'long'

@app.get('/blog/type/{type}')
def get(type: BlogType):
    return f'You requested a {type} blog type.'
