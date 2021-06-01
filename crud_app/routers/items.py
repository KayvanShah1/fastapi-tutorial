from typing import Optional
from fastapi import APIRouter

from crud_app.models.item import Item


router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.get("/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}