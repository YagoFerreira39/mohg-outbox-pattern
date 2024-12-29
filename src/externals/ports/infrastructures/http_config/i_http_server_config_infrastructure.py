from abc import ABC, abstractmethod

from fastapi import FastAPI


class IHttpServerConfigInfrastructure(ABC):
    @abstractmethod
    def config_http_server(self) -> FastAPI:
        pass
