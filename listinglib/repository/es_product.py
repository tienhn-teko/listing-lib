# coding=utf-8
import logging

from listinglib.config import EsConfig
from listinglib.repository import EsRepositoryInterface

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductRepository(EsRepositoryInterface):
    def __init__(self, es_product=None, doc_type=None):
        super().__init__()
        self._index = es_product or EsConfig.PRODUCT_CATALOG_INDEX
        self.doc_type = doc_type or EsConfig.PRODUCT_CATALOG_DOC_TYPE
