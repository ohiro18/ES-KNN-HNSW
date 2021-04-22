from elasticsearch import Elasticsearch
from datetime import datetime

import pathlib
import glob

es = Elasticsearch(
    hosts=[{'host': "es-sg-25u2403rq000qwfko.public.elasticsearch.aliyuncs.com", 'port':9200}],
    http_auth=('elastic', 'FY21!hands-on'))

res = es.cat.indices()


img_path = pathlib.Path('C:\\Users\\1200358\\Dev\\ES-KNN-HNSW\\app\\flask\\static')

for f in img_path.glob('*.jpg'):
    print(f.name)

    f_id = f.name.split('.')
    
    doc = { 
        "image_name" : f.name, 
        'timestamp': datetime.utcnow(), 
        "category" : category
        }

    actions.append(
        {
            '_index':index_name, 
            '_type':'_doc', 
            '_id':f_id[0],  
            '_source':doc
            }
            )


