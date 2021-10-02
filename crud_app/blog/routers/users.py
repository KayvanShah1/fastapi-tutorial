from fastapi import APIRouter
from crud_app.blog import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from blog.helpers import user_ops

router = APIRouter(prefix="/user", tags=["Users"])

get_db = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_ops.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_ops.show(id, db)
