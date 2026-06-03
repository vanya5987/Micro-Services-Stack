import os
import sys

class RootDirectoryPath:
    @staticmethod
    def GetRootPath() -> str:
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.join(os.path.dirname(__file__))