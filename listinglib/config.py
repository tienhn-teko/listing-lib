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
                                      'product_dev_v2')
    PRODUCT_CATALOG_DOC_TYPE = os.getenv('PRODUCT_CATALOG_DOC_TYPE',
                                      'products')
    ELASTIC_URL = os.getenv('ELASTIC_URL', 'http://localhost:9200')


class DatabaseConfig:
    TK_RESULT_DB_HOST = os.getenv('TK_RESULT_DB_HOST', '123.31.32.171')
    TK_RESULT_DB_PORT = os.getenv('TK_RESULT_DB_PORT', '3306')
    TK_RESULT_DB_USER = os.getenv('TK_RESULT_DB_USER', 'bigdata')
    TK_RESULT_DB_PASS = os.getenv('TK_RESULT_DB_PASS', 'bigdata123')
    TK_RESULT_DB_NAME = os.getenv('TK_RESULT_DB_NAME', 'tk_result')

    CATALOG_DB_HOST = os.getenv('CATALOG_DB_HOST', '123.31.32.181')
    CATALOG_DB_PORT = os.getenv('CATALOG_DB_PORT', '3306')
    CATALOG_DB_USER = os.getenv('CATALOG_DB_USER', 'congtm')
    CATALOG_DB_PASS = os.getenv('CATALOG_DB_PASS', 'DgKoL3103b')
    CATALOG_DB_NAME = os.getenv('CATALOG_DB_NAME', 'catalog-live')


ENV_MODE = Mode(os.getenv('ENV_MODE', 'dev'))
