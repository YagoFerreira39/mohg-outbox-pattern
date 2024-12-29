from decouple import config
from kafka import KafkaProducer
from witch_doctor import WitchDoctor

from src.adapters.ports.infrastructure.kafka.i_kafka_infrastructure import (
    IKafkaInfrastructure,
)
from src.domain.models.rental_event_model import RentalEventModel
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
    async def send_rental_event_to_topic(
        cls, rental_event_model: RentalEventModel
    ) -> None:
        producer: KafkaProducer
        pass
