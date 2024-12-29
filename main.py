from pyfiglet import print_figlet
import uvicorn
from decouple import config
from fastapi import FastAPI
from src.externals.infrastructure.logs_config.loglifos_config_infrastructure import (
    LoglifosConfigInfrastructure,
)

from src.externals.infrastructure.ioc_container.mohg_ioc_container_config_infrastructure import (
    MohgIocContainerConfigInfrastructure,
)

from src.externals.infrastructure.api_config.api_config_infrastructure import (
    ApiConfigInfrastructure,
)
from src.externals.infrastructure.http_config.http_server_config_infrastructure import (
    HttpServerConfigInfrastructure,
)


def config_app() -> FastAPI:
    ioc_container_config_infrastructure = MohgIocContainerConfigInfrastructure()
    ioc_container_config_infrastructure.init_resources()
    ioc_container_config_infrastructure.wire(
        modules=["src.externals.routers.rental_router"]
    )

    http_server_config_infrastructure = HttpServerConfigInfrastructure()
    logs_config_infrastructure = LoglifosConfigInfrastructure()

    api_server_config_infrastructure = ApiConfigInfrastructure(
        http_server_config_infrastructure=http_server_config_infrastructure,
        logs_config_infrastructure=logs_config_infrastructure,
    )

    app = api_server_config_infrastructure.config_api()
    app.container = ioc_container_config_infrastructure

    return app


if __name__ == "__main__":
    host = config("SERVER_HOST")
    port = int(config("SERVER_PORT"))

    app = config_app()

    print(f"Server is ready at URL {host}:{port}")
    print_figlet(text="Mohg's Outbox Pattern", colors="0;85;225", width=150)

    uvicorn.run(app, host=host, port=port)
