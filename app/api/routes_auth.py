from fastapi import APIRouter
from pydantic import BaseModel
from core.security import create_jwt_token


router = APIRouter()

class AuthRouter(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(data: AuthRouter):
    if (data.username == 'admin') and (data.password == 'admin'):
        token = create_jwt_token({'sub': data.username})
        return {'access_token': token}
    return {'error': 'Invalid credentials'}
