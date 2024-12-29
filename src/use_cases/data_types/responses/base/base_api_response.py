from typing import TypedDict, List

from pydantic import BaseModel

from src.adapters.controllers.exceptions.controller_exceptions_reasons_enum import (
    ControllerExceptionsReasonsEnum,
)
from src.use_cases.data_types import base_model_omit_none
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


@base_model_omit_none
class BaseApiResponse(BaseModel):
    status: bool
    error_code: UseCaseExceptionsReasonsEnum | ControllerExceptionsReasonsEnum = None
    message: str = None
    payload: TypedDict | List[TypedDict] = None
