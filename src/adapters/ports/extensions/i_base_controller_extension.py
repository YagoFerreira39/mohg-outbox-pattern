from abc import ABC, abstractmethod

from starlette.responses import JSONResponse

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException


class IBaseControllerExtension(ABC):
    @staticmethod
    @abstractmethod
    def create_error_response(exception: UseCaseBaseException) -> JSONResponse:
        pass
