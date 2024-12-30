from abc import ABC, abstractmethod

from src.domain.models.rental_event_model import RentalEventModel
from src.domain.models.rental_model import RentalModel


class IRentalRepository(ABC):
    pass

    @classmethod
    @abstractmethod
    async def register_rental(cls, model: RentalModel) -> RentalModel:
        pass

    @classmethod
    @abstractmethod
    async def get_rental_events_by_status(cls, status: str) -> list[RentalEventModel]:
        pass
