from flask import Flask, render_template
from bakery.ext import configuration 
from flask_bootstrap import Bootstrap

app = Flask(__name__)




Bootstrap(app)
configuration.init_app(app)
@app.route("/")
def index():
  products = ['baguete', 'pão frances']
  return render_template("index.html", products=products)