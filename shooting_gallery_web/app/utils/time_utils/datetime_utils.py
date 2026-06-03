from datetime import datetime, date, timedelta

class DatetimeUtils:
    @staticmethod
    def get_shooting_time_format(current_time, start_time):
        elapsed = current_time - start_time

        total_ms = int(elapsed.total_seconds() * 1000)

        minutes = total_ms // 60000
        seconds = (total_ms % 60000) // 1000
        milliseconds = total_ms % 1000

        return f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}"

    @staticmethod
    def get_developer_shooting_time_format(current_time, start_time):
        elapsed = current_time - start_time

        total_ms = int(elapsed.total_seconds() * 1000)

        minutes = total_ms // 60000
        seconds = (total_ms % 60000) // 1000

        return f"{minutes:02d}:{seconds:02d}"

    @staticmethod
    def get_current_date() -> str:
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def get_threshold_date(days: int = 100) -> str:
        date_obj = datetime.strptime(DatetimeUtils.get_current_date(), "%Y-%m-%d")
        new_date = date_obj + timedelta(days=days)

        return new_date.strftime("%Y-%m-%d")

    @staticmethod
    def get_current_datetime() -> datetime:  # Формат вывода: 2024-01-15 14:30:45.123456.
        return datetime.now()

    @staticmethod
    def get_current_day() -> date:  # Формат вывода: 2024-01-15.
        return date.today()

    @staticmethod
    def get_current_day_for_files() -> str:  # Формат вывода: 20240115.
        return DatetimeUtils.get_current_datetime().strftime("%Y%m%d")

    @staticmethod
    def convert_str_to_date(source: str) -> date:  # Формат вывода: 2024-01-15.
        return datetime.strptime(source, "%Y%m%d").date()

    @staticmethod
    def append_days_for_data(source_date: date, day_count: int) -> date:  # Формат вывода: 2024-01-15.
        return source_date + timedelta(days=day_count)