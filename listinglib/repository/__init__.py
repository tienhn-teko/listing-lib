# coding=utf-8
import logging

from elastictools.doctools import DocTools

from listinglib.config import EsConfig

from listinglib.es_models import es_product

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsRepositoryInterface(object):
    def __init__(self, elastic_url=None):
        self._es = DocTools.from_url(elastic_url or EsConfig.ELASTIC_URL)
        self._index = None

    @property
    def is_existed(self):
        """
        Check if index has existed on elasticsearch
        If not, raise an error
        :return:
        """
        if not self._es.indextool().exists(self._index):
            raise ValueError('Index %s does not exist.' % self._index)
        return True

    def create_if_not_exists(self):
        self._es.indextool().create_if_not_exists(
            index_name=self._index,
            mapping=es_product.mapping,
            settings=es_product.settings)

    def ingest_products(self, data):
        """
        Ingest a list of products into index
        :param list data:
        """
        products = self._valid_products(data)
        self._ingest_data(data=products)

    def _ingest_data(self, data):
        """
        Ingest data into index, if index does not exist, raise an error
        :param list data:
        """
        assert self.is_existed
        self._es.indextool().refresh(self._index)
        self._es.bulk(index_name=self._index, actions=data)

    @staticmethod
    def _valid_products(products):
        products = [
            {'_id': product['sku'], 'doc': product}
            for product in products if 'sku' in product
        ]
        return products
