from fastapi import APIRouter

blog_router = APIRouter(prefix='/api/v1', tags=['v1'])

@blog_router.get('/blog/author/{id}', tags=['blog', 'user'])
def get_user(id: int):
    return {'author_id': id, 'blog_id': id**3}
