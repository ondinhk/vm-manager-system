from typing import Optional

from pydantic import BaseModel


class VMModel(BaseModel):
    name: str
    ip_address: str
    proxy: Optional[str] = 'None'
    group: str


class VMResponse(BaseModel):
    id: str
    name: str
    ip_address: str
    proxy: str
    group: str
