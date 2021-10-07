from datetime import datetime
class DatetimeUtils() :

    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    
    @staticmethod
    def now() -> str:
        return datetime.now().strftime(DatetimeUtils.TIME_FORMAT)