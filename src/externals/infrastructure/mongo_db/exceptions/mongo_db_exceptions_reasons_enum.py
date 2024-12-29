from enum import IntEnum


class MongoDbExceptionsReasonsEnum(IntEnum):
    # MongoDbInfraExceptionCodes 0-99

    UNEXPECTED_ERROR = 0
    UNABLE_TO_CONNECT_ERROR = 1
    WRITE_ERROR = 2
    READ_ERROR = 3
    UNABLE_TO_COMMUNICATE_ERROR = 4
