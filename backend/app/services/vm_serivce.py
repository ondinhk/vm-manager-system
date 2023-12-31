from app.models.vm_model import VMModel, VMResponse
from app.repositories.base_repository import MongoDBClient
from fastapi import HTTPException


class VMService:
    mongo_client = MongoDBClient(collection_name="vms")

    @classmethod
    async def init_vms(cls, vm: list[VMModel]):
        await cls.mongo_client.drop_collection()
        for item in vm:
            await cls.mongo_client.create_item(item.model_dump())

    @classmethod
    async def create_vm(cls, vm: VMModel):
        vm_exists = await cls.mongo_client.find_by_query(query={'name': vm.name})
        if vm_exists:
            raise HTTPException(status_code=400, detail="VMModel already exists")
        vm_id = await cls.mongo_client.create_item(vm.model_dump())
        return vm_id

    @classmethod
    async def get_vm(cls, vm_id: str):
        vm = await cls.mongo_client.read_item(vm_id)
        if not vm:
            raise HTTPException(status_code=404, detail="VMModel not found")
        return VMResponse(id=str(vm.get('_id')), **vm)

    @classmethod
    async def get_vm_by_name(cls, vm_name):
        vm = await cls.mongo_client.find_by_query({'name': vm_name})
        if not vm:
            raise HTTPException(status_code=404, detail="VMModel not found")
        return VMResponse(id=str(vm.get('_id')), **vm)

    @classmethod
    async def get_vms(cls):
        data = await cls.mongo_client.read_items()

        def get_index_from_name(vm):
            if vm["name"] == 'VM_MASTER':
                return -1
            return int(vm["name"].split("_")[1])

        sorted_vm_list = sorted(data, key=get_index_from_name)
        return [VMResponse(id=str(item.get('_id')), **item) for item in sorted_vm_list]

    @classmethod
    async def update_vm(cls, vm_id: str, body: VMModel):
        await cls.mongo_client.update_item(vm_id, body.model_dump())

    @classmethod
    async def delete_vm(cls, vm_id: str):
        await cls.get_vm(vm_id)
        await cls.mongo_client.delete_item(vm_id)

    @classmethod
    async def delete_vms(cls):
        await cls.mongo_client.drop_collection()
