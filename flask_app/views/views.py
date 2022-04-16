# encoding=utf8
# flask app views
from . import main
from flask_app import db

@main.route("/",methods=['GET','POST'])
def index():
    return "index"

