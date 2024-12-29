from src.domain.exceptions.track_base_exception import TrackBaseException
from src.externals.infrastructure.mongo_db.exceptions.mongo_db_exceptions_reasons_enum import \
    MongoDbExceptionsReasonsEnum


class MongoDbBaseInfrastructureException(TrackBaseException):
    _reason = MongoDbExceptionsReasonsEnum
