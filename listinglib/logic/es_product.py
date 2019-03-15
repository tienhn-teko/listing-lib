# coding=utf-8
import logging

from listinglib.es_models import EsData

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductLogic:
    @staticmethod
    def to_es_data(raw_product):
        """
        Hàm biến đổi dữ liệu product json thành es data để index vào elastic search
        :param raw_product:
        :return: EsData
        """
        id = raw_product.get("pv_sku", None)
        if not type(id) == str:
            raise Exception('pv_sku invalid ', raw_product)
        info = raw_product

        return EsData(_id=id, info=info)
