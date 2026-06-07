from pydantic import BaseModel
from typing import Optional

class ClientDto(BaseModel):
    client_id: Optional[int] = None
    name: str
    surname: str
    online: bool = True