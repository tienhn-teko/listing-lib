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

    def update_products(self, data):
        """
        Ingest a list of products into index
        :param list data:
        """
        products = self._valid_products(data)
        self._update_existed_data(actions=products)

    def _update_existed_data(self, actions, chunk_size=1000):
        """
        Execute actions on documents of existed index
        :param list data:
        """
        assert self.is_existed
        result = self._es.bulk(index_name=self._index, actions=actions,
                               chunk_size=chunk_size)
        self._es.indextool().refresh(self._index)
        return result

    @staticmethod
    def _valid_products(products):
        products = [
            {
                '_op_type': 'update',
                '_id': product['sku'],
                'doc': product,
                'doc_as_upsert': False
            }
            for product in products if 'sku' in product
        ]
        print('DEBUG', products[0])
        return products
