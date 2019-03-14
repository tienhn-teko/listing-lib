# coding=utf-8
import logging
import os
from enum import Enum

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class Mode(Enum):
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'


class EsConfig:
    PRODUCT_CATALOG_INDEX = os.getenv('PRODUCT_CATALOG_INDEX',
                                      'product_lib_dev')
    PRODUCT_CATALOG_DOC_TYPE = os.getenv('PRODUCT_CATALOG_DOC_TYPE',
                                      'product')
    ELASTIC_URL = os.getenv('ELASTIC_URL', 'http://localhost:9200')


ENV_MODE = Mode(os.getenv('ENV_MODE', 'dev'))
