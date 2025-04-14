from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Query
from fastapi import Body
from fastapi import Path

# Pydantic parser
class LoginParser(BaseModel):
    user: str
    password: str

blog_router = APIRouter(prefix='/api/v1', tags=['v1'])


# Dependencies
from fastapi import Depends

def required_stuff():
    return {'Message': "Hi how are you doing?"}

# Here the order of endpoints is important.
@blog_router.get('/blog/all')
def get(page: int = 1, items: int = 10, 
        required: dict = Depends(required_stuff)):    # Query Params
    return "All blogs returned"

@blog_router.get('/blog/{id}')      # Path Params
def get(id: int):           # This is not type annotation this is
    return f'Hello {id}!'   # is an actual validation via pydantic

class BlogType(Enum):
    short = 'short'
    long = 'long'

@app.get('/blog/type/{type}')
def get(type: BlogType):
    return f'You requested a {type} blog type.'


@blog_router.get('/blog/author/{id}', tags=['blog', 'user'])
def get_user(id: int):
    return {'author_id': id, 'blog_id': id**3}

# Pydantic parser example
@blog_router.post('/login')
def special_login(data: LoginParser):
    return {'User': data.user.title()}

# Parameter Metadata
@blog_router.get('/param_info')
def get(id: int = Query(None, description='This is a unique id',
                        deprecated=True)):
    return id
