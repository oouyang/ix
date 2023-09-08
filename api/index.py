from flask import Flask

app = Flask(__name__)


@app.route('/l/<string:l>/c/<string:c>')
def ix():
  l=request.args.get('l')
  c=request.args.get('c')
  return '%d-%d'%(l,c)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
