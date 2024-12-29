from abc import ABC, abstractmethod

from src.domain.entities.rental_entity import RentalEntity
from src.domain.models.rental_model import RentalModel
from src.use_cases.data_types.dtos.register_rental_dto import RegisterRentalDto
from src.use_cases.data_types.requests.register_rental_request import (
    RegisterRentalRequest,
)
from src.use_cases.data_types.responses.register_rental_response import (
    RegisterRentalResponse,
)
from src.use_cases.data_types.router_requests.register_rental_router_request import (
    RegisterRentalRouterRequest,
)


class IRegisterRentalExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_router_request_to_request(
        router_request: RegisterRentalRouterRequest,
    ) -> RegisterRentalRequest:
        pass

    @staticmethod
    @abstractmethod
    def from_request_to_entity(request: RegisterRentalRequest) -> RentalEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_to_model(entity: RentalEntity) -> RentalModel:
        pass

    @staticmethod
    @abstractmethod
    def create_dto(registered: bool) -> RegisterRentalDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(dto: RegisterRentalDto) -> RegisterRentalResponse:
        pass
