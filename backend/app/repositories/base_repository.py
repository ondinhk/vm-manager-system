import os

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv('MONGODB_URI', None)
DATABASE_NAME = os.getenv('DATABASE_NAME', None)


class MongoDBClient:
    def __init__(self, collection_name: str):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.database = self.client[DATABASE_NAME]
        self.collection = self.database[collection_name]
        # self.client = None
        # self.database = None
        # self.collection = None

    async def create_item(self, item: dict):
        result = await self.collection.insert_one(item)
        return str(result.inserted_id)

    async def read_items(self):
        items = await self.collection.find().to_list(length=None)
        return items

    async def read_item(self, item_id: str):
        item = await self.collection.find_one({"_id": ObjectId(item_id)})
        return item

    async def update_item(self, item_id: str, updated_item: dict):
        result = await self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
        return result.modified_count == 1

    async def delete_item(self, item_id: str):
        result = await self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count == 1

    async def find_by_query(self, query: dict):
        return await self.collection.find_one(query)

    async def drop_collection(self):
        return await self.collection.drop()
