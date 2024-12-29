from abc import ABC, abstractmethod

from fastapi import FastAPI


class IApiConfigInfrastructure(ABC):
    @abstractmethod
    def config_api(self) -> FastAPI:
        pass