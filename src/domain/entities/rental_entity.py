from dataclasses import dataclass
from datetime import timedelta

from src.domain.entities.value_objects.date_entity import DateEntity
from src.domain.entities.value_objects.id_entity import IdEntity
from src.domain.enums.rental_period_enum import RentalPeriodEnum
from src.domain.exceptions.entity_exceptions import MalformedProlongPatternException


@dataclass
class RentalEntity:
    __rental_id: IdEntity
    __resource_id: IdEntity
    __rental_period: DateEntity

    def __init__(
        self,
        resource_id: IdEntity,
        rental_period: RentalPeriodEnum,
        rental_id: IdEntity = None,
    ):
        self.__rental_id = rental_id if rental_id else IdEntity.new_one()
        self.__resource_id = resource_id
        self.__rental_period = self.__define_rental_period(rental_period=rental_period)

    @property
    def rental_id(self) -> IdEntity:
        return self.__rental_id

    @property
    def resource_id(self) -> IdEntity:
        return self.__resource_id

    @property
    def rental_period(self) -> DateEntity:
        return self.__rental_period

    def prolong(self, days: int) -> None:
        if days > 7:
            raise MalformedProlongPatternException(
                message="prolongation period exceeded"
            )

        self.__rental_period = DateEntity(
            self.__rental_period.start_date,
            self.__rental_period.end_date + timedelta(days=days),
        )

    @staticmethod
    def __define_rental_period(rental_period: RentalPeriodEnum) -> DateEntity:
        rental_periods = {
            RentalPeriodEnum.ONE_WEEK.value: DateEntity.one_week(),
            RentalPeriodEnum.TWO_WEEKS.value: DateEntity.two_weeks(),
            RentalPeriodEnum.ONE_MONTH.value: DateEntity.one_month(),
        }

        period = rental_periods.get(rental_period.value)

        return period
