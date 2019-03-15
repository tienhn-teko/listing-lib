# coding=utf-8
import logging

import pytest
from elasticsearch import Elasticsearch

from listinglib.es_models.es_product import mapping, settings

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

PRODUCT_CATALOG_INDEX = "product_catalog_to_pytest"
PRODUCT_CATALOG_URL = "http://localhost:9200"

@pytest.fixture
def es_client(request):
    """
    :return: es_product
    """
    es = Elasticsearch(PRODUCT_CATALOG_URL)
    es.indices.create(PRODUCT_CATALOG_INDEX, body={
        "settings": settings,
        "mappings": mapping
    })

    def teardown():
        es.indices.delete(index=PRODUCT_CATALOG_INDEX)

    request.addfinalizer(teardown)
    return es
