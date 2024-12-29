from abc import ABC, abstractmethod

from src.domain.models.rental_model import RentalModel


class IRentalRepository(ABC):
    pass

    @classmethod
    @abstractmethod
    async def register_rental(cls, model: RentalModel) -> RentalModel:
        pass
