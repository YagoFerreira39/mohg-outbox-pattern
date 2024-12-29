from typing import TypeVar

import loglifos

from src.adapters.controllers.exceptions.controller_base_exception import (
    ControllerBaseException,
)
from src.adapters.extensions.base.base_controller_extension import (
    BaseControllerExtension,
)
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException

T = TypeVar("T")


def controller_error_handler(function: T) -> T:
    async def wrap(*args, **kwargs):
        try:
            return await function(*args, **kwargs)
        except UseCaseBaseException as exception:
            loglifos.error("An error occurred", exception=exception)
            response = BaseControllerExtension.create_error_response(
                exception=exception
            )
            return response
        except ControllerBaseException as exception:
            loglifos.error("An error occurred", exception=exception)
            response = BaseControllerExtension.create_error_response(
                exception=exception
            )
            return response

    wrap.__wrapped__ = function
    return wrap
