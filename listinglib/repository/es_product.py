# coding=utf-8
import logging

from listinglib.esconfig import EsConfig
from listinglib.repository import EsRepositoryInterface

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductRepository(EsRepositoryInterface):
    def __init__(self, mode=None):
        super().__init__(mode)
        self._index = EsConfig.get_es_config(mode).PRODUCT_INDEX
        self.doc_type = EsConfig.get_es_config(mode).PRODUCT_DOC_TYPE
