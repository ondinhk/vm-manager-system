from typing import List

from app.log import logger
from app.models.action_model import ActionModel, ActionResponse
from app.services.action_service import ActionService
from fastapi import APIRouter

action_route = APIRouter(tags=['Actions'])


# Create
@action_route.post("/actions")
async def create_action(action: ActionModel):
    logger.info("Create action")
    await ActionService.create_action(action)
    return "success"


@action_route.get("/actions", response_model=List[ActionResponse])
async def read_actions():
    return await ActionService.get_list_action()


@action_route.get("/actions/{vm_name}", response_model=ActionResponse)
async def read_action_by_name(vm_name: str):
    return await ActionService.get_action_by_name(vm_name)


@action_route.put("/actions/{action_id}")
async def update_action(action_id: str, body: ActionModel):
    await ActionService.update_action(action_id, body)
    return 'success'


@action_route.delete("/actions/{action_id}")
async def delete_action(action_id: str):
    logger.info("Delete action")
    await ActionService.delete_action(action_id)
    return 'success'
