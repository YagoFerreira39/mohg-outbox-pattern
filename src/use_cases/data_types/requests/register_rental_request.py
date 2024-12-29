from dataclasses import dataclass

from src.domain.enums.rental_period_enum import RentalPeriodEnum


@dataclass(slots=True)
class RegisterRentalRequest:
    resource_id: str
    rental_period: RentalPeriodEnum
