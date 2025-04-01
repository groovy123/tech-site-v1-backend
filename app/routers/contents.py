import logging
from fastapi import APIRouter
from ..mongo.client import get_client
from ..mongo.content_repository import create, update, delete, read, read_all, replace
from ..models.model import Content

logger = logging.getLogger('uvicorn')

router = APIRouter(
    prefix="/contents",
    tags=["contents"],
)

@router.get("/")
async def read_contents() -> list[Content]:
    return read_all()

@router.get("/{id}")
async def read_conte(id: str):
    logger.info(f"read content. id={id}")
    return await read(id)

@router.post("/")
async def create_content(content: Content):
    result = await replace(content)
    logger.info(f"Suceess update document matched_count:{result.matched_count} modified_count:{result.modified_count} id:{result.upserted_id}.")
    return content

