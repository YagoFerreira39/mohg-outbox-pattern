from src.externals.infrastructure.mongo_db.exceptions.mongo_db_base_infrastructure_exception import \
    MongoDbBaseInfrastructureException
from src.externals.infrastructure.mongo_db.exceptions.mongo_db_exceptions_reasons_enum import \
    MongoDbExceptionsReasonsEnum


class MongoDbInfrastructureUnableToConnectError(MongoDbBaseInfrastructureException):
    _reason = MongoDbExceptionsReasonsEnum.UNABLE_TO_CONNECT_ERROR


class MongoDbInfrastructureUnexpectedError(MongoDbBaseInfrastructureException):
    _reason = MongoDbExceptionsReasonsEnum.UNEXPECTED_ERROR


class MongoDbInfrastructureConnectionBrokenError(MongoDbBaseInfrastructureException):
    _reason = MongoDbExceptionsReasonsEnum.UNABLE_TO_COMMUNICATE_ERROR


class MongoDbInfrastructureWriteError(MongoDbBaseInfrastructureException):
    _reason = MongoDbExceptionsReasonsEnum.WRITE_ERROR


class MongoDbInfrastructureReadError(MongoDbBaseInfrastructureException):
    _reason = MongoDbExceptionsReasonsEnum.READ_ERROR
