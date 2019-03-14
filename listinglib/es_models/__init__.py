# coding=utf-8
import logging

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsData:
    def __init__(self, _id, info):
        self.id = _id
        self.info = info
