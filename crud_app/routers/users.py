from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud_app.dependencies.hashing import Hash
from crud_app.databases.blog import get_db
from crud_app.schemas.blog import UserSchema
from crud_app.models.blog import User, ShowUser


router = APIRouter(
    prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}}
)


@router.post("/{id}", response_model=ShowUser)
def create(request: User, db: Session = Depends(get_db)):
    new_user = UserSchema(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserSchema).filter(UserSchema.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )
    return user
