from elasticsearch import Elasticsearch

# 建立连接
es = Elasticsearch(
    ["192.168.236.10:9200"],
)

# 测试连接是否成功
# print(es.ping())

# 打印当前节点的信息
# print(es.info())

# 查看当前节点的状态
# print(es.cluster.health())

# 查看当前节点的索引
# print(es.cat.indices())

# term查询
"""
res = es.search(
    index="dangdang",
    body={
        "query": {
            "match_all": {}
        }
    }
)
# print(res['hits']['hits'][0]["_source"])
for item in res['hits']['hits']:
    print(item['_source'])
"""


# 创建索引
"""
mapping = {
    "mappings": {
        "product": {
            "properties": {
                "name": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "age": {"type": "integer"},
                "price": {"type": "double"},
                "content": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "createDate": {"type": "date"}
            }
        }
    }
}

res = es.indices.create(index="dangdang",  body=mapping)
print(res)
"""
# es_1 = es.get(index="dangdang", doc_type="product", id="1")
# print(es_1)

# 在索引中创建一条记录
"""
body = {
    "name": "古力娜扎",
    "age": 22,
    "price": 333.45,
    "content": "古力娜扎是一位非常美丽而又性感的女孩",
    "createDate": "2011-11-11"
}
res = es.index(index="dangdang", doc_type="product", id=None, body=body)
print(res)
"""

# 查询文档
"""
doc = es.get(index="dangdang", doc_type="product", id="uNj6Em8BfPs-eRY11WWV")
print(doc)
print(doc['_source'])
"""


# 删除文档
# doc = es.delete(index="dangdang", doc_type="product", id="t9jwEm8BfPs-eRY1uWX-")
# print(doc)

# 更新文档
"""
body = {
    "doc": {
        "content": "古力娜扎是一位非常美丽而又性感的女孩,她的身高达到了1.72，拥有非常修长的身材"
    }
}
res = es.update(index="dangdang", doc_type="product", id="uNj6Em8BfPs-eRY11WWV", body=body)
print(res)
"""

# 批量更新
"""
doc = [
    {"index": {}},
    {
        "name": "赵丽颖",
        "age": 32,
        "price": 1111.45,
        "content": "赵丽颖是一位非常美丽而又性感的女孩",
        "createDate": "2015-11-11"},
    {"index": {}},
    {
        "name": "刘亦菲",
        "age": 42,
        "price": 2222.45,
        "content": "刘亦菲是一位非常美丽而又性感的女孩",
        "createDate": "2016-11-11"},
    {"index": {}},
    {
        "name": "赵奕欢",
        "age": 2,
        "price": 333.45,
        "content": "赵奕欢是一位非常美丽而又性感的女孩",
        "createDate": "2017-11-11"},
]

res = es.bulk(index="dangdang", doc_type="product", body=doc)
print(res)
"""
