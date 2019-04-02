# coding=utf-8
import logging

from listinglib.config import Config
from listinglib.repository import EsRepositoryInterface
from listinglib.logic.es_product import EsProductLogic
from listinglib.logic.es_product_quantity_revenue import EsProductQuantityRevenue
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

    @staticmethod
    def save_all_with_quantity_and_revenue():
        raw_resp = EsProductQuantityRevenue.collect_quantity_and_revenue_by_pv_sku()
        parsed_resp = list(map(EsProductLogic.to_es_data,raw_resp))
        es = EsRepositoryInterface()
        es._index = Config.PRODUCT_INDEX
        es.doc_type = Config.PRODUCT_DOC_TYPE
        es.save_all(parsed_resp)
