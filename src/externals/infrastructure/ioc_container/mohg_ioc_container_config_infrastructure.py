from dependency_injector import providers, containers

from src.adapters.controllers.rental_controller import RentalController
from src.adapters.extensions.register_rental_extension import RegisterRentalExtension
from src.adapters.extensions.rental_extension import RentalExtension
from src.adapters.repositories.kafka.kafka_rental_events_repository import (
    KafkaRentalEventsRepository,
)
from src.adapters.repositories.mongo_db.rental_repository import RentalRepository
from src.externals.infrastructure.kafka.kafka_infrastructure import KafkaInfrastructure
from src.externals.infrastructure.mongo_db.mongo_db_infrastructure import (
    MongoDbInfrastructure,
)
from src.use_cases.publishers.rental_events_publisher import RentalEventsPublisher
from src.use_cases.rental.register_rental_use_case import RegisterRentalUseCase


class MohgIocContainerConfigInfrastructure(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Infrastructures
    kafka_infrastructure = providers.Singleton(KafkaInfrastructure)
    mongo_db_infrastructure = providers.Singleton(MongoDbInfrastructure)

    # Extensions
    rental_extension = providers.Singleton(RentalExtension)
    register_rental_extension = providers.Singleton(RegisterRentalExtension)

    # Repositories
    rental_repository = providers.Singleton(
        RentalRepository,
        mongo_db_infrastructure=mongo_db_infrastructure,
        rental_extension=rental_extension,
    )
    kafka_rental_events_repository = providers.Singleton(
        KafkaRentalEventsRepository, kafka_infrastructure=kafka_infrastructure
    )

    # Use Cases
    register_rental_use_case = providers.Singleton(
        RegisterRentalUseCase,
        rental_extension=rental_extension,
        register_rental_extension=register_rental_extension,
    )
    rental_events_publisher = providers.Singleton(
        RentalEventsPublisher,
        rental_extension=rental_extension,
        rental_repository=rental_repository,
        kafka_rental_events_repository=kafka_rental_events_repository,
    )

    # Controllers
    rental_controller = providers.Singleton(
        RentalController,
        register_rental_use_case=register_rental_use_case,
        register_rental_extension=register_rental_extension,
    )
