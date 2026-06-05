from pydantic import BaseModel

class OperatorDto(BaseModel):
    operator_id: int
    name: str
    surname: str
    online: bool
    operator_is_busy: bool