PUT hans_on_image_search  
{  
    "aliases": {  
        "images": {}  
      },   
      "settings": {  
        "index.codec": "proxima",  
        "index.vector.algorithm": "hnsw",  
        "index.number_of_replicas":1,  
        "index.number_of_shards":3  
      },  
      "mappings": {  
        "_doc": {  
          "properties": {  
            "image_name": {
                "type": "keyword"  
            },
            "feature": {  
                  "type": "proxima_vector",  
                  "dim": 512  
            } 
            }  
        }  
    }  
}  


GET hans_on_image_search/_search
{
    "query": {  
        "hnsw": {  
            "feature": {  
                "vector": [255,255,255,255,255,255,255,255,255,255],  
                "size": 3,  
                "ef": 1  
            }  
        }  
    },  
    "from": 0,  
    "size": 20,   
    "sort": [  
    {  
        "_score": {  
            "order": "desc"  
        }  
    }  
   ],   
    "collapse": {  
        "field": "image_name"  
    },  
    "_source": {  
        "includes": [  
            "image_name"  
        ]  
    }
}