from pydantic import BaseModel, StrictStr

from src.domain.enums.rental_period_enum import RentalPeriodEnum


class RegisterRentalRouterRequest(BaseModel):
    resource_id: StrictStr
    rental_period: RentalPeriodEnum
