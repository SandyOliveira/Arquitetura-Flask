from flask import Flask, render_template
from bakery.ext import configuration 
from bakery.ext import appearance


from bakery.blueprints import views
from bakery.blueprints import restapi


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
views.init_app(app)
restapi.init_app(app)

