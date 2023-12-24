from typing import Optional

from pydantic import BaseModel


class ActionModel(BaseModel):
    vm_name: str
    username: str
    password: str
    email: str
    email_password: str
    platform: Optional[str] = 'None'
    channel: Optional[str] = 'None'
    status: Optional[int] = 500
    alive: Optional[int] = 0


class ActionResponse(BaseModel):
    id: str
    vm_name: str
    username: str
    password: str
    email: str
    email_password: str
    platform: str
    channel: str
    status: int
    alive: int
