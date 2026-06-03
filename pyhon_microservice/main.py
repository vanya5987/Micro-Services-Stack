from fastapi import FastAPI
from test_endpoints import router

import time
import webbrowser
import threading

app = FastAPI()

app.include_router(router)

def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    import uvicorn

    threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_config={"version": 1, "disable_existing_loggers": True}
    )