from decouple import config
from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection
from pymongo.results import InsertOneResult
from witch_doctor import WitchDoctor

from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)
from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbInfrastructure,
)
from src.adapters.repositories.exceptions.repository_exceptions import (
    FailToInsertException,
    FailToRetrieveInformationException,
)
from src.domain.models.rental_event_model import RentalEventModel
from src.domain.models.rental_model import RentalModel
from src.externals.infrastructure.mongo_db.exceptions.mongo_db_base_infrastructure_exception import (
    MongoDbBaseInfrastructureException,
)
from src.use_cases.ports.extensions.i_rental_extension import IRentalExtension
from src.use_cases.ports.repositories.mongo_db.i_rental_repository import (
    IRentalRepository,
)


class RentalRepository(IRentalRepository):
    __mongo_db_infrastructure: IMongoDbInfrastructure
    __rental_collection: IMongoDbCollection
    __rental_event_collection: IMongoDbCollection
    __rental_extension: IRentalExtension

    @WitchDoctor.injection
    def __init__(
        self,
        mongo_db_infrastructure: IMongoDbInfrastructure,
        rental_extension: IRentalExtension,
    ):
        RentalRepository.__mongo_db_infrastructure = mongo_db_infrastructure
        RentalRepository.__rental_collection = (
            RentalRepository.__mongo_db_infrastructure.require_collection(
                database=config("MOHG_OUTBOX_DATABASE"),
                collection=config("RENTAL_COLLECTION"),
            )
        )
        RentalRepository.__rental_event_collection = (
            RentalRepository.__mongo_db_infrastructure.require_collection(
                database=config("MOHG_OUTBOX_DATABASE"),
                collection=config("RENTAL_EVENTS_COLLECTION"),
            )
        )
        RentalRepository.__rental_extension = rental_extension

    @classmethod
    async def register_rental(cls, model: RentalModel) -> RentalModel:
        session: AsyncIOMotorClientSession = (
            await cls.__mongo_db_infrastructure.get_client().start_session()
        )

        try:
            async with session.start_transaction():
                async with cls.__rental_collection.with_collection() as rental_collection:
                    inserted_result: InsertOneResult = (
                        await rental_collection.insert_one(model.to_insert())
                    )
                    inserted_model = model
                    inserted_model.rental_id = inserted_result.inserted_id

                async with cls.__rental_event_collection.with_collection() as rental_event_collection:
                    event_model = cls.__rental_extension.create_rental_event_model(
                        model=inserted_model
                    )

                    await rental_event_collection.insert_one(event_model.to_insert())

            return inserted_model

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToInsertException(
                message="Failed to register rental in database.",
                original_error=original_exception,
            ) from original_exception

        finally:
            await session.end_session()

    @classmethod
    async def get_rental_events_by_status(cls, status: str) -> list[RentalEventModel]:
        try:
            async with cls.__rental_event_collection.with_collection() as rental_event_collection:
                collection: AsyncIOMotorCollection

                query = {"status": status}

                pending_events = (
                    await rental_event_collection.find(query)
                    .limit(10)
                    .to_list(length=None)
                )

                rental_event_model_list = (
                    cls.__rental_extension.from_database_result_to_event_model_list(
                        result_list=pending_events
                    )
                )

                return rental_event_model_list

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToRetrieveInformationException(
                message="Failed to retrieve rental events in database.",
                original_error=original_exception,
            ) from original_exception
