from pydantic import BaseModel

from src.use_cases.data_types import base_model_omit_none


@base_model_omit_none
class RegisterRentalPayload(BaseModel):
    registered: bool = None
