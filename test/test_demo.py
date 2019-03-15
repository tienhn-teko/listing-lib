# coding=utf-8
import logging

from listinglib.config import EsConfig
from test.conftest import PRODUCT_CATALOG_INDEX

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

def test_index(es_client):
    data_test = {
        "pv_sku": "1",
        "name": "2"
    }
    res = es_client.index(index=PRODUCT_CATALOG_INDEX, body=data_test, doc_type=EsConfig.PRODUCT_CATALOG_DOC_TYPE)
    assert res
