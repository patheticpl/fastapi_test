from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.tokens import auth_token
from models import schemas
from models.datebase import get_db

router = APIRouter()


@router.post("/create", response_model=schemas.Token, status_code=201)
def create_token(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return auth_token(db=db, user_data=user_data)
