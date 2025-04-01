import logging
from bson import ObjectId
from pymongo import MongoClient, collection, results
from app.models.model import Content
from .client import get_client

logger = logging.getLogger('uvicorn')

async def create(content: Content) -> Content:
    client, collection = await get_content_client()
    with client as c:
        return collection.insert_one(content.model_dump())

async def update(content: Content) -> Content:
    client, collection = await get_content_client()
    with client as c:
        query_filter = {"_id": content._id}
        return collection.update_one(query_filter, content.model_dump())

async def replace(content: Content) -> results.UpdateResult:
    client, collection = await get_content_client()
    with client as c:
        query_filter = {"category": content.category}
        return collection.replace_one(query_filter, content.model_dump(), upsert=True)

async def delete(content: Content):
    client, collection = await get_content_client()
    with client as c:
        query_filter = {"_id": content._id}
        collection.delete_one(query_filter)

async def read_all() -> list[Content]:
    client, collection = await get_content_client()
    with client as c:
        return collection.find({})

async def read_all_categories() -> list[Content]:
    client, collection = await get_content_client()
    with client as c:
        cursor = collection.find({}, {"text": 0}).sort("category")
        # return [Content(**x) for x in cursor]
        contents = []
        for c in cursor:
            id = c.get("_id")
            content = Content(**c)
            content.id = str(id)
            contents.append(content)
        logger.info(f"read_all_categories. size={len(contents)}")
        return contents

async def read(id: str) -> Content:
    client, collection = await get_content_client()
    with client as c:
        result = collection.find_one({"_id": ObjectId(id)})
        content = Content(**result)
        content.id = str(result.get("_id"))
        return content

async def get_content_client() -> tuple[MongoClient, collection.Collection]:
    return get_client("ContentStore", "Contents")