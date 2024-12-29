from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.exceptions.entity_exceptions_reasons_enum import (
    EntityExceptionsReasonsEnum,
)


class MalformedDatePatternException(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.MALFORMED_DATE_PATTERN_ERROR


class MalformedProlongPatternException(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.MALFORMED_PROLONG_PATTERN_ERROR
