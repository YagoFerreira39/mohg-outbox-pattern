from abc import ABC, abstractmethod


class ILogsConfigInfrastructure(ABC):
    @classmethod
    @abstractmethod
    def config_logs(cls):
        pass
