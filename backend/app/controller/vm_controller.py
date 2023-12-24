from typing import List

from app.log import logger
from app.models.vm_model import VMModel, VMResponse
from app.services.vm_serivce import VMService
from fastapi import APIRouter, HTTPException

vm_router = APIRouter(tags=['VM Manage'])


@vm_router.post("/vms")
async def create_vm(vm: VMModel):
    logger.info("Create VM")
    vm_id = await VMService.create_vm(vm)
    if not vm_id:
        raise HTTPException(status_code=400, detail="Create VM fail")
    return 'success'


@vm_router.post("/vms/init")
async def init_vms(vm: list[VMModel]):
    logger.info("Init vm")
    await VMService.init_vms(vm)
    return 'success'


@vm_router.get("/vms", response_model=List[VMResponse])
async def read_vms():
    return await VMService.get_vms()


@vm_router.get("/vms/{vm_id}", response_model=VMResponse)
async def read_vm(vm_id: str):
    return await VMService.get_vm(vm_id)


@vm_router.get("/vms/name/{vm_name}", response_model=VMResponse)
async def read_vm_by_name(vm_name: str):
    return await VMService.get_vm_by_name(vm_name)


@vm_router.put("/vms/{vm_id}")
async def update_vm(vm_id: str, body: VMModel):
    return await VMService.update_vm(vm_id, body)


@vm_router.delete("/vms/{vm_id}")
async def delete_vm(vm_id: str):
    return await VMService.delete_vm(vm_id)


@vm_router.delete("/vms")
async def delete_vm():
    return await VMService.delete_vms()
