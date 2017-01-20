from tornado import locale

from config import rpc
from config.settings import TRANSLATIONS_PATH
from connectors.LoggerConnector import LoggerConnector
from pools.RedisPool import RedisPool


class Bootstrap:
    def __init__(self, application, options):
        self.application = application
        self.options = options

    def run(self):
        self.application.logger = LoggerConnector.get_logger('app')

        self.application.logger.info("FM Component Web Application Bootstrap run() - started")
        self.application.options = self.options
        self.application.logger.info("Tornado server File Manager app started with options %s",
                                     self.application.options.as_dict())

        # resources
        self.application.redis = RedisPool()
        self.application.logger.info("FM Component Redis - started")

        # RPC
        rpc.servers["default"]["host"] = self.options.rpc_host
        rpc.servers["default"]["port"] = self.options.rpc_port

        # Localization
        locale.load_translations(TRANSLATIONS_PATH)
