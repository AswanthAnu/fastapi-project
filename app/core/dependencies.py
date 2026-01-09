from fastapi import HTTPException, Header
from app.core.security import verify_jwt_token
from app.core.config import settings


def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
def get_current_user(token: str = Header(...)):
    valid_token = verify_jwt_token(token)
    if not valid_token:
        raise HTTPException(status_code=401, detail="Invalid JWT Token")
    return valid_token