# coding=utf-8
import logging

from test.conftest import PRODUCT_INDEX

__author__ = 'TungLQ'
_logger = logging.getLogger(__name__)


class EsProduct:
    def __init__(self, es):
        self._es = es

    def get_products_by_id(self, id):
        return self._es.get_source(
            index=PRODUCT_INDEX,
            doc_type='_all',
            id=id)

    def get_products_by_ids(self, ids):
        resp = self._es.mget(
            index=PRODUCT_INDEX,
            doc_type='_all',
            body={'ids': ids})
        filtered_data = [doc['_source'] for doc in resp['docs'] if doc['found']]
        return filtered_data


class ComparableProduct:
    es_product_schema = ['name', 'pv_sku']

    def __init__(self, product):
        for key, value in product.items():
            setattr(self, key, value)

    def __eq__(self, other):
        for key in ComparableProduct.es_product_schema:
            if self.__getattribute__(key) != other.__getattribute__(key):
                return False
        return True

    def __repr__(self):
        return "%s" % self.__dict__.items()

    @classmethod
    def compare_list_products(self, products_1, products_2):
        products_1 = [ComparableProduct(_) for _ in products_1]
        products_2 = [ComparableProduct(_) for _ in products_2]
        diff = [_ for _ in products_1 if _ not in products_2]
        if len(diff) > 0:
            raise AssertionError('Not found document: %s' % repr(diff[0]))
        return True
