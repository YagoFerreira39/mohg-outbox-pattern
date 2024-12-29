from abc import abstractmethod, ABC

from motor.motor_asyncio import AsyncIOMotorClient

from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)


class IMongoDbInfrastructure(ABC):
    @abstractmethod
    def require_collection(self, database: str, collection: str) -> IMongoDbCollection:
        pass

    @abstractmethod
    def get_client(self) -> AsyncIOMotorClient:
        pass
