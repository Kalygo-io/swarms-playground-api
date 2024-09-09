from fastapi import APIRouter, Request, Response

from slowapi.util import get_remote_address
from slowapi import Limiter
from src.deps import jwt_dependency

limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

@router.get("/")
@limiter.limit("5/minute")  # 5 requests per minute
def designSwarm(request: Request, response: Response, jwt: jwt_dependency):
    return {"status": "OK!"}