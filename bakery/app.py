from flask import Flask, render_template
from bakery.ext import configuration 
from bakery.ext import appearance
from bakery.ext import views


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
views.init_app(app)

