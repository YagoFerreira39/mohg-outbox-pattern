from abc import ABC, abstractmethod
from typing import AsyncIterator

from kafka import KafkaProducer


class IKafkaInfrastructure(ABC):
    @abstractmethod
    async def with_producer(self) -> AsyncIterator[KafkaProducer]:
        pass
