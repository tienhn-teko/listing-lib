# coding=utf-8
import logging

from listinglib.config import EsConfig
from listinglib.repository import EsRepositoryInterface

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductRepository(EsRepositoryInterface):
    def __init__(self, es_product = None):
        super().__init__()
        self._index = es_product or EsConfig.PRODUCT_CATALOG_INDEX


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