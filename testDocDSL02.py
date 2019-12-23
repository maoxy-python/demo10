from elasticsearch import Elasticsearch

es = Elasticsearch(['192.168.236.10:9200'])

"""
doc = {
    "query": {
        "term": {
            "name": {
                "value": "古"
            }
        },
    },
    "sort": [
        {
            "age": {
                "order": "desc"
            }
        }
    ]
}
"""
"""
doc = {
    "query": {
        "match_all": {},
    },
    "from": 2,
    "size": 2,
}
"""

# 指定字段查询
"""
doc = {
    "query": {
        "match_all": {},
    },
    "_source": ['name', 'age']
}
"""

# 范围查询
"""
doc = {
    "query": {
        "range": {
            "age": {
                "gte": 10,
                "lte": 30
            }
        },
    },
}
"""

# 前缀查询
"""
doc = {
    "query": {
        "prefix": {
            "name": {
                "value": "古"
            }
        },
    },
}
"""

# 通配查询
"""
doc = {
    "query": {
        "wildcard": {
            "content": {
                "value": "古*"
            }
        },
    },
}
"""

# 多id查询
"""
doc = {
    "query": {
        "ids": {
            "values": ["lg5HwWkBxH7z6xax7W3_","lQ5HwWkBxH7z6xax7W3_"]
        }
    }
}
"""

# 模糊查询
"""
doc = {
    "query": {
        "fuzzy": {
            "content": "女孩"
        }
    }
}
"""

# 布尔查询
"""
doc = {
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "age": {
                            "gte": 10,
                            "lte": 40
                        }
                    }
                }
            ],
            "must_not": [
                {
                    "wildcard": {
                        "name": {
                            "value": "赵"
                        }
                    }
                }
            ]
        }
    },
    "sort": [
        {
            "age": {
                "order": "desc"
            }
        }
    ]
}
"""

# 高亮查询
"""
doc = {
    "query": {
        "term": {
            "content": {
                "value": "性感"
            }
        }
    },
    "highlight": {
        "fields": {
            "*": {}
        }
    }
}

"""

# 自定义高亮查询
doc = {
    "query": {
        "term": {
            "content": {
                "value": "性感"
            }
        }
    },
    "highlight": {
        "pre_tags": ["<span style='color:red'>"],
        "post_tags": ["</span>"],
        "fields": {
            "*": {}
        }
    }
}

sort_doc = es.search(index="dangdang", doc_type="product", body=doc)
for item in sort_doc['hits']['hits']:
    print(item['_source'])
    print(item['highlight'])












