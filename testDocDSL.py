from elasticsearch import Elasticsearch


class ElasticObj(object):

    def __init__(self, index_name, index_type, ip="192.168.236.10"):
        """

        :param index_name: 索引名称
        :param index_type: 索引类型
        :param ip: es服务所在ip
        """
        self.index_name = index_name
        self.index_type = index_type
        self.es = Elasticsearch([ip], port=9200)

    def get_data_by_boby(self):

        doc = {
            "query": {
                "term": {
                    "address": {
                        "value": "南京"
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

        _searched = self.es.search(index=self.index_name, doc_type=self.index_type, body=doc)

        for item in _searched['hits']['hits']:
            print(item['_source'])


if __name__ == '__main__':
    obj = ElasticObj('ems', "emp")
    obj.get_data_by_boby()

