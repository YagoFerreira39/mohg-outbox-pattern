from src.externals.infrastructures.kafka.exceptions.kafka_infrastructure_base_exception import (
    KafkaInfrastructureBaseException,
)
from src.externals.infrastructures.kafka.exceptions.kafka_infrastructure_exceptions_reasons_enum import (
    KafkaInfrastructureExceptionsReasonsEnum,
)


class KafkaInfrastructureNoBrokersAvailableException(KafkaInfrastructureBaseException):
    _reason = (
        KafkaInfrastructureExceptionsReasonsEnum.KAFKA_NO_BROKERS_AVAILABLE_EXCEPTION_ERROR
    )


class KafkaInfrastructureUnexpectedException(KafkaInfrastructureBaseException):
    _reason = KafkaInfrastructureExceptionsReasonsEnum.UNEXPECTED_EXCEPTION_ERROR
