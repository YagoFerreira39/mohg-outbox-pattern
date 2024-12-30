from abc import ABC, abstractmethod

from src.domain.models.rental_event_message_model import RentalEventMessageModel


class IKafkaRentalEventsRepository(ABC):
    @classmethod
    @abstractmethod
    async def send_rental_event_message_to_topic(
        cls, rental_event_message_model: RentalEventMessageModel
    ) -> None:
        pass
