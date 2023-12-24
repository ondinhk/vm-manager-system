from app.models.action_model import ActionModel, ActionResponse
from app.repositories.base_repository import MongoDBClient
from app.services.vm_serivce import VMService
from fastapi import HTTPException


class ActionService:
    mongo_client = MongoDBClient(collection_name="actions")

    @classmethod
    async def create_action(cls, credit: ActionModel):
        await VMService.get_vm_by_name(credit.vm_name)
        await cls.mongo_client.create_item(credit.model_dump())

    @classmethod
    async def get_list_action(cls):
        data = await cls.mongo_client.read_items()
        return [ActionResponse(id=str(item.get('_id')), **item) for item in data]

    @classmethod
    async def update_action(cls, video_id: str, body: ActionModel):
        await cls.mongo_client.update_item(video_id, body.model_dump())

    @classmethod
    async def delete_action(cls, video_id):
        await cls.mongo_client.delete_item(video_id)

    @classmethod
    async def get_action_by_name(cls, vm_name: str):
        action = await cls.mongo_client.find_by_query({'vm_name': vm_name})
        if not action:
            raise HTTPException(status_code=404, detail="VMModel not found")
        return ActionResponse(id=str(action.get('_id')), **action)
