from http import HTTPStatus
from uuid import UUID

from src.adapters.controllers.exceptions.controller_exceptions_reasons_enum import (
    ControllerExceptionsReasonsEnum,
)
from src.domain.exceptions.track_base_exception import TrackBaseException


class ControllerBaseException(TrackBaseException):
    _reason: ControllerExceptionsReasonsEnum
    _http_status_code: HTTPStatus

    def __init__(
        self,
        message: str,
        reason: ControllerExceptionsReasonsEnum = None,
        error_id: UUID = None,
        original_error: Exception = None,
        http_status_code: HTTPStatus = None,
    ):
        super().__init__(
            message=message,
            reason=reason,
            error_id=error_id,
            original_error=original_error,
        )

        if http_status_code is None:
            http_status_code = self._http_status_code

        self.http_status_code = http_status_code
