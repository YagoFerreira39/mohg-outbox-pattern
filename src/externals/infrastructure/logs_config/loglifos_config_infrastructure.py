import loglifos
from decouple import config

from src.externals.ports.infrastructures.logs_config.i_logs_config_infrastructure import ILogsConfigInfrastructure


class LoglifosConfigInfrastructure(ILogsConfigInfrastructure):
    @classmethod
    def config_logs(cls):
        loglifos.set_config(log_level=int(config("LOG_LEVEL")))
