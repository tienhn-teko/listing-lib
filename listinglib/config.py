# coding=utf-8
import logging

from enum import Enum

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class Mode(Enum):
    LOCAL = 'local'
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'


class Config:

    MODE = Mode.DEV
    PRODUCT_INDEX = 'product_dev_v2'
    PRODUCT_DOC_TYPE = 'products'

    @staticmethod
    def set_mode(mode):
        Config.MODE = mode


    @staticmethod
    def get_es_config(mode=None):
        _mode = mode if mode else Config.MODE
        if _mode == Mode.LOCAL:
            return LocalConfig
        elif _mode == Mode.DEV:
            return DevelopmentConfig
        elif _mode == Mode.TEST:
            return TestConfig
        elif _mode == Mode.PROD:
            return ProductionConfig
        else:
            raise Exception("Invalid mode for listing lib")


class LocalConfig(Config):
    ELASTIC_URL = 'http://localhost:9200'


class DevelopmentConfig(Config):
    ELASTIC_URL = 'http://123.31.32.226:9200'


class TestConfig(Config):
    ELASTIC_URL = 'http://localhost:9200'

class ProductionConfig(Config):
    ELASTIC_URL = 'http://123.31.32.226:9200'

