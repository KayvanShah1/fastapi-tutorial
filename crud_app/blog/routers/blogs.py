from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models
from blog.dependencies import oauth2
from sqlalchemy.orm import Session
from blog.helpers import blog_ops

router = APIRouter(prefix="/blog", tags=["Blogs"])

get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def all(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog_ops.get_all(db)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog_ops.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog_ops.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog_ops.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog_ops.show(id, db)
