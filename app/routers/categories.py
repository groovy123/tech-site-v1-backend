import logging
from fastapi import APIRouter
from ..mongo.content_repository import read_all_categories
from ..models.model import Content

logger = logging.getLogger('uvicorn')

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.get("/")
async def read_categories() -> list[Content]:
    return await read_all_categories()
