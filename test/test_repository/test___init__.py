# coding=utf-8
import logging

from listinglib.repository import EsRepositoryInterface
from listinglib.logic.es_product import EsProductLogic
from listinglib.config import EsConfig
from test.conftest import PRODUCT_CATALOG_INDEX, PRODUCT_CATALOG_URL

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

_RAW_TEST_DATA = [
    {
        "name": "Chuột Logitech G102",
        "pv_sku": "123456"
    },
    {
        "name": "Chuột Fuhlen",
        "pv_sku": "654321"
    }
]

_PARSED_TEST_DATA = [EsProductLogic.to_es_data(p) for p in _RAW_TEST_DATA]

def test_save(es_client):
    es_product = EsRepositoryInterface(elastic_url=PRODUCT_CATALOG_URL)
    es_product._index = PRODUCT_CATALOG_INDEX
    es_product.doc_type = EsConfig.PRODUCT_CATALOG_DOC_TYPE
    test_data = _PARSED_TEST_DATA[0]
    res = es_product.save(data=test_data)
    assert res

def test_save_all(es_client):
    es_product = EsRepositoryInterface(elastic_url=PRODUCT_CATALOG_URL)
    es_product._index = PRODUCT_CATALOG_INDEX
    test_data = _PARSED_TEST_DATA
    res = es_product.save_all(test_data)
    assert res
