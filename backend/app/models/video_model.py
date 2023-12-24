from pydantic import BaseModel


class VideoModel(BaseModel):
    video_name: str
    video_time: float


class VideoResponse(BaseModel):
    id: str
    video_name: str
    video_time: float
