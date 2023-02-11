import importlib
import os
import logging
import logging.config
from decouple import config
from log.default_logger import LoggerDefault
from service import Singleton


class DefaultConfig(metaclass=Singleton):
    DEBUG = False
    LIST_PER_PAGE = 10
    ADMIN_PASS = config("ADMIN_PASS", cast=str)
    SECRET_KEY = config("SECRET_KEY", cast=str)
    LOG_LEVEL = config('LOG_LEVEL', 'INFO')
    PROJECT_NAME = config("PROJECT_NAME", default='youshop', cast=str)
    ENV = os.environ.get("ENV", "Developer")
    TIME_ZONE = config("TIME_ZONE", default='America/Sao_Paulo', cast=str)
    SQL_DATABASE = config("SQL_DATABASE", default='postgres', cast=str)
    SQL_USER = config("SQL_USER", default='postgres', cast=str)
    SQL_PASSWORD = config("SQL_PASSWORD", default='postgres', cast=str)
    SQL_HOST = config("SQL_HOST", default='127.0.0.1', cast=str)
    SQL_PORT = config("SQL_HOST", default=5432, cast=int)

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%s'
            }
        },
        'handlers': {
            'dev_null': {
                'formatter': 'standard',
                'class': 'logging.NullHandler'
            },
            'stdout_logger': {
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'level': 'INFO',
            },
        },
        'loggers': {
            '': {
                'level': LOG_LEVEL,
                'handlers': ['stdout_logger'],
                'propagate': False,
            },
        },

    }


class DeveloperConfig(DefaultConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG

    def __init__(self):
        logging.config.dictConfig(self.LOGGING)
        logging.setLoggerClass(LoggerDefault)


def get_config():
    """ Create Configs object to load in application"""
    config_var = os.getenv('ENV', 'Developer')
    environments = "{}Config".format(config_var)
    config_app = getattr(importlib.import_module("setup.config"), environments)
    return config_app()
