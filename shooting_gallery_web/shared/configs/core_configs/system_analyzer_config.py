from app.utils.os_system_utils.system_components_calculator import SystemComponentsCalculator

from typing import List

import platform
import psutil

class SystemAnalyzerConfig:
    BASE_LOG_HEADERS: List[str] = ["OS type: {0}", "OS version: {0}", "Processor: {0}", "Cores: {0}", "Threads: {0}",
                                        "Frequency : {0} MHz", "Memory: {0} GB", "Resolution: {0}", "Kernel: {0}",
                                   "V4L2_CTL: {0}", "Permission: {0}", "Tkinter: {0}"]

    BASE_SYSTEM_INFO_KEYS: List[str] = ["system_type", "system_name", "processor", "cpu_cores", "cpu_threads",
                                "cpu_freq", "total_ram_gb", "screen_resolution", "kernel_version", "v4l2_ctl_version",
                                "permission", "tkinter"]

    OS_TYPE: str = platform.system()
    OS_VERSION: str = platform.platform()
    PROCESSOR: str = SystemComponentsCalculator.get_multiplatform_processor()
    CORES: str = psutil.cpu_count(logical=False)
    THREADS: str = psutil.cpu_count(logical=True)
    FREQUENCY: str = psutil.cpu_freq().current if psutil.cpu_freq() else "N/A"
    MEMORY: str = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    RESOLUTION: str = SystemComponentsCalculator.get_screen_resolution()
    KERNEL_VERSION: str = SystemComponentsCalculator.get_kernel_version()
    V4L2_VERSION: str = SystemComponentsCalculator.get_v4l2_ctl_util()
    PERMS: str = SystemComponentsCalculator.get_perms()
    TKINTER: str = SystemComponentsCalculator.get_tkinter_lib()

    BASE_CURRENT_INFO: List[str] = [OS_TYPE, OS_VERSION, PROCESSOR, CORES, THREADS, FREQUENCY, MEMORY, RESOLUTION,
                                    KERNEL_VERSION, V4L2_VERSION, PERMS, TKINTER]