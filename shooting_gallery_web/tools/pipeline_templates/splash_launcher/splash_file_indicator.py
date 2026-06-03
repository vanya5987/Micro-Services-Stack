import os
import sys

class SplashDirectoryPath:
    @staticmethod
    def get_splash_path() -> str:
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.join(os.path.dirname(__file__))