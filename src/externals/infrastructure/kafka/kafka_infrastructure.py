from contextlib import asynccontextmanager
from typing import AsyncIterator

import meeseeks
from decouple import config
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

from src.adapters.ports.infrastructure.kafka.i_kafka_infrastructure import (
    IKafkaInfrastructure,
)
from src.externals.infrastructure.kafka.exceptions.kafka_infrastructure_base_exception import (
    KafkaInfrastructureBaseException,
)
from src.externals.infrastructure.kafka.exceptions.kafka_infrastructure_exceptions import (
    KafkaInfrastructureNoBrokersAvailableException,
    KafkaInfrastructureUnexpectedException,
)


@meeseeks.OnlyOne()
class KafkaInfrastructure(IKafkaInfrastructure):
    def __init__(self):
        self._uri = config("KAFKA_URI")
        self._security_protocol = config("KAFKA_SECURITY_PROTOCOL")
        self._sasl_mechanism = config("KAFKA_SASL_MECHANISM")
        self._sasl_username = config("KAFKA_SASL_USERNAME")
        self._sasl_password = config("KAFKA_SASL_PASSWORD")
        self._client_id = config("KAFKA_CLIENT_ID")

        self._producer = None

    @property
    def producer(self) -> KafkaProducer:
        try:
            if self._producer is None:
                self._producer = KafkaProducer(
                    bootstrap_servers=self._uri,
                    security_protocol=self._security_protocol,
                    sasl_mechanism=self._sasl_mechanism,
                    sasl_plain_username=self._sasl_username,
                    sasl_plain_password=self._sasl_password,
                    client_id=self._client_id,
                )

            return self._producer

        except NoBrokersAvailable as original_exception:
            raise KafkaInfrastructureNoBrokersAvailableException(
                message="KafkaInfrastructure no brokers exception.",
                original_error=original_exception,
            ) from original_exception

        except Exception as original_exception:
            raise KafkaInfrastructureUnexpectedException(
                message="KafkaInfrastructure unexpected producer property exception.",
                original_error=original_exception,
            ) from original_exception

    @asynccontextmanager
    async def with_producer(self) -> AsyncIterator[KafkaProducer]:
        try:
            yield self.producer

        except KafkaInfrastructureBaseException as original_exception:
            raise KafkaInfrastructureUnexpectedException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception

        except Exception as original_exception:
            raise KafkaInfrastructureUnexpectedException(
                message="KafkaInfrastructure unexpected producer exception.",
                original_error=original_exception,
            ) from original_exception
