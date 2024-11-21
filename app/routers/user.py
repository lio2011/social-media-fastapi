from .. import models, utils, schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine,SessionLocal, get_db
from typing import List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/",status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    user_query = db.query(models.User).filter(models.User.email == new_user.email)
    user_found = user_query.first()
    if(user_found == None):
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"user with email : {new_user.email} already exist")

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if(not user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id : {id} does not exists")
    return user