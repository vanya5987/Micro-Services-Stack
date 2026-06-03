from fastapi.routing import APIRouter
from postgre_api import PostgresApi

router = APIRouter(prefix="/clients", tags=["Clients"])
api = PostgresApi()

@router.post("/")
async def create_client(client_id: int):
    return await api.create_client(client_id)

@router.get("/{id}/")
async def get_client(client_id: int):
    return await api.get_client(client_id)

@router.delete("/{id}/")
async def delete_client(client_id: int):
    return await api.delete_client(client_id)

@router.put("/{id}/")
async def hard_update_client(client_id: int):
    return await api.hard_update_client(client_id)

@router.patch("/{id}/")
async def soft_update_client(client_id: int):
    return await api.soft_update_client(client_id)