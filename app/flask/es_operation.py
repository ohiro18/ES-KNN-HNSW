from datetime import datetime
import pathlib, glob
#import numpy as np

from elasticsearch import Elasticsearch
from elasticsearch import helpers


class Ela():
    def __init__(self, es_server):
        self.es = Elasticsearch(es_server)

    def get_indices(self):
        es = self.es
        return es.cat.indices()

    # Categoryの種類を返す
    def get_category(self, index_name):
        es = self.es
        body =  {
            "aggs" : {
                "by_category" : { "terms": { "field" : "category" } }
            },
            "size" : 0
        }
        res = es.search(index=index_name, body=body, size=0)
        return [k['key'] for k in res['aggregations']['by_category']['buckets']]

    # category 内の画像名をランダムで返す
    def get_doc(self, index_name, cate):
        es = self.es
        body =  { 
            "query": {
                "function_score" : {
                    "query": {"match": { "category" : cate}},
                    "random_score": {}
                }
            }
        }
        res = es.search(index=index_name, body=body, size=5)
        return [s['_source']['image_name'] for s in res['hits']['hits'] ]

        