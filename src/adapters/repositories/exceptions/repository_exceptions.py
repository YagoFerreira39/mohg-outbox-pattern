from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.exceptions.repository_exceptions_reasons_enum import (
    RepositoryExceptionsReasonsEnum,
)


class FailToRetrieveInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.FAIL_TO_RETRIEVE_INFORMATION_ERROR


class FailToInsertException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.FAIL_TO_INSERT_ERROR
