
from pymongo import MongoClient, collection
from ..utils.env_utils import get_env, EnvKey

def get_client(database_name: str, collection_name: str) -> tuple[MongoClient, collection.Collection]:
    url = get_env(EnvKey.MONGO_URL, "mongodb://localhost:27017")
    client = MongoClient(url)

    try:
        database = client.get_database(database_name)
        return (client, database.get_collection(collection_name))
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

