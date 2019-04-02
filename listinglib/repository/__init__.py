# coding=utf-8
import logging

from elastictools.doctools import DocTools

from listinglib.config import EsConfig

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsRepositoryInterface:
    def __init__(self, elastic_url=None):
        self._es = DocTools.from_url(elastic_url or EsConfig.ELASTIC_URL)
        self._index = None
        self.doc_type = None

    def save(self, data):
        """
        index dữ liệu đơn lẻ vào elastic search
        :param data: EsData
        :return:
        """
        res = self._es._es.index(index=self._index, doc_type=self.doc_type,
                                 id=data.id, body=data.info)
        self._es.indextool().refresh(self._index)
        return res

    def save_all(self, data_list, chunk_size=100):
        """
        Bulk index list data to elastic search
        :param data_list: Array<EsData>
        :return:
        """
        queries = [
            {
                "_op_type": "update",
                "_id": data.id,
                "doc": data.info,
                "doc_as_upsert": True
            }
            for data in data_list
        ]
        res = self._es.bulk(index_name=self._index,
                            actions=queries, chunk_size=chunk_size)
        self._es.indextool().refresh(self._index)
        return res
