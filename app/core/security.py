from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.core.config import settings


def create_jwt_token(data: dict, expiry_minutes=30):
    payload = data.copy()
    expiry_time = datetime.now(timezone.utc) + timedelta(minutes=expiry_minutes)
    payload.update(
        {'exp' : expiry_time}
    )
    return jwt.encode(
        payload,
        settings.JWT_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(
                        token,
                        settings.JWT_KEY,
                        settings.JWT_ALGORITHM
                    )
        return payload
    except JWTError:
        return None