from fastapi import APIRouter

from crud_app.models.user import User


router = APIRouter(
    prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}}
)
