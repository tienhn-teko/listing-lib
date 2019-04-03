# coding=utf-8
import logging

from listinglib.logic.es_product import EsProductLogic
from listinglib.repository.es_product import EsProductRepository

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
        parsed_product = EsProductLogic.to_es_data(product)
        es = EsProductRepository()
        return es.save(parsed_product)

    @staticmethod
    def save_all(products):
        """
        Bulk index list product to elastic search
        :param products: Array<json>
        :return:
        """
        parsed_products = list(map(EsProductLogic.to_es_data,products))
        es = EsProductRepository()
        return es.save_all(parsed_products)
