from datetime import datetime

class DateChecker:
    @staticmethod
    def is_valid_date(date_str: str, fmt: str = "%Y-%m-%d") -> bool:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except (ValueError, TypeError):
            return False