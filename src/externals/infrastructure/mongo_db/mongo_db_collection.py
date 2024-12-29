from contextlib import asynccontextmanager
from typing import AsyncIterator

import loglifos
import meeseeks
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo.errors import (
    ServerSelectionTimeoutError,
    InvalidURI,
    NetworkTimeout,
    WriteError,
    BulkWriteError,
    DuplicateKeyError,
    OperationFailure,
    InvalidOperation,
)

from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_collection import IMongoDbCollection
from src.externals.infrastructure.mongo_db.exceptions.mongo_db_infrastructure_exceptions import \
    MongoDbInfrastructureConnectionBrokenError, MongoDbInfrastructureWriteError, MongoDbInfrastructureReadError, \
    MongoDbInfrastructureUnexpectedError


@meeseeks.OnlyOne(by_args_hash=True)
class MongoDbCollection(IMongoDbCollection):
    def __init__(self, client: AsyncIOMotorClient, database: str, collection: str):
        self._database = database
        self._collection = collection
        loglifos.debug(
            msg="Creating collection",
            database=self._database,
            collection=self._collection,
        )
        self._client: AsyncIOMotorClient = client

    @asynccontextmanager
    async def with_collection(self) -> AsyncIterator[AsyncIOMotorCollection]:
        try:
            database = self._client.get_database(name=self._database)
            collection = database.get_collection(name=self._collection)
            loglifos.debug(
                msg="Getting collection",
                _database=self._database,
                _collection=self._collection,
            )
            yield collection
        except (
            ServerSelectionTimeoutError,
            InvalidURI,
            NetworkTimeout,
        ) as original_error:
            loglifos.debug(msg="Cleaning AsyncIOMotorClient client")
            raise MongoDbInfrastructureConnectionBrokenError(
                message=f"Fail to connect to "
                f"database: {self._database}, "
                f"collection: {self._collection}",
                original_error=original_error,
            ) from original_error
        except (WriteError, BulkWriteError, DuplicateKeyError) as original_error:
            raise MongoDbInfrastructureWriteError(
                message="Fail to write",
                original_error=original_error,
            ) from original_error
        except (OperationFailure, InvalidOperation) as original_error:
            raise MongoDbInfrastructureReadError(
                message="Fail to read",
                original_error=original_error,
            ) from original_error
        except Exception as original_error:
            raise MongoDbInfrastructureUnexpectedError(
                message="So seed so far! see original_error",
                original_error=original_error,
            ) from original_error
