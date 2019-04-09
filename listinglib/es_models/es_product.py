# coding=utf-8
import logging

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

settings = {
    "index": {
        "max_result_window": 123,
        "analysis": {
            "filter": {
                "synonym_filter": {
                    "type": "synonym",
                    "synonyms_path": "/etc/elasticsearch/analysis/synonyms.txt"
                }
            },
            "analyzer": {
                "synonym_analyzer": {
                    "filter": [
                        "lowercase",
                        "synonym_filter"
                    ],
                    "tokenizer": "standard"
                }
            }
        }
    }
}

mapping = {
    "products": {
        "dynamic": "strict",
        "properties": {
            "sku": {
                "type": "keyword"
            },
            "name": {
                "type": "keyword",
                "index": False
            },
            "seller_id": {
                "type": "integer"
            },
            "url": {
                "type": "keyword",
                "index": False
            },
            "images": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "url": {
                        "index": False,
                        "type": "keyword"
                    },
                    "label": {
                        "index": False,
                        "type": "keyword"
                    },
                    "priority": {
                        "index": False,
                        "type": "integer"
                    }
                }
            },
            "display_name": {
                "type": "keyword",
                "index": False
            },
            "color": {
                "dynamic": "strict",
                "properties": {
                    "name": {
                        "type": "keyword",
                        "index": False
                    },
                    "value": {
                        "type": "keyword"
                    },
                    "code": {
                        "type": "keyword"
                    }
                }
            },
            "attributes_group": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "group_value": {
                        "type": "keyword",
                        "index": False
                    },
                    "highlight": {
                        "type": "boolean",
                        "index": False
                    },
                    "priority": {
                        "type": "integer",
                        "index": False
                    },
                    "parent_id": {
                        "type": "integer",
                        "index": False
                    },
                    "id": {
                        "type": "keyword",
                        "index": False
                    },
                    "name": {
                        "type": "keyword",
                        "index": False
                    }
                }
            },
            "attributes": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "integer",
                        "index": False
                    },
                    "code": {
                        "type": "keyword"
                    },
                    "value": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "keyword",
                        "index": False
                    },
                    "priority": {
                        "type": "integer"
                    },
                    "is_searchable": {
                        "type": "boolean"
                    },
                    "is_filterable": {
                        "type": "boolean"
                    },
                    "is_compareable": {
                        "type": "boolean"
                    }
                }
            },
            "product_group": {
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "integer",
                        "index": False
                    },
                    "name": {
                        "type": "keyword",
                        "index": False
                    },
                    "variation_attributes": {
                        "type": "nested",
                        "dynamic": "strict",
                        "properties": {
                            "attribute_id": {
                                "type": "integer",
                                "index": False
                            },
                            "attribute_name": {
                                "type": "keyword",
                                "index": False
                            }
                        }
                    },
                    "variation_products": {
                        "type": "nested",
                        "dynamic": "strict",
                        "properties": {
                            "sku": {
                                "type": "keyword",
                                "index": False
                            },
                            "attribute_value": {
                                "type": "nested",
                                "dynamic": "strict",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "index": False
                                    },
                                    "code": {
                                        "type": "keyword",
                                        "index": False
                                    },
                                    "value": {
                                        "type": "keyword",
                                        "index": False
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "category_path": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "integer",
                        "index": False
                    },
                    "code": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "keyword",
                        "index": False
                    },
                    "url": {
                        "type": "keyword",
                        "index": False
                    },
                    "description": {
                        "type": "keyword",
                        "index": False
                    },
                    "parent_id": {
                        "type": "integer",
                        "index": False
                    },
                    "level": {
                        "type": "integer",
                        "index": False
                    }
                }
            },
            "sale_categories": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "channel": {
                        "type": "keyword"
                    },
                    "categories": {
                        "type": "nested",
                        "dynamic": "strict",
                        "properties": {
                            "category_path": {
                                "type": "nested",
                                "dynamic": "strict",
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "code": {
                                        "type": "keyword"
                                    },
                                    "name": {
                                        "type": "keyword",
                                        "index": False
                                    },
                                    "description": {
                                        "type": "keyword",
                                        "index": False
                                    },
                                    "url": {
                                        "type": "keyword",
                                        "index": False
                                    },
                                    "parent_id": {
                                        "type": "integer",
                                        "index": False
                                    },
                                    "level": {
                                        "type": "integer",
                                        "index": False
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "brand": {
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "code": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "keyword",
                        "index": False
                    },
                    "description": {
                        "type": "keyword",
                        "index": False
                    }
                }
            },
            "status": {
                "dynamic": "strict",
                "properties": {
                    "selling_status": {
                        "dynamic": "False",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "index": False
                            },
                            "code": {
                                "type": "keyword"
                            },
                            "name": {
                                "type": "keyword",
                                "index": False
                            }
                        }
                    },
                    "editing_status": {
                        "dynamic": "strict",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "index": False
                            },
                            "code": {
                                "type": "keyword"
                            },
                            "name": {
                                "type": "keyword",
                                "index": False
                            }
                        }
                    },
                    "srm_status": {
                        "dynamic": "strict",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "index": False
                            },
                            "code": {
                                "type": "keyword"
                            },
                            "name": {
                                "type": "keyword",
                                "index": False
                            }
                        }
                    }
                }
            },
            "seo_info": {
                "dynamic": "strict",
                "properties": {
                    "description": {
                        "type": "keyword",
                        "index": False
                    },
                    "meta_title": {
                        "type": "keyword",
                        "index": False
                    },
                    "meta_keyword": {
                        "type": "keyword",
                        "index": False
                    },
                    "meta_description": {
                        "type": "keyword",
                        "index": False
                    },
                    "short_description": {
                        "type": "keyword",
                        "index": False
                    }
                }
            },
            "tag": {
                "type": "keyword"
            },
            "warranty": {
                "dynamic": "strict",
                "properties": {
                    "warranty_months": {
                        "type": "keyword",
                        "index": False
                    },
                    "warranty_description": {
                        "index": False,
                        "type": "keyword"
                    }
                }
            },
            "search_text": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "created_at": {
                "type": "date"
            },
            "price": {
                "properties": {
                    "supplier_sale_price": {
                        "type": "double"
                    },
                    "sell_price": {
                        "type": "double"
                    }
                }
            },
            "promotion_prices": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "channel": {
                        "type": "keyword"
                    },
                    "promotion_price": {
                        "type": "double"
                    },
                    "flash_sale_price": {
                        "type": "double"
                    },
                    "best_price": {
                        "type": "double"
                    }
                }
            },
            "promotions": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "channel": {
                        "type": "keyword"
                    },
                    "flash_sales": {
                        "type": "nested",
                        "properties": {
                            "start_time": {
                                "type": "date"
                            },
                            "end_time": {
                                "type": "date"
                            },
                            "quantity": {
                                "index": False,
                                "type": "integer"
                            },
                            "flash_sale_price": {
                                "index": False,
                                "type": "double"
                            }
                        }
                    },
                    "promotion_details": {
                        "properties": {
                            "definition": {
                                "type": "nested",
                                "dynamic": "strict",
                                "properties": {
                                    "promotion_id": {
                                        "type": "integer"
                                    },
                                    "start_time": {
                                        "type": "date"
                                    },
                                    "end_time": {
                                        "type": "date"
                                    },
                                    "name": {
                                        "type": "keyword",
                                        "index": False
                                    },
                                    "description": {
                                        "type": "keyword",
                                        "index": False
                                    },
                                    "benefits": {
                                        "properties": {
                                            "type": {
                                                "type": "keyword"
                                            },
                                            "money": {
                                                "dynamic": "strict",
                                                "properties": {
                                                    "type": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "discount_type": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "percent": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "amount": {
                                                        "type": "double",
                                                        "index": False
                                                    },
                                                    "max_discount": {
                                                        "type": "keyword",
                                                        "index": False
                                                    }
                                                }
                                            },
                                            "items": {
                                                "type": "nested",
                                                "dynamic": "strict",
                                                "properties": {
                                                    "sku": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "name": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "total": {
                                                        "type": "integer",
                                                        "index": False
                                                    },
                                                    "used": {
                                                        "type": "integer",
                                                        "index": False
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "conditions": {
                                        "dynamic": "strict",
                                        "properties": {
                                            "payment": {
                                                "dynamic": "strict",
                                                "properties": {
                                                    "method": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "partner": {
                                                        "type": "keyword",
                                                        "index": False
                                                    },
                                                    "type": {
                                                        "type": "keyword",
                                                        "index": False
                                                    }
                                                }
                                            },
                                            "coupon": {
                                                "type": "keyword"
                                            }
                                        }
                                    }
                                }
                            },
                            "optional_promotions": {
                                "type": "nested",
                                "dynamic": "strict",
                                "properties": {
                                    "promotions": {
                                        "type": "integer",
                                        "index": False
                                    }
                                }
                            },
                            "certain_promotions": {
                                "type": "integer",
                                "index": False
                            }
                        }
                    }
                }
            },
            "branch_in_stocks": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "incoming": {
                        "type": "integer"
                    },
                    "product_biz_type": {
                        "type": "keyword"
                    },
                    "reserved": {
                        "type": "integer"
                    },
                    "warehouse": {
                        "type": "keyword"
                    },
                    "store_code": {
                        "type": "keyword"
                    },
                    "outgoing": {
                        "type": "integer"
                    },
                    "location": {
                        "type": "keyword"
                    },
                    "available": {
                        "type": "integer"
                    },
                    "on_hand": {
                        "type": "integer"
                    },
                    "branch": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "keyword"
                    }
                }
            },
            "revenue": {
                "type": "double"
            },
            "quantity": {
                "type": "double"
            },
            "rating_score": {
                "type": "float"
            }
        }
    }
}
