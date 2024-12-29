from abc import abstractmethod, ABC

from motor.motor_asyncio import AsyncIOMotorCollection


class IMongoDbCollection(ABC):
    @abstractmethod
    async def with_collection(self) -> AsyncIOMotorCollection:
        pass
