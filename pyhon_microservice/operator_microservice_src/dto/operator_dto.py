from pydantic import BaseModel
from typing import Optional

class OperatorDto(BaseModel):
    operator_id: Optional[int] = None
    name: str
    surname: str
    online: bool = True
    operator_is_busy: bool = False