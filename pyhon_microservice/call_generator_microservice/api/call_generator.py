from fastapi import APIRouter, HTTPException, status
import asyncio
import httpx

router = APIRouter(prefix="/generate-call")

CLIENTS_SERVICE_URL = "http://127.0.0.1:8001/clients/"
OPERATORS_SERVICE_URL = "http://127.0.0.1:8002/operators/"
CALL_DATA_SERVICE_URL = ""

@router.post("/")
async def generate_call(client_id: int):
    async with httpx.AsyncClient() as http_client:
        try:
            client_resp = await http_client.get(f"{CLIENTS_SERVICE_URL}{client_id}")
            if client_resp.status_code == 404:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
            client_resp.raise_for_status()

            client_data = client_resp.json()
            current_balance = client_data.get("balance", 0)

            if current_balance <= 0:
                raise HTTPException(
                    status_code=status.HTTP_402_PAYMENT_REQUIRED)

            operator_resp = await http_client.get(f"{OPERATORS_SERVICE_URL}free")
            if operator_resp.status_code == 404:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
            operator_resp.raise_for_status()

            operator_data = operator_resp.json()
            operator_id = operator_data.get("operator_id")

            await asyncio.sleep(4)

            patch_operator_data = {
                "operator_id": operator_id,
                "name": operator_data.get("name"),
                "surname": operator_data.get("surname"),
                "online": True,
                "operator_is_busy": False
            }
            op_update_resp = await http_client.patch(
                f"{OPERATORS_SERVICE_URL}{operator_id}",
                json=patch_operator_data
            )
            op_update_resp.raise_for_status()

            new_balance = max(0, current_balance - 10)
            patch_client_data = {
                "client_id": client_id,
                "name": client_data.get("name"),
                "surname": client_data.get("surname"),
                "balance": new_balance,
                "online": client_data.get("online")
            }
            client_update_resp = await http_client.patch(
                f"{CLIENTS_SERVICE_URL}{client_id}",
                json=patch_client_data
            )
            client_update_resp.raise_for_status()

            return {
                "status": "call_finished",
                "client_id": client_id,
                "operator_id": operator_id,
                "old_balance": current_balance,
                "new_balance": new_balance
            }

        except HTTPException:
            raise
        except httpx.RequestError as ex:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(ex))
        except httpx.HTTPStatusError as status_ex:
            raise HTTPException(status_code=status_ex.response.status_code, detail=status_ex.response.text)