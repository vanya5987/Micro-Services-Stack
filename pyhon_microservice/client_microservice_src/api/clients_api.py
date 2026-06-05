from fastapi import APIRouter, Depends
from common_api.create_session import CreateEngine

from client_microservice_src.api.create_clients_tables import Clients
from client_microservice_src.dto.client_dto import ClientDto

router = APIRouter(prefix="/clients")
engine = CreateEngine("postgresql+asyncpg://postgres:password@localhost:5432/clients")

@router.post("/")
async def create_client(client: ClientDto, session = Depends(engine.async_session_factory)):
    try:
        new_client = Clients(
            ID=client.client_id,
            Name=client.name,
            Surname=client.surname,
            Balance=client.balance,
            Online=client.online
        )

        session.add(new_client)
        await session.commit()

        return {"status": "success", "details": f"Client {new_client.ID}:"
                                                f" {new_client.Name} {new_client.Surname} has been created!"}
    except Exception as ex:
        await session.rollback()

        return {"status": "error", "details" : f"{ex}"}