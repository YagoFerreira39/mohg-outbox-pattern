from src.use_cases.data_types import base_model_omit_none
from src.use_cases.data_types.responses.base.base_api_response import BaseApiResponse
from src.use_cases.data_types.responses.payload.register_rental_payload import (
    RegisterRentalPayload,
)


@base_model_omit_none
class RegisterRentalResponse(BaseApiResponse):
    payload: RegisterRentalPayload = None
