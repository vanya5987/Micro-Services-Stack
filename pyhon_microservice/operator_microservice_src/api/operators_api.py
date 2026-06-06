from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import *

from common_api.create_session import CreateEngine

from operator_microservice_src.api.create_operators_tables import Operators
from operator_microservice_src.dto.operator_dto import OperatorDto

router = APIRouter(prefix="/operators")
engine = CreateEngine("postgresql+asyncpg://postgres:password@localhost:5432/operators")

@router.post("/")
async def create_operator(operator_dto: OperatorDto, session = Depends(engine.async_session_factory)):
    try:
        operator_params: dict = {
            "Name": operator_dto.name,
            "Surname": operator_dto.surname,
            "Online": operator_dto.online,
            "Operator_is_busy": operator_dto.operator_is_busy
        }

        if operator_dto.operator_id != 0:
            operator_params["ID"] = operator_dto.operator_id

        new_operator = Operators(**operator_params)

        session.add(new_operator)
        await session.commit()
        await session.refresh(new_operator)

        return {"status": "success", "details": f"Operator {new_operator.ID}:"
                                                f"{new_operator.Name} {new_operator.Surname} created"}
    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.get("/")
async def get_operators(last_id: int = 0, slice_size: int = 100, session = Depends(engine.async_session_factory)):
    try:
        query = (select(Operators)
                 .where(Operators.ID > last_id)
                 .order_by(Operators.ID)
                 .limit(slice_size))

        operators = await session.execute(query)

        operators_db = operators.scalars().all()

        return [OperatorDto(
            operator_id=operator.ID,
            name=operator.Name,
            surname=operator.Surname,
            online=operator.Online,
            operator_is_busy=operator.Operator_is_busy
        ) for operator in operators_db]

    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.delete("/{operator_id}")
async def delete_operator(operator_id: int, session = Depends(engine.async_session_factory)):
    try:
        operator = (delete(Operators)
                    .where(Operators.ID == operator_id))

        result = await session.execute(operator)
        await session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return {"status": "success", "details": f"Operator {operator_id} deleted"}
    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.patch("/{operator_id}")
async def update_operator(operator_id: int, operator: OperatorDto, session = Depends(engine.async_session_factory)):
    try:
        operator_params: dict = {
            "Operator_is_busy": operator.operator_is_busy
        }

        if operator.online != None:
            operator_params["Online"] = operator.online

        query = (update(Operators)
                 .where(Operators.ID == operator_id)
                 .values(**operator_params)
                 )

        result = await session.execute(query)
        await session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return {"status": "success", "details": f"Operator {operator_id} updated!"}

    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))

@router.get("/free")
async def get_free_operator(session = Depends(engine.async_session_factory)):
    try:
        query = (select(Operators)
                 .where(
            Operators.Operator_is_busy == False,
                        Operators.Online == True)
                 .order_by(Operators.ID)
                 .limit(1)
                 )

        result = await session.execute(query)
        operator_db = result.scalars().first()

        if operator_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        operator_db.Operator_is_busy = True
        await session.commit()

        return OperatorDto(
            operator_id=operator_db.ID,
            name=operator_db.Name,
            surname=operator_db.Surname,
            online=operator_db.Online,
            operator_is_busy=operator_db.Operator_is_busy
        )

    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))