from flask import Flask, render_template
from flask import request
import es_operation

app = Flask(__name__)


ELASTIC_SERVER = 'elastic:FY21!hands-on@es-cn-mjc2443530001o0te.public.elasticsearch.aliyuncs.com:9200'
es = es_operation.Ela(es_server=ELASTIC_SERVER)

index_name = 'hans_on_image_search'
cates= es.get_category(index_name)

@app.route('/')
def index():
  return render_template("index.html", title="image", cates=cates)

@app.route('/pic', methods=['GET', 'POST'])
def post():
  cate = request.args.get('cate')
  images = es.get_doc(index_name, cate) 
  return render_template('index.html', \
    title = 'image', \
    message = '{}'.format(cate), cates=cates, selected=cate, images=images)


if __name__ == '__main__':
  app.run(host='0.0.0.0')

  