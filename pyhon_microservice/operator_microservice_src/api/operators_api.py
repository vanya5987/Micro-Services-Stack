from fastapi import APIRouter, Depends
from common_api.create_session import CreateEngine

from operator_microservice_src.api.create_operators_tables import Operators

router = APIRouter()
engine = CreateEngine("postgresql+asyncpg://postgres:password@localhost:5432/operators")

