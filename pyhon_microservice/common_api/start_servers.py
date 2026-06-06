from operator_microservice_src.api.operators_api import router as operators_router
from client_microservice_src.api.clients_api import router as clients_router
from call_generator_microservice.api.call_generator import router as call_generator_router
from fastapi import FastAPI
from multiprocessing import Process

from common_api.run_uvicorn_server import ServerRunner

operator_microservice = FastAPI(title="Asterisk Operators Microservice")
operator_microservice.include_router(operators_router)

client_microservice = FastAPI(title="Asterisk Clients Microservice")
client_microservice.include_router(clients_router)

call_generator = FastAPI(title="Asterisk Calls Generator")
call_generator.include_router(call_generator_router)

if __name__ == "__main__":
    client_process = Process(target=ServerRunner.create_and_run_server,
                            args=("start_servers:client_microservice", 8001))
    operator_process = Process(target=ServerRunner.create_and_run_server,
                               args=("start_servers:operator_microservice", 8002))

    call_generator_process = Process(target=ServerRunner.create_and_run_server,
                                     args=("start_servers:call_generator", 8003))

    client_process.start()
    operator_process.start()
    call_generator_process.start()

    client_process.join()
    operator_process.join()
    call_generator_process.join()