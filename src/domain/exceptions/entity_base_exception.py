from src.domain.exceptions.entity_exceptions_reasons_enum import (
    EntityExceptionsReasonsEnum,
)
from src.domain.exceptions.track_base_exception import TrackBaseException


class EntityBaseException(TrackBaseException):
    _reason = EntityExceptionsReasonsEnum
