# coding=utf-8
import logging

from listinglib.service.es_product import EsProductService
from test.util.es.es_product import EsProduct, ComparableProduct

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class TestEsProductService:
    @staticmethod
    def test_save(product_test_data, es_client):
        for raw_data in product_test_data['_RAW']:
            EsProductService.save(raw_data)
        # assertion
        test_es_product = EsProduct(es_client)
        indexed_data = test_es_product.get_products_by_ids(
            ids=[raw_data['pv_sku'] for raw_data in product_test_data['_RAW']])
        assert ComparableProduct.compare_list_products(
            products_1=product_test_data['_RAW'],
            products_2=indexed_data)

    @staticmethod
    def test_save_all(product_test_data, es_client):
        EsProductService.save_all(product_test_data['_RAW'])
        # assertion
        test_es_product = EsProduct(es_client)
        indexed_data = test_es_product.get_products_by_ids(
            ids=[raw_data['pv_sku'] for raw_data in product_test_data['_RAW']])
        assert ComparableProduct.compare_list_products(
            products_1=product_test_data['_RAW'],
            products_2=indexed_data)
