from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import *

from common_api.create_session import CreateEngine

from client_microservice_src.api.create_clients_tables import Clients
from client_microservice_src.dto.client_dto import ClientDto

router = APIRouter(prefix="/clients")
engine = CreateEngine("postgresql+asyncpg://postgres:password@localhost:5432/clients")

@router.post("/")
async def create_client(client: ClientDto, session = Depends(engine.async_session_factory)):
    try:
        client_params: dict = {
            "Name": client.name,
            "Surname": client.surname,
            "Balance": client.balance,
            "Online": client.online
        }

        if client.client_id != 0:
            client_params["ID"] = client.client_id

        new_client = Clients(**client_params)

        session.add(new_client)
        await session.commit()
        await session.refresh(new_client)

        return {"status": "success", "details": f"Client {new_client.ID}:"
                                                f" {new_client.Name} {new_client.Surname} has been created!"}
    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.get("/{client_id}")
async def get_client_by_id(client_id: int, session = Depends(engine.async_session_factory)):
    try:
        query = select(Clients).where(
            Clients.ID == client_id
        )

        result = await session.execute(query)
        client_db = result.scalars().first()

        if client_db is None or client_db.Online == False:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return ClientDto(
            client_id=client_db.ID,
            name=client_db.Name,
            surname=client_db.Surname,
            balance=client_db.Balance,
            online=client_db.Online
        )
    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.get("/")
async def get_clients_slice(last_id: int = 0, slice_size: int = 100, session=Depends(engine.async_session_factory)):
    try:
        query = (
            select(Clients)
            .where(Clients.ID > last_id)
            .order_by(Clients.ID)
            .limit(slice_size)
        )

        result = await session.execute(query)

        clients_db = result.scalars().all()

        response_data = [
            ClientDto(
                client_id=client.ID,
                name=client.Name,
                surname=client.Surname,
                balance=client.Balance,
                online=client.Online)
            for client in clients_db]

        return response_data
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.delete("/{client_id}")
async def delete_client(client_id: int, session = Depends(engine.async_session_factory)):
    try:
        query = delete(Clients).where(Clients.ID == client_id)

        result = await session.execute(query)
        await session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return {"status": "success", "details": f"Client {client_id} has been deleted!"}

    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.patch("/{client_id}")
async def update_client(client_id: int, client: ClientDto, session=Depends(engine.async_session_factory)):
    try:
        client_params: dict = {
            "Balance": client.balance,
            "Online": client.online
        }

        query = (update(Clients)
                 .where(Clients.ID == client_id)
                 .values(**client_params)
                 )

        result = await session.execute(query)
        await session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return {"status": "success", "details": f"Client {client_id} has been updated!"}

    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))
