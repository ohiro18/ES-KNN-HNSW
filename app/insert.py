from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
from keras_vgg16 import VGGNet  

import pathlib
import glob

es = Elasticsearch(
    hosts=[{'host': "es-cn-mjc2443530001o0te.public.elasticsearch.aliyuncs.com", 'port':9200}],
    http_auth=('elastic', 'FY21!hands-on'))

# ESでindex一覧を表示
print(es.cat.indices())

index_name = "web_app_test"
img_path = pathlib.Path('C:\\Users\\1200358\\Dev\\ES-KNN-HNSW\\app\\flask\\static')
dataset_dict = []

model = VGGNet()  

for f in img_path.glob('*.jpg'):
    #print(f.name)
    f_id = f.name.split('.')    
    feature = model.extract_feat(f).tolist()  #vgg16 モデルを用いて特徴量データへ変換

    doc = { 
        "image_name" : f.name, 
        "feature" : feature 
        }

    dataset_dict.append(
        {
            '_index':index_name, 
            '_type':'_doc', 
            '_id':f_id[0],  
            '_source':doc
        }
    )

# ES indexへ一括インポート
helpers.bulk(es, dataset_dict)


