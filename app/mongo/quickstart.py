from pymongo import MongoClient

url = "mongodb://localhost:27017"
client = MongoClient(url)

try:
    database = client.get_database("ContentStore")
    contents = database.get_collection("Contents")

    query = {"type": "1"}
    content = contents.find_one(query)

    print(content)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)