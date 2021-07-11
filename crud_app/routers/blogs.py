from typing import List
from fastapi import APIRouter, status, HTTPException, Depends

from sqlalchemy.orm import Session

from crud_app.databases.blog import get_db
from crud_app.models.blog import ShowBlog, Blog
from crud_app.schemas.blog import BlogSchema


router = APIRouter(
    prefix="/blogs", tags=["Blogs"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(BlogSchema).all()
    return blogs


@router.get("/{id}", status_code=200, response_model=ShowBlog)
def show(db: Session = Depends(get_db)):
    blog = db.query(BlogSchema).filter(BlogSchema.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    return blog


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = BlogSchema(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put("/{id}")
def update(id: int, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(BlogSchema).filter(BlogSchema.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.update(request)
    db.commit()
    return f"Blog {id} updated"


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogSchema).filter(BlogSchema.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return f"Blog {id} deleted"
