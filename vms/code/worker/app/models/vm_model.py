from pydantic import BaseModel


class VMResponse(BaseModel):
    id: str
    name: str
    username: str
    password: str
    email: str
    ip_address: str
    mac: str
    action: str
    proxy: str
    alive: int
    group: str
    status: int
    client_id: str
