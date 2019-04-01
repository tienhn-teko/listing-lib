# coding=utf-8
import logging

__author__ = 'TienHN'
_logger = logging.getLogger(__name__)

settings = {
    "index": {
        "number_of_shards": 5,
        "number_of_replicas": 2,
        "max_result_window": 50000,
        "mapping": {"total_fields": {"limit": "10000"}}
    }
}

mapping = {
    "products": {
        "dynamic": "strict",
        "properties": {
            "attributes": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                        "code": {
                            "type": "keyword"
                        },
                    "id": {
                            "type": "integer",
                            "index": false
                            },
                    "is_compareable": {
                            "type": "boolean"
                            },
                    "is_filterable": {
                            "type": "boolean"
                            },
                    "is_searchable": {
                            "type": "boolean"
                            },
                    "name": {
                            "type": "keyword",
                            "index": false
                            },
                    "priority": {
                            "type": "integer"
                            },
                    "value": {
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
                        "index": false
                    },
                    "highlight": {
                        "type": "boolean",
                        "index": false
                    },
                    "id": {
                        "type": "keyword",
                        "index": false
                    },
                    "name": {
                        "type": "keyword",
                        "index": false
                    },
                    "parent_id": {
                        "type": "integer",
                        "index": false
                    },
                    "priority": {
                        "type": "integer",
                        "index": false
                    }
                }
            },
            "branch_in_stock": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "avaiable": {
                        "type": "integer"
                    },
                    "branch": {
                        "type": "keyword"
                    },
                    "incoming": {
                        "type": "integer"
                    },
                    "location": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "keyword"
                    },
                    "on_hand": {
                        "type": "integer"
                    },
                    "outgoing": {
                        "type": "integer"
                    },
                    "product_biz_type": {
                        "type": "keyword"
                    },
                    "reversed": {
                        "type": "integer"
                    },
                    "store_code": {
                        "type": "keyword"
                    },
                    "warehouse": {
                        "type": "keyword"
                    }
                }
            },
            "brand": {
                "dynamic": "strict",
                "properties": {
                    "code": {
                        "type": "keyword"
                    },
                    "description": {
                        "type": "keyword",
                        "index": false
                    },
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "keyword",
                        "index": false
                    }
                }
            },
            "category_path": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "code": {
                        "type": "keyword"
                    },
                    "description": {
                        "type": "keyword",
                        "index": false
                    },
                    "id": {
                        "type": "integer",
                        "index": false
                    },
                    "level": {
                        "type": "integer",
                        "index": false
                    },
                    "name": {
                        "type": "keyword",
                        "index": false
                    },
                    "parent_id": {
                        "type": "integer",
                        "index": false
                    },
                    "url": {
                        "type": "keyword",
                        "index": false
                    }
                }
            },
            "color": {
                "dynamic": "strict",
                "properties": {
                    "code": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "keyword",
                        "index": false
                    },
                    "value": {
                        "type": "keyword"
                    }
                }
            },
            "created_at": {
                "type": "date"
            },
            "display_name": {
                "type": "keyword",
                "index": false
            },
            "images": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                        "label": {
                            "type": "keyword",
                            "index": false
                        },
                    "priority": {
                            "type": "integer",
                            "index": false
                            },
                    "url": {
                            "type": "keyword",
                            "index": false
                            }
                }
            },
            "name": {
                "type": "keyword",
                "index": false
            },
            "price": {
                "properties": {
                    "sell_price": {
                        "type": "double"
                    },
                    "supplier_sale_price": {
                        "type": "double"
                    }
                }
            },
            "product_group": {
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "integer",
                        "index": false
                    },
                    "name": {
                        "type": "keyword",
                        "index": false
                    },
                    "variation_attributes": {
                        "type": "nested",
                        "dynamic": "strict",
                        "properties": {
                                "attribute_id": {
                                    "type": "integer",
                                    "index": false
                                },
                            "attribute_name": {
                                    "type": "keyword",
                                    "index": false
                                    }
                        }
                    },
                    "variation_products": {
                        "type": "nested",
                        "dynamic": "strict",
                        "properties": {
                                "attribute_value": {
                                    "type": "nested",
                                    "dynamic": "strict",
                                    "properties": {
                                        "code": {
                                            "type": "keyword",
                                            "index": false
                                        },
                                        "id": {
                                            "type": "integer",
                                            "index": false
                                        },
                                        "value": {
                                            "type": "keyword",
                                            "index": false
                                        }
                                    }
                                },
                            "sku": {
                                    "type": "keyword",
                                    "index": false
                                    }
                        }
                    }
                }
            },
            "promotion": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                        "channel": {
                            "type": "keyword"
                        },
                    "flash_sale": {
                            "type": "nested",
                            "properties": {
                                "end_time": {
                                    "type": "date"
                                },
                                "flash_sale_price": {
                                    "type": "double",
                                    "index": false
                                },
                                "quantity": {
                                    "type": "integer",
                                    "index": false
                                },
                                "start_time": {
                                    "type": "date"
                                }
                            }
                            },
                    "promotion_detail": {
                            "properties": {
                                "certain_promotions": {
                                    "type": "integer",
                                    "index": false
                                },
                                "definition": {
                                    "type": "nested",
                                    "dynamic": "strict",
                                    "properties": {
                                        "benefits": {
                                            "properties": {
                                                "items": {
                                                    "type": "nested",
                                                    "dynamic": "strict",
                                                    "properties": {
                                                        "name": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "sku": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "total": {
                                                            "type": "integer",
                                                            "index": false
                                                        },
                                                        "used": {
                                                            "type": "integer",
                                                            "index": false
                                                        }
                                                    }
                                                },
                                                "money": {
                                                    "dynamic": "strict",
                                                    "properties": {
                                                        "discount_type": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "max_discount": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "money": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "percent": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "type": {
                                                            "type": "keyword",
                                                            "index": false
                                                        }
                                                    }
                                                },
                                                "type": {
                                                    "type": "keyword"
                                                }
                                            }
                                        },
                                        "conditions": {
                                            "dynamic": "strict",
                                            "properties": {
                                                "coupon": {
                                                    "type": "keyword"
                                                },
                                                "payment": {
                                                    "dynamic": "strict",
                                                    "properties": {
                                                        "method": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "partner": {
                                                            "type": "keyword",
                                                            "index": false
                                                        },
                                                        "type": {
                                                            "type": "keyword",
                                                            "index": false
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "description": {
                                            "type": "keyword",
                                            "index": false
                                        },
                                        "end_time": {
                                            "type": "date"
                                        },
                                        "name": {
                                            "type": "keyword",
                                            "index": false
                                        },
                                        "promotion_id": {
                                            "type": "integer"
                                        },
                                        "start_time": {
                                            "type": "date"
                                        }
                                    }
                                },
                                "optional_promotions": {
                                    "type": "nested",
                                    "dynamic": "strict",
                                    "properties": {
                                        "promotions": {
                                            "type": "integer",
                                            "index": false
                                        }
                                    }
                                }
                            }
                            }
                }
            },
            "promotion_price": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                        "best_price": {
                            "type": "double"
                        },
                    "channel": {
                            "type": "keyword"
                            },
                    "flash_sale_price": {
                            "type": "double"
                            },
                    "promotion_price": {
                            "type": "double"
                            }
                }
            },
            "quantity": {
                "type": "double"
            },
            "rating_score": {
                "type": "float"
            },
            "revenue": {
                "type": "double"
            },
            "sale_categories": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                        "categories": {
                            "type": "nested",
                            "dynamic": "strict",
                            "properties": {
                                "category_path": {
                                    "type": "nested",
                                    "dynamic": "strict",
                                    "properties": {
                                        "code": {
                                            "type": "keyword"
                                        },
                                        "description": {
                                            "type": "keyword",
                                            "index": false
                                        },
                                        "id": {
                                            "type": "integer"
                                        },
                                        "level": {
                                            "type": "integer",
                                            "index": false
                                        },
                                        "name": {
                                            "type": "keyword",
                                            "index": false
                                        },
                                        "parent_id": {
                                            "type": "integer",
                                            "index": false
                                        },
                                        "url": {
                                            "type": "keyword",
                                            "index": false
                                        }
                                    }
                                }
                            }
                        },
                    "channel": {
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
            "seller_id": {
                "type": "integer"
            },
            "seo_info": {
                "dynamic": "strict",
                "properties": {
                    "description": {
                        "type": "keyword",
                        "index": false
                    },
                    "meta_description": {
                        "type": "keyword",
                        "index": false
                    },
                    "meta_keyword": {
                        "type": "keyword",
                        "index": false
                    },
                    "meta_title": {
                        "type": "keyword",
                        "index": false
                    },
                    "short_description": {
                        "type": "keyword",
                        "index": false
                    }
                }
            },
            "sku": {
                "type": "keyword"
            },
            "status": {
                "dynamic": "strict",
                "properties": {
                    "editing_status": {
                        "dynamic": "strict",
                        "properties": {
                            "code": {
                                "type": "keyword"
                            },
                            "id": {
                                "type": "integer",
                                "index": false
                            },
                            "name": {
                                "type": "keyword",
                                "index": false
                            }
                        }
                    },
                    "selling_status": {
                        "dynamic": "false",
                        "properties": {
                            "code": {
                                "type": "keyword"
                            },
                            "id": {
                                "type": "integer",
                                "index": false
                            },
                            "name": {
                                "type": "keyword",
                                "index": false
                            }
                        }
                    },
                    "srm_status": {
                        "dynamic": "strict",
                        "properties": {
                            "code": {
                                "type": "keyword"
                            },
                            "id": {
                                "type": "integer",
                                "index": false
                            },
                            "name": {
                                "type": "keyword",
                                "index": false
                            }
                        }
                    }
                }
            },
            "tag": {
                "type": "keyword"
            },
            "url": {
                "type": "keyword",
                "index": false
            },
            "warranty": {
                "dynamic": "strict",
                "properties": {
                    "warranty_description": {
                        "type": "keyword",
                        "index": false
                    },
                    "warranty_months": {
                        "type": "keyword",
                        "index": false
                    }
                }
            }
        }
    }
}
