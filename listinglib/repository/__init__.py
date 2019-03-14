# coding=utf-8
import logging

from elastictools.doctools import DocTools

from listinglib.config import EsConfig


__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsRepositoryInterface(object):
    def __init__(self, elastic_url=None):
        self._es = DocTools.from_url(elastic_url or EsConfig.ELASTIC_URL)
        self._index = None

    def save(self, data):
        # TODO
        pass

    def save_all(self, data_list):
        # TODO
        pass
