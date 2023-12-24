from app.models.video_model import VideoModel, VideoResponse
from app.repositories.base_repository import MongoDBClient
from fastapi import HTTPException


class VideoService:
    mongo_client = MongoDBClient(collection_name="videos")

    @classmethod
    async def create_video(cls, vm: VideoModel):
        await cls.mongo_client.create_item(vm.model_dump())

    @classmethod
    async def get_list_video(cls):
        data = await cls.mongo_client.read_items()
        return [VideoResponse(id=str(item.get('_id')), **item) for item in data]

    @classmethod
    async def update_video(cls, video_id: str, body: VideoModel):
        video = await cls.mongo_client.read_item(video_id)
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        await cls.mongo_client.update_item(video_id, body.model_dump())

    @classmethod
    async def delete_video(cls, video_id):
        video = await cls.mongo_client.read_item(video_id)
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        await cls.mongo_client.delete_item(video_id)
