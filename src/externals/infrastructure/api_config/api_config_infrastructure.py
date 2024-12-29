from fastapi import FastAPI

from src.externals.ports.infrastructures.logs_config.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)
from src.externals.ports.infrastructures.api_config.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)
from src.externals.ports.infrastructures.http_config.i_http_server_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)


class ApiConfigInfrastructure(IApiConfigInfrastructure):
    def __init__(
        self,
        http_server_config_infrastructure: IHttpServerConfigInfrastructure,
        logs_config_infrastructure: ILogsConfigInfrastructure,
    ):
        self.__http_server_config_infrastructure = http_server_config_infrastructure
        self.__logs_config_infrastructure = logs_config_infrastructure

    def config_api(self) -> FastAPI:
        app = self.__http_server_config_infrastructure.config_http_server()
        self.__logs_config_infrastructure.config_logs()

        return app
