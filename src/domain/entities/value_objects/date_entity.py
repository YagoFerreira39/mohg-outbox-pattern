from datetime import datetime, timedelta
from dataclasses import dataclass

from src.domain.exceptions.entity_exceptions import MalformedDatePatternException


@dataclass(frozen=True, slots=True)
class DateEntity:
    __start_date: datetime
    __end_date: datetime

    def __post_init__(self) -> None:
        self.__validate_date_range()

    def __composite_values__(self) -> tuple[datetime, datetime]:
        return self.__start_date, self.__end_date

    @property
    def start_date(self) -> datetime:
        return self.__start_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @classmethod
    def create(cls, start_date: datetime, end_date: datetime) -> "DateEntity":
        return cls(start_date, end_date)

    @classmethod
    def one_week(cls) -> "DateEntity":
        start_date = datetime.now()
        end_date = start_date + timedelta(weeks=1)
        return cls(start_date, end_date)

    @classmethod
    def two_weeks(cls) -> "DateEntity":
        start_date = datetime.now()
        end_date = start_date + timedelta(weeks=2)
        return cls(start_date, end_date)

    @classmethod
    def one_month(cls) -> "DateEntity":
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)
        return cls(start_date, end_date)

    def is_within_range(self, date: datetime) -> bool:
        return self.__start_date <= date <= self.__end_date

    def __validate_date_range(self) -> None:
        if self.__start_date > self.__end_date:
            raise MalformedDatePatternException(
                message="end date is greater than start date"
            )
