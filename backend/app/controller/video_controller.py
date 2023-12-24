from typing import List

from app.log import logger
from app.models.video_model import VideoModel, VideoResponse
from app.services.video_service import VideoService
from fastapi import APIRouter

video_route = APIRouter(tags=['Videos'])


# Create
@video_route.post("/videos")
async def create_video(vm: VideoModel):
    logger.info("Create video")
    await VideoService.create_video(vm)
    return "success"


@video_route.get("/videos", response_model=List[VideoResponse])
async def read_video():
    return await VideoService.get_list_video()


@video_route.put("/videos/{video_id}")
async def update_video(video_id: str, body: VideoModel):
    await VideoService.update_video(video_id, body)
    return 'success'


@video_route.delete("/videos/{video_id}")
async def delete_video(video_id: str):
    logger.info("Delete video")
    await VideoService.delete_video(video_id)
    return 'success'
