# coding=utf-8
import logging

from listinglib.esconfig import EsConfig
from test.conftest import PRODUCT_INDEX

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

def test_index(es_client):
    data_test = {
        "pv_sku": "1",
        "name": "2"
    }
    res = es_client.index(index=PRODUCT_INDEX, body=data_test, doc_type=EsConfig.PRODUCT_DOC_TYPE)
    assert res
