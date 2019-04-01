# coding=utf-8
import logging
import time
import json

from listinglib.repository.es_product import _collect_quantity_and_revenue_tk_result, \
    _collect_product_sku, collect_quantity_and_revenue_by_pv_sku

__author__ = 'TungLQ'
_logger = logging.getLogger(__name__)

start_time = time.time()

with open('result.json', 'w') as fp:
    res = collect_quantity_and_revenue_by_pv_sku().to_dict('records')
    json.dump(res, fp)

end_time = time.time()
print('Execution Time: %.9f' % (end_time - start_time))
