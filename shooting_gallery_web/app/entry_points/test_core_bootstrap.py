import os
import signal
import webbrowser
import threading
import time
import cv2
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.utils.cams_utils.cam_initialize import CamInitialize
from app.utils.cams_utils.frame_brightness_calculator import FrameBrightnessCalculator
from shared.pathings.path_config import PathConfig

from shared.pathings.frontend_path_config import router as path_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/resources", StaticFiles(directory=PathConfig.RESOURCES_PATH), name="resources")
app.mount("/data", StaticFiles(directory=PathConfig.DATA_PATH), name="data")
app.mount("/sounds", StaticFiles(directory=PathConfig.SOUNDS_PATH), name="sounds")
app.mount("/pages", StaticFiles(directory=PathConfig.PAGES_PATH), name="pages")
app.include_router(path_router)

class TestCoreBootstrap:
    def __init__(self, cam_index=0):
        self.frame_brightness_calculator = FrameBrightnessCalculator()
        self.camInitialize = CamInitialize()
        self.videoCapture = self.camInitialize.GetVideoCapture(cam_index)

    def start_property_core(self):
        while True:
            frame, isCaptureRetrieve = self.videoCapture.GetMatrix()
            if not isCaptureRetrieve or frame is None:
                break

            _, buffer = cv2.imencode('.jpg', frame)

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

    @staticmethod
    def start_base_core(cam_index=0):
        camInitialize = CamInitialize()
        videoCapture = camInitialize.GetVideoCapture(cam_index)

        while True:
            frame, isCaptureRetrieve = videoCapture.GetMatrix()
            cv2.imshow("Test", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                break

core = TestCoreBootstrap(cam_index=0)

@app.get("/video")
def video():
    return StreamingResponse(core.start_property_core(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/menu")
def route_menu():
    return FileResponse(PathConfig.MENU_PAGE_PATH)

@app.get("/video_page")
def route_video_page():
    return FileResponse(PathConfig.VIDEO_STREAM_PAGE_PATH)

@app.get("/video_stream_page.js")
def route_stream_scr():
    return FileResponse(PathConfig.VIDEO_STREAM_SCR_PATH)

@app.get("/menu_page.js")
def route_menu_src():
    return FileResponse(PathConfig.MENU_SCR_PATH)

def kill_process_with_delay():
    time.sleep(0.5)
    core.videoCapture.cleanup()
    os.kill(os.getpid(), signal.SIGINT)

def open_browser():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:8000/menu")


if __name__ == "__main__":
    import uvicorn

    threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_config={"version": 1, "disable_existing_loggers": True}
    )

    print("Server is start!")