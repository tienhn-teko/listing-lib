# coding=utf-8
import logging

from listinglib.config import Config
from listinglib.repository import EsRepositoryInterface

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductRepository(EsRepositoryInterface):
    def __init__(self, mode=None):
        super().__init__(mode)
        self._index = Config.get_es_config(mode).PRODUCT_CATALOG_INDEX
        self.doc_type = Config.get_es_config(mode).PRODUCT_DOC_TYPE
