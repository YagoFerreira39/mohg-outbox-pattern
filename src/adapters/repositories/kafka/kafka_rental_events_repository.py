import json

from decouple import config
from kafka import KafkaProducer
from witch_doctor import WitchDoctor

from src.adapters.ports.infrastructure.kafka.i_kafka_infrastructure import (
    IKafkaInfrastructure,
)
from src.adapters.repositories.exceptions.repository_exceptions import (
    FailToInsertException,
    RepositoryUnexpectedException,
)
from src.domain.models.rental_event_message_model import RentalEventMessageModel
from src.externals.infrastructure.kafka.exceptions.kafka_infrastructure_base_exception import (
    KafkaInfrastructureBaseException,
)
from src.use_cases.ports.repositories.kafka.i_kafka_rental_events_repository import (
    IKafkaRentalEventsRepository,
)


class KafkaRentalEventsRepository(IKafkaRentalEventsRepository):
    __kafka_infrastructure: IKafkaInfrastructure
    __user_subscriptions_command_topic = config("KAFKA_RENTAL_TOPIC")

    @WitchDoctor.injection
    def __init__(
        self,
        kafka_infrastructure: IKafkaInfrastructure,
    ):
        KafkaRentalEventsRepository.__kafka_infrastructure = kafka_infrastructure

    @classmethod
    async def send_rental_event_message_to_topic(
        cls, rental_event_message_model: RentalEventMessageModel
    ) -> None:
        await cls.__send_rental_event_to_topic(
            rental_event_message_model=rental_event_message_model
        )

    @classmethod
    async def __send_rental_event_to_topic(
        cls, rental_event_message_model: RentalEventMessageModel
    ):
        producer: KafkaProducer

        try:
            model_to_send = rental_event_message_model.to_send()

            encoded_key = model_to_send.get("id_").encode()
            encoded_value = json.dumps(model_to_send).encode()

            async with cls.__kafka_infrastructure.with_producer() as producer:
                producer.send(
                    topic=rental_event_message_model.topic,
                    key=encoded_key,
                    value=encoded_value,
                )
                producer.flush()

        except KafkaInfrastructureBaseException as original_exception:
            raise FailToInsertException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception

        except Exception as original_exception:
            raise RepositoryUnexpectedException(
                message="Unexpected repository exception",
                original_error=original_exception,
            ) from original_exception
