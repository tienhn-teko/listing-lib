# coding=utf-8
import logging
from listinglib.repository import EsRepositoryInterface

__author__ = 'TungLQ'
_logger = logging.getLogger(__name__)

products = [
    {
        'sku': 1,
        'name': 'Combo Intel i3-8100 + Asus TUF H310M-Plus Gaming + RAM Adata XPG GAMMIX D10 8GB (2400) + Asus CERBERUS GTX 1050 Ti 4GB'
    },
    {
        'sku': 2,
        'name': 'Combo Intel i8-8550 + MSI Z370 Tomahawk + G.Skill DDR4 2x8GB (3000) + MSI GTX 1070 Ti Gaming 8GB'
    }
]

def test_update_products():
    es_repo = EsRepositoryInterface()
    es_repo._index = 'product_catalog_dev'
    try:
        es_repo.is_existed
    except Exception:
        es_repo.create_if_not_exists()
    es_repo.update_products(data=products)
