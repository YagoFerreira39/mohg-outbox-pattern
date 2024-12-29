from enum import IntEnum
from uuid import UUID, uuid4


class TrackBaseException(Exception):
    _reason: IntEnum

    def __init__(
        self,
        message: str,
        reason: IntEnum = None,
        error_id: UUID = None,
        original_error: Exception = None,
    ):
        super().__init__(message)
        if error_id is None:
            error_id = uuid4()

        if reason is None:
            reason = self._reason

        self.error_id = error_id
        self.reason = reason

        self.message = message
        self.original_error = original_error
