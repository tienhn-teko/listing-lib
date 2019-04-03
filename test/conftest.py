# coding=utf-8
import logging

import pytest
from elasticsearch import Elasticsearch

from listinglib.es_models.es_product import mapping, settings
from listinglib.logic.es_product import EsProductLogic

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

PRODUCT_INDEX = "product_catalog_to_pytest"
PRODUCT_CATALOG_URL = "http://localhost:9200"


@pytest.fixture(scope="session")
def es_client(request):
    """
    :return: es_product
    """
    es = Elasticsearch(PRODUCT_CATALOG_URL)
    es.indices.create(PRODUCT_INDEX, body={
        "settings": settings,
        "mappings": mapping
    })

    def teardown():
        es.indices.delete(index=PRODUCT_INDEX)

    request.addfinalizer(teardown)
    return es


@pytest.fixture
def product_test_data():
    data = {
        "_RAW" : [
            {"name": "Chuột Logitech G102", "pv_sku": "123456"},
            {"name": "Chuột Fuhlen", "pv_sku": "654321"}
        ]
    }
    data["_PARSED"] = [EsProductLogic.to_es_data(p) for p in data['_RAW']]
    return data
