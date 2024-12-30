import asyncio
from http import HTTPStatus

import loglifos
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from src.externals.infrastructure.ioc_container.mohg_ioc_container_config_infrastructure import (
    MohgIocContainerConfigInfrastructure,
)
from starlette.routing import Router

from src.adapters.controllers.rental_controller import RentalController
from src.use_cases.data_types.responses.register_rental_response import (
    RegisterRentalResponse,
)
from src.use_cases.data_types.router_requests.register_rental_router_request import (
    RegisterRentalRouterRequest,
)
from src.use_cases.publishers.rental_events_publisher import RentalEventsPublisher


class RentalRouter(Router):
    __rental_router = APIRouter()

    @staticmethod
    def get_router() -> APIRouter:
        return RentalRouter.__rental_router

    @staticmethod
    @__rental_router.post(
        path="/rental",
        tags=["Rental"],
        response_model_exclude_none=True,
        response_model=RegisterRentalResponse,
        status_code=HTTPStatus.OK,
    )
    @inject
    async def register_rental(
        router_request: RegisterRentalRouterRequest,
        controller: RentalController = Depends(
            Provide[MohgIocContainerConfigInfrastructure.rental_controller]
        ),
    ) -> RegisterRentalResponse:
        response = await controller.register_rental(router_request=router_request)
        return response

    @staticmethod
    @__rental_router.on_event("startup")
    @inject
    async def startup_event(
        rental_events_publisher: RentalEventsPublisher = Depends(
            Provide[MohgIocContainerConfigInfrastructure.rental_events_publisher]
        ),
    ) -> None:
        try:
            await rental_events_publisher.publish_register_rental_events()
        except Exception as exception:
            loglifos.error(msg=f"Failed to publish rental events: {exception}")
