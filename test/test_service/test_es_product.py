# coding=utf-8
import logging

from listinglib.service.es_product import EsProductService

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class TestEsProductService:
    @staticmethod
    def test_save(product_test_data):
        for raw_data in product_test_data['_RAW']:
            assert EsProductService.save(raw_data)

    @staticmethod
    def test_save_all(product_test_data):
        assert EsProductService.save_all(product_test_data['_RAW'])
