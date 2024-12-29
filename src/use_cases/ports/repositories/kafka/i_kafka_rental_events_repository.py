from abc import ABC, abstractmethod

from src.domain.models.rental_event_model import RentalEventModel


class IKafkaRentalEventsRepository(ABC):
    @classmethod
    @abstractmethod
    async def send_rental_event_to_topic(
        cls, rental_event_model: RentalEventModel
    ) -> None:
        pass
