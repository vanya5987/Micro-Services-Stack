from sqlalchemy import MetaData
from sqlalchemy.orm import *

clients_metadata = MetaData()

class BaseModel(DeclarativeBase):
    metadata = clients_metadata

class Clients(BaseModel):
    __tablename__ = "Clients"

    ID: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
    Surname: Mapped[str]
    Online: Mapped[bool]
