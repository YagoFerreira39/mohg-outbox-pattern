from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.entities.rental_entity import RentalEntity
from src.domain.entities.value_objects.date_entity import DateEntity
from src.domain.entities.value_objects.id_entity import IdEntity
from src.domain.models.rental_model import RentalModel

from src.use_cases.data_types.dtos.register_rental_dto import RegisterRentalDto
from src.use_cases.data_types.requests.register_rental_request import (
    RegisterRentalRequest,
)

from src.use_cases.data_types.responses.payload.register_rental_payload import (
    RegisterRentalPayload,
)
from src.use_cases.data_types.responses.register_rental_response import (
    RegisterRentalResponse,
)
from src.use_cases.data_types.router_requests.register_rental_router_request import (
    RegisterRentalRouterRequest,
)
from src.use_cases.ports.extensions.i_register_rental_extension import (
    IRegisterRentalExtension,
)


class RegisterRentalExtension(IRegisterRentalExtension):
    @staticmethod
    def from_router_request_to_request(
        router_request: RegisterRentalRouterRequest,
    ) -> RegisterRentalRequest:
        try:
            request = RegisterRentalRequest(
                resource_id=router_request.resource_id,
                rental_period=router_request.rental_period,
            )

            return request

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_request_to_entity(request: RegisterRentalRequest) -> RentalEntity:
        try:
            resource_id = IdEntity.of(id=request.resource_id)

            entity = RentalEntity(
                resource_id=resource_id, rental_period=request.rental_period
            )

            return entity

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_entity_to_model(entity: RentalEntity) -> RentalModel:
        try:
            model = RentalModel(
                resource_id=entity.resource_id.value,
                start_date=entity.rental_period.start_date,
                end_date=entity.rental_period.end_date,
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def create_dto(registered: bool) -> RegisterRentalDto:
        try:
            dto = RegisterRentalDto(registered=registered)

            return dto

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(dto: RegisterRentalDto) -> RegisterRentalResponse:
        try:
            payload = RegisterRentalPayload(registered=dto.registered)

            response = RegisterRentalResponse(
                status=True, payload=payload, message="user registered"
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
