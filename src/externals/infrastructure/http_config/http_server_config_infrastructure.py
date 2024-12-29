from decouple import config
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.externals.ports.infrastructures.http_config.i_http_server_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.routers.rental_router import RentalRouter


class HttpServerConfigInfrastructure(IHttpServerConfigInfrastructure):
    def __init__(self):
        self.__root_path = config("ROOT_PATH")
        self.__app = FastAPI(
            title="Mohg Outbox Pattern",
            description="",
            docs_url=self.__root_path + "/docs",
            openapi_url=self.__root_path + "/openapi.json",
        )

    def __register_cors_rules(self) -> None:
        cors_allowed_origins_str = config("CORS_ALLOWED_ORIGINS")
        cors_allowed_origins = cors_allowed_origins_str.split(",")
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __register_routers(self) -> None:
        router = RentalRouter.get_router()
        self.__app.include_router(router, prefix=self.__root_path)

    def config_http_server(self) -> FastAPI:
        self.__register_cors_rules()
        self.__register_routers()

        return self.__app
