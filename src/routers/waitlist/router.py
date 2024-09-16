from datetime import timedelta, datetime, timezone
import uuid
from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, BackgroundTasks, Request
from pydantic import BaseModel
from jose import jwt
from dotenv import load_dotenv
import os
from db.waitlist import Waitlist
from src.db.models import Account
from src.routers.auth.background_tasks import record_login
from src.routers.auth.background_tasks.send_reset_password_link_email_ses import send_reset_password_link_email_ses
from src.routers.auth.background_tasks.send_password_has_been_reset_email_ses import send_password_has_been_reset_email_ses
from src.deps import db_dependency, bcrypt_context

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

load_dotenv()

router = APIRouter()

class JoinWaitlistRequestBody(BaseModel):
    email: str

@router.post("/join")
async def create_account(db: db_dependency, body: JoinWaitlistRequestBody, request: Request):
    try:
        create_account_model = Waitlist(
            email=body.email,
            
        )
        db.add(create_account_model)
        db.commit()
        db.refresh(create_account_model)

        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print('create_user error', e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))