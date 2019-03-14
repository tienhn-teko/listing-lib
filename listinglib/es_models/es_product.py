# coding=utf-8
import logging

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

settings = {
    "index": {
        "number_of_shards": 1,
        "number_of_replicas": 2,
        "max_result_window": 50000,
        "mapping": {"total_fields": {"limit": "10000"}}
    }
}

mapping = {
    "product": {
        "properties": {
            "sku": {
                "type": "long"
            },
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
        }
    }
}
