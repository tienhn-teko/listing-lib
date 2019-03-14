# coding=utf-8
import logging

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductService:
    @staticmethod
    def save(product):
        """
        Index product đơn lẻ vào elastic search
        :param product: json
        :return:
        """
        pass

    @staticmethod
    def save_all(products):
        """
        Bulk index list product to elastic search
        :param products: Array<json>
        :return:
        """
        pass

