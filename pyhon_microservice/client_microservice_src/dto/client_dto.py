from pydantic import BaseModel

class ClientDto(BaseModel):
    client_id: int
    name: str
    surname: str
    balance: int
    online: bool