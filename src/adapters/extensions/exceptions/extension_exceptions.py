from http import HTTPStatus

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from src.adapters.extensions.exceptions.extension_exceptions_reasons_enum import (
    ExtensionExceptionsReasonsEnum,
)


class ExtensionUnexpectedException(ExtensionBaseException):
    _reason = ExtensionExceptionsReasonsEnum.UNEXPECTED_EXCEPTION_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR
