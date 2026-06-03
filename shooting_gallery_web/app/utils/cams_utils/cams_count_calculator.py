from app.utils.os_system_utils.get_system_type import SystemTypeGetter
from typing import *
import cv2


class CamsCountCalculator:
    @staticmethod
    def get_available_cams() -> Dict[int, str]:
        if SystemTypeGetter.system_is_windows():
            return CamsCountCalculator._get_available_windows_cams()
        else:
            return CamsCountCalculator._get_available_linux_cams()

    @staticmethod
    def _get_available_windows_cams() -> Dict[int, str]:
        from pygrabber.dshow_graph import FilterGraph

        graph = FilterGraph()
        devices = graph.get_input_devices()

        return {
            index: f"{index + 1}. {name}"
            for index, name in enumerate(devices)
        }

    @staticmethod
    def _get_available_linux_cams() -> Dict[int, str]:
        import subprocess
        import re
        import os
        import fcntl
        import ctypes
        from typing import Dict

        availableCameras: Dict[int, str] = {}

        class v4l2_capability(ctypes.Structure):
            _fields_ = [
                ("driver", ctypes.c_char * 16),
                ("card", ctypes.c_char * 32),
                ("bus_info", ctypes.c_char * 32),
                ("version", ctypes.c_uint32),
                ("capabilities", ctypes.c_uint32),
                ("device_caps", ctypes.c_uint32),
                ("reserved", ctypes.c_uint32 * 3),
            ]

        VIDIOC_QUERYCAP = 0x80685600

        V4L2_CAP_VIDEO_CAPTURE = 0x00000001
        V4L2_CAP_VIDEO_CAPTURE_MPLANE = 0x00001000
        V4L2_CAP_META_CAPTURE = 0x00004000

        try:
            result = subprocess.run(
                ["v4l2-ctl", "--list-devices"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )

            currentName: str = "Unknown Camera"

            for line in result.stdout.split('\n'):
                line = line.strip()

                if line and ':' in line and not line.startswith('/dev/'):
                    currentName = line.split('(')[0].strip()

                elif line.startswith('/dev/video'):
                    match = re.search(r'video(\d+)', line)
                    if not match:
                        continue

                    devNum = int(match.group(1))
                    devPath = line.strip()

                    fd = None

                    try:
                        fd = os.open(devPath, os.O_RDWR | os.O_NONBLOCK)

                        cap = v4l2_capability()
                        fcntl.ioctl(fd, VIDIOC_QUERYCAP, cap)

                        caps = cap.capabilities
                        dcaps = cap.device_caps

                        if not ((dcaps & V4L2_CAP_VIDEO_CAPTURE) or
                                (dcaps & V4L2_CAP_VIDEO_CAPTURE_MPLANE)):
                            continue

                        if dcaps & V4L2_CAP_META_CAPTURE:
                            continue

                        driver = cap.driver.decode(errors="ignore").lower()
                        if "loopback" in driver or "v4l2loopback" in driver:
                            continue

                        availableCameras[devNum] = currentName

                    except Exception:
                        continue

                    finally:
                        if fd is not None:
                            os.close(fd)

        except (subprocess.SubprocessError, FileNotFoundError):
            for i in range(10):
                try:
                    cap = cv2.VideoCapture(i, cv2.CAP_V4L2)
                    if cap.isOpened():
                        availableCameras[i] = f"Camera {i}"
                        cap.release()
                except:
                    continue

        return availableCameras
