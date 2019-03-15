# coding=utf-8
import logging

from test.conftest import PRODUCT_CATALOG_INDEX

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)




def test1(es_client):
    data_test = {
        "a": 1,
        "b": 2
    }
    res = es_client.index(index=PRODUCT_CATALOG_INDEX, body=data_test, doc_type="_doc")
    print(res)
    print("Hello")
    assert True