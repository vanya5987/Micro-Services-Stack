from screeninfo import get_monitors

class ScreenInfo:
    @staticmethod
    def _get_primary_monitor():
        return next((m for m in get_monitors() if m.x == 0 and m.y == 0), None)

    @staticmethod
    def get_screen_resolution():
        primary = ScreenInfo._get_primary_monitor()

        return primary.width, primary.height