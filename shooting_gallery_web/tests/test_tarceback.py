from PyQt5.QtWidgets import QApplication

import sys


class TestTraceback:
    @staticmethod
    def setup_global_exception_handling():
        import traceback
        import faulthandler
        faulthandler.enable()

        def exception_hook(exctype, value, tb):
            error_msg = "".join(traceback.format_exception(exctype, value, tb))
            print(error_msg)

        sys.excepthook = exception_hook

        global SafeApplication

        class SafeApplication(QApplication):
            def notify(self, receiver, event):
                try:
                    return super().notify(receiver, event)
                except Exception:
                    print(traceback.format_exc())
                    return False
