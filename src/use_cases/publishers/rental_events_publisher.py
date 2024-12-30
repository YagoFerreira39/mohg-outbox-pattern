import loglifos

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from witch_doctor import WitchDoctor

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.models.rental_event_message_model import RentalEventMessageModel
from src.domain.models.rental_event_model import RentalEventModel
from src.use_cases.exceptions.use_case_exceptions import (
    UnableToSendEventToQueueException,
    UnexpectedUseCaseException,
)
from src.use_cases.ports.extensions.i_rental_extension import IRentalExtension
from src.use_cases.ports.publishers.i_rental_events_publisher import (
    IRentalEventsPublisher,
)
from src.use_cases.ports.repositories.kafka.i_kafka_rental_events_repository import (
    IKafkaRentalEventsRepository,
)
from src.use_cases.ports.repositories.mongo_db.i_rental_repository import (
    IRentalRepository,
)


class RentalEventsPublisher(IRentalEventsPublisher):
    __rental_extension: IRentalExtension
    __rental_repository: IRentalRepository
    __kafka_rental_events_repository: IKafkaRentalEventsRepository

    @WitchDoctor.injection
    def __init__(
        self,
        rental_extension: IRentalExtension,
        rental_repository: IRentalRepository,
        kafka_rental_events_repository: IKafkaRentalEventsRepository,
    ):
        RentalEventsPublisher.__rental_extension = rental_extension
        RentalEventsPublisher.__rental_repository = rental_repository
        RentalEventsPublisher.__kafka_rental_events_repository = (
            kafka_rental_events_repository
        )

    @classmethod
    async def publish_register_rental_events(cls) -> None:
        try:
            rental_events_with_pending_status = await cls.__get_rental_events_by_status(
                status="pending"
            )

            rental_event_message_model_list = (
                cls.__create_rental_event_message_model_list(
                    rental_event_model_list=rental_events_with_pending_status
                )
            )

            await cls.__send_events_to_queue(
                rental_event_message_model_list=rental_event_message_model_list
            )

        except UseCaseBaseException as original_exception:
            raise original_exception

        except Exception as original_exception:
            raise UnexpectedUseCaseException(
                message="An unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __get_rental_events_by_status(cls, status: str) -> list[RentalEventModel]:
        try:
            model_list = await cls.__rental_repository.get_rental_events_by_status(
                status=status
            )

            return model_list

        except RepositoryBaseException as original_exception:
            loglifos.error(msg=f"Unable to process rental events.")

            raise UnableToSendEventToQueueException(
                message="Rental event created, but unable to send it to queue.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    def __create_rental_event_message_model_list(
        cls, rental_event_model_list: list[RentalEventModel]
    ) -> list[RentalEventMessageModel]:
        try:
            rental_event_message_model_list = [
                cls.__rental_extension.create_rental_event_message_model(
                    rental_event_model=rental_event_model
                )
                for rental_event_model in rental_event_model_list
            ]

            return rental_event_message_model_list

        except ExtensionBaseException as original_exception:
            loglifos.error(msg=f"Unable to process rental events.")

            raise UnableToSendEventToQueueException(
                message="Rental event created, but unable to send it to queue.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __send_events_to_queue(
        cls, rental_event_message_model_list: list[RentalEventMessageModel]
    ) -> None:
        try:
            for rental_event_message_model in rental_event_message_model_list:
                await cls.__kafka_rental_events_repository.send_rental_event_message_to_topic(
                    rental_event_message_model=rental_event_message_model
                )

                loglifos.debug(
                    msg=f"Rental event [{rental_event_message_model.id_}] with rental_id [{rental_event_message_model.rental_id}] sent to queue."
                )

        except RepositoryBaseException as original_exception:
            raise UnableToSendEventToQueueException(
                message="Rental event created, but unable to send it to queue.",
                original_error=original_exception,
            ) from original_exception
