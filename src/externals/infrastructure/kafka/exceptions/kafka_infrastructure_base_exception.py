from src.domain.exceptions.track_base_exception import TrackBaseException
from src.externals.infrastructures.kafka.exceptions.kafka_infrastructure_exceptions_reasons_enum import (
    KafkaInfrastructureExceptionsReasonsEnum,
)


class KafkaInfrastructureBaseException(TrackBaseException):
    _reason = KafkaInfrastructureExceptionsReasonsEnum
