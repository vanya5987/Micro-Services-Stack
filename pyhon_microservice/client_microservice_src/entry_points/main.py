from client_microservice_src.api.clients_api import router
from fastapi import FastAPI

from common_api.run_uvicorn_server import ServerRunner

app = FastAPI(title="Asterisk Clients Microservice")
app.include_router(router)

if __name__ == "__main__":
    ServerRunner.create_and_run_server(reflection_name="main:app", port=8001)
