from enum import IntEnum


class UseCaseExceptionsReasonsEnum(IntEnum):
    # UseCasesExceptionsCodes  100-199

    UNEXPECTED_EXCEPTION_ERROR = 100
    MALFORMED_REQUEST_INPUT_ERROR = 101
    UNABLE_TO_REGISTER_RENTAL_ERROR = 102
    UNABLE_TO_SEND_EVENT_TO_QUEUE_ERROR = 103
