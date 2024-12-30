from src.adapters.controllers import controller_error_handler
from src.use_cases.data_types.responses.register_rental_response import (
    RegisterRentalResponse,
)
from src.use_cases.data_types.router_requests.register_rental_router_request import (
    RegisterRentalRouterRequest,
)
from src.use_cases.ports.extensions.i_register_rental_extension import (
    IRegisterRentalExtension,
)
from src.use_cases.ports.use_cases.rental.i_register_rental_use_case import (
    IRegisterRentalUseCase,
)


class RentalController:
    def __init__(
        self,
        register_rental_use_case: IRegisterRentalUseCase,
        register_rental_extension: IRegisterRentalExtension,
    ):
        self.__register_rental_use_case = register_rental_use_case
        self.__register_rental_extension = register_rental_extension

    @controller_error_handler
    async def register_rental(
        self,
        router_request: RegisterRentalRouterRequest,
    ) -> RegisterRentalResponse:
        request = self.__register_rental_extension.from_router_request_to_request(
            router_request=router_request
        )

        dto = await self.__register_rental_use_case.register_rental(request=request)

        response = self.__register_rental_extension.from_dto_to_response(dto=dto)

        return response

    @classmethod
    @controller_error_handler
    async def log_message(cls, msg: str) -> None:
        print(msg)
