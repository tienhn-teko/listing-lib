# coding=utf-8
import logging

from listinglib import listing_lib_logger
from listinglib.logic.es_product import EsProductLogic
from listinglib.repository.es_product import EsProductRepository

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductService:
    @staticmethod
    def save(product, mode=None):
        """
        Index product đơn lẻ vào elastic search
        :param product: json
        :param mode: Es mode
        :return:
        """
        listing_lib_logger.info("Save: %s" % product)
        parsed_product = EsProductLogic.to_es_data(product)
        es = EsProductRepository(mode=mode)
        return es.save(parsed_product)

    @staticmethod
    def save_all(products, mode=None):
        """
        Bulk index list product to elastic search
        :param products: Array<json>
        :param mode: Es mode
        :return:
        """
        listing_lib_logger.info("Save all: %s" % products)
        parsed_products = list(map(EsProductLogic.to_es_data, products))
        es = EsProductRepository(mode)
        return es.save_all(parsed_products)
