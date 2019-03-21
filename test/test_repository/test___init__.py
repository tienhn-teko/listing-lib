# coding=utf-8
import logging
import json

from listinglib.repository import EsRepositoryInterface
from listinglib.logic.es_product import EsProductLogic
from listinglib.config import EsConfig
from test.conftest import PRODUCT_CATALOG_INDEX, PRODUCT_CATALOG_URL
from test.util.es.es_product import EsProduct, ComparableProduct

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


def test_save(product_test_data, es_client):
    es_product = EsRepositoryInterface(elastic_url=PRODUCT_CATALOG_URL)
    es_product._index = PRODUCT_CATALOG_INDEX
    es_product.doc_type = EsConfig.PRODUCT_CATALOG_DOC_TYPE
    test_data = product_test_data['_PARSED'][0]
    res = es_product.save(data=test_data)
    # assertion
    test_es_product = EsProduct(es_client)
    indexed_data = test_es_product.get_products_by_id(test_data.id)
    assert ComparableProduct.compare_list_products(
        products_1=[product_test_data['_RAW'][0]],
        products_2=[indexed_data])

def test_save_all(product_test_data, es_client):
    es_product = EsRepositoryInterface(elastic_url=PRODUCT_CATALOG_URL)
    es_product._index = PRODUCT_CATALOG_INDEX
    test_data = product_test_data['_PARSED']
    res = es_product.save_all(test_data)
    # assertion
    test_es_product = EsProduct(es_client)
    indexed_data = test_es_product.get_products_by_ids([_.id for _ in test_data])
    assert ComparableProduct.compare_list_products(
        products_1=product_test_data['_RAW'],
        products_2=indexed_data)
