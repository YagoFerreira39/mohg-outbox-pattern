from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.register_rental_dto import RegisterRentalDto
from src.use_cases.data_types.requests.register_rental_request import (
    RegisterRentalRequest,
)


class IRegisterRentalUseCase(ABC):
    @classmethod
    @abstractmethod
    async def register_rental(cls, request: RegisterRentalRequest) -> RegisterRentalDto:
        pass
