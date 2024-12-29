from src.adapters.repositories.exceptions.repository_exceptions_reasons_enum import (
    RepositoryExceptionsReasonsEnum,
)
from src.domain.exceptions.track_base_exception import TrackBaseException


class RepositoryBaseException(TrackBaseException):
    _reason = RepositoryExceptionsReasonsEnum
