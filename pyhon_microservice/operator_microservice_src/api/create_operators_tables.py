from sqlalchemy import MetaData
from sqlalchemy.orm import *

operators_metadata = MetaData()

class BaseModel(DeclarativeBase):
    metadata = operators_metadata

class Operators(BaseModel):
    __tablename__ = "Operators"

    ID: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
    Surname: Mapped[str]
    Online: Mapped[bool]
    Operator_is_busy: Mapped[bool]