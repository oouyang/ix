from flask import Flask
import os,sys,json

pdir = os.path.dirname(os.path.realpath(__file__))
pdir = os.path.dirname(pdir)
sys.path.append(pdir)

from app import getChapter, getCList

#x = getChapter(317,66236)

app = Flask(__name__)


@app.route('/l/<int:l>/c/<int:c>')
def ix(l,c):
  #l=request.args.get('l')
  #c=request.args.get('c')
  #ret = '%d-%d'%(l,c)
  return '<pre>'+'\n'.join(getChapter(c,l))+'</pre>'

@app.route('/api/l/<int:l>/c/<int:c>')
def ixapi(l,c):
  return json.dumps(getChapter(c,l))

@app.route('/api/l/<int:l>')
def ixl(l):
  return getCList(l)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
