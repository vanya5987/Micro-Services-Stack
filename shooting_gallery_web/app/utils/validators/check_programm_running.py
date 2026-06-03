from app.utils.os_system_utils.get_system_type import SystemTypeGetter
import tempfile
import os


class CheckProgramRunning:
    @staticmethod
    def app_is_running(lock_name: str):
        lockfile = os.path.join(tempfile.gettempdir(), lock_name)
        try:
            fd = os.open(lockfile, os.O_WRONLY | os.O_CREAT)
            try:
                if SystemTypeGetter.system_is_windows():
                    import msvcrt
                    msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except (IOError, OSError):
                return True
            return False
        except:
            return False
