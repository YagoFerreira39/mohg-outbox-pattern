from enum import IntEnum


class RepositoryExceptionsReasonsEnum(IntEnum):
    # RepositoryExceptionsCodes  200-399

    FAIL_TO_RETRIEVE_INFORMATION_ERROR = 200
    FAIL_TO_INSERT_ERROR = 201
    UNEXPECTED_ERROR = 202
