# coding=utf-8
import logging

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from string import Template

from listinglib.config import EsConfig, DatabaseConfig
from listinglib.repository import EsRepositoryInterface

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)


class EsProductRepository(EsRepositoryInterface):
    def __init__(self, es_product=None, doc_type=None):
        super().__init__()
        self._index = es_product or EsConfig.PRODUCT_CATALOG_INDEX
        self.doc_type = doc_type or EsConfig.PRODUCT_CATALOG_DOC_TYPE


def collect_quantity_and_revenue_by_pv_sku():
    # join pv_sku voi tien va so luong hang ban ra
    pv_sku_df = _collect_product_sku()
    quan_reve_df = _collect_quantity_and_revenue_tk_result()
    merged_products = pd.merge(
        pv_sku_df, quan_reve_df,
        on='pv_sku',
        how='left').fillna({'tien_ban_ra': 0, 'sl_ban_ra': 0})
    # lay gia tri max va min khac 0
    tien_ban_ra = np.asarray(merged_products.iloc[:]['tien_ban_ra'].values)
    sl_ban_ra = np.asarray(merged_products.iloc[:]['sl_ban_ra'].values)
    tien_ban_ra = tien_ban_ra[tien_ban_ra > 0]
    sl_ban_ra = sl_ban_ra[sl_ban_ra > 0]
    tien_ban_ra_min = min(tien_ban_ra, default=0)
    tien_ban_ra_max = max(tien_ban_ra, default=0)
    sl_ban_ra_min = min(sl_ban_ra, default=0)
    sl_ban_ra_max = max(sl_ban_ra, default=0)
    # normalize quantity va revenue

    return result


def _collect_product_sku():
    catalog_template = Template(
        'mysql+pymysql://$user:$password@$host:$port/$database'
    ).substitute(
        user=DatabaseConfig.CATALOG_DB_USER,
        password=DatabaseConfig.CATALOG_DB_PASS,
        host=DatabaseConfig.CATALOG_DB_HOST,
        port=DatabaseConfig.CATALOG_DB_PORT,
        database=DatabaseConfig.CATALOG_DB_NAME)
    engine = create_engine(catalog_template)
    pv_sku_df = pd.read_sql_table(
        table_name='products', con=engine, columns=['pv_sku'])
    return pv_sku_df


def _collect_quantity_and_revenue_tk_result():
    tk_result_template = Template(
        'mysql+pymysql://$user:$password@$host:$port/$database'
    ).substitute(
        user=DatabaseConfig.TK_RESULT_DB_USER,
        password=DatabaseConfig.TK_RESULT_DB_PASS,
        host=DatabaseConfig.TK_RESULT_DB_HOST,
        port=DatabaseConfig.TK_RESULT_DB_PORT,
        database=DatabaseConfig.TK_RESULT_DB_NAME)
    engine = create_engine(tk_result_template)
    sql_query = _build_aggregate_sale_quantity_and_revenue_query()
    quan_reve_df = pd.read_sql(sql=sql_query, con=engine)
    quan_reve_df.rename(columns={'ma_vt': 'pv_sku'}, inplace=True)
    sql_query = _build_aggregate_sale_quantity_and_revenue_query()
    return quan_reve_df


def _build_aggregate_sale_quantity_and_revenue_query():
    return "SELECT " \
        "ma_vt, " \
        "sum(CASE WHEN ma_ct = 'PTX' THEN tien2 ELSE 0 END) " \
        "- sum(CASE WHEN ma_ct = 'HDF' THEN tien2 ELSE  0 END) as tien_ban_ra, " \
        "sum(CASE WHEN ma_ct = 'PTX' THEN  so_luong ELSE 0 END) " \
        "- sum(CASE WHEN ma_ct = 'HDF' THEN so_luong ELSE 0 END) as sl_ban_ra " \
        "FROM " \
        "daily_revenue_detail_v1 " \
        "GROUP BY " \
        "ma_vt " \
        "ORDER BY " \
        "ma_vt " \
        # "LIMIT 10"
