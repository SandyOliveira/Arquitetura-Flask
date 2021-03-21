from flask import render_template



def init_app(app):
  @app.route("/")
  def index():
    products = ['baguete', 'pão frances']
    return render_template("index.html", products=products)