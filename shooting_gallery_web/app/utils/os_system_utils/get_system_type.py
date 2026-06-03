import platform

class SystemTypeGetter:
    @staticmethod
    def system_is_windows():
        system = platform.system().lower()

        if system == 'windows':
            return True
        else:
            return False