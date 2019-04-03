# coding=utf-8
import logging

from enum import Enum

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsMode(Enum):
    LOCAL = 'local'
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'


class EsConfig:

    MODE = EsMode.DEV
    PRODUCT_INDEX = 'product_dev_v2'
    PRODUCT_DOC_TYPE = 'products'

    @staticmethod
    def set_mode(mode):
        EsConfig.MODE = mode


    @staticmethod
    def get_es_config(mode=None):
        _mode = mode if mode else EsConfig.MODE
        if _mode == EsMode.LOCAL:
            return LocalEsConfig
        elif _mode == EsMode.DEV:
            return DevelopmentEsConfig
        elif _mode == EsMode.TEST:
            return TestEsConfig
        elif _mode == EsMode.PROD:
            return ProductionEsConfig
        else:
            raise Exception("Invalid mode for listing lib")


class LocalEsConfig(EsConfig):
    ELASTIC_URL = 'http://localhost:9200'


class DevelopmentEsConfig(EsConfig):
    ELASTIC_URL = 'http://123.31.32.226:9200'


class TestEsConfig(EsConfig):
    ELASTIC_URL = 'http://localhost:9200'

class ProductionEsConfig(EsConfig):
    ELASTIC_URL = 'http://123.31.32.226:9200'

