from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from models import schemas
from models.datebase import get_db
from controllers.user import register, get_user_by_token
from secure.hash import apikey_header

router = APIRouter()

@router.post("/register", response_model=schemas.SelfUser, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)

@router.get("/self", response_model=None)
def self_user(access_token: str = Depends(apikey_header), db: Session = Depends(get_db)):
    return get_user_by_token(access_token=access_token, db=db)