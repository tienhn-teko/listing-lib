# coding=utf-8
import logging

import pytest

from listinglib.logic.es_product import EsProductLogic

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

class TestEsProductLogic:
    @staticmethod
    def test_valid_to_es_product_data():
        raw_product = {
            "pv_sku": "18323292",
            "name": "This is my name"
        }
        data = EsProductLogic().to_es_data(raw_product)
        assert (data.id == "18323292")
        assert (data.info == {
            "pv_sku": "18323292",
            "name": "This is my name"
        })

    @staticmethod
    def test_to_es_product_data_not_found_sku():
        raw_product = {
            "name": "This is my name"
        }
        with pytest.raises(Exception):
            EsProductLogic().to_es_data(raw_product)
