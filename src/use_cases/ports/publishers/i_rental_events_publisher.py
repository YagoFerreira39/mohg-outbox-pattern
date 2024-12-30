from abc import ABC, abstractmethod


class IRentalEventsPublisher(ABC):
    @classmethod
    @abstractmethod
    async def publish_register_rental_events(cls) -> None:
        pass
