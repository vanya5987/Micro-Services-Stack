from app.utils.os_system_utils.get_system_type import SystemTypeGetter

from typing import List

import subprocess
import screeninfo
import shutil
import os

class SystemComponentsCalculator:
    @staticmethod
    def get_multiplatform_processor() -> str:
        processor: str = [
            line.strip()
            for line in subprocess.run(
                "wmic cpu get name",
                capture_output=True,
                text=True,
                shell=True,
                timeout=5
            ).stdout.split('\n')
            if line.strip() and "Name" not in line
        ][0] if SystemTypeGetter.system_is_windows() else [
            line.split(':')[1].strip()
            for line in subprocess.run(
                "cat /proc/cpuinfo",
                capture_output=True,
                text=True,
                shell=True,
                timeout=5
            ).stdout.split('\n')
            if 'model name' in line
        ][0]

        return processor

    @staticmethod
    def get_kernel_version() -> str:
        kernel_version: str = ("Windows" if SystemTypeGetter.system_is_windows()
                               else subprocess.run("uname -r", capture_output=True, text=True,
                                                   shell=True, timeout=5).stdout.strip())

        return kernel_version

    @staticmethod
    def get_screen_resolution() -> str:
        resolution: str = f"{screeninfo.get_monitors()[0].width}x{screeninfo.get_monitors()[0].height}" \
            if len(screeninfo.get_monitors()) > 0 else "N/A"

        return resolution

    @staticmethod
    def get_v4l2_ctl_util():
        if shutil.which("v4l2-ctl") is None:
            return "Utils is not installed (only for linux)!"

        result = subprocess.run(["v4l2-ctl", "--version"],
                              capture_output=True, text=True, check=False, timeout=5)

        return " ".join(result.stdout.split())

    @staticmethod
    def get_tkinter_lib() -> str:
        try:
            result = subprocess.run([
                    "python", "-c", "import tkinter; print(tkinter.TkVersion)"
            ], capture_output=True, text=True, check=True, timeout=5)
        except:
            return "Is not installed!"

        return " ".join(result.stdout.split())

    @staticmethod
    def get_perms():
        import getpass

        perms: List[str] = []

        perms.append(f"(username:{getpass.getuser()})")

        if SystemTypeGetter.system_is_windows():
            try:
                import ctypes
                if ctypes.windll.shell32.IsUserAnAdmin():
                    perms.append("(admin:true)")
                else:
                    perms.append("(admin:false)")
            except:
                perms.append("(admin:unknown)")
        else:
            if os.geteuid() == 0:
                perms.append("(admin:true)")
            else:
                perms.append("(admin:false)")

        current_dir = os.getcwd()
        home_dir = os.path.expanduser("~")

        perms.append(f"(write_current_dir:{'true' if os.access(current_dir, os.W_OK) else 'false'})")
        perms.append(f"(write_home_dir:{'true' if os.access(home_dir, os.W_OK) else 'false'})")

        return " ".join(perms)