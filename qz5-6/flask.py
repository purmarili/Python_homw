import os.path

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{base_dir}/data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from models import *

db.create_all()


def create_user_from_json(request_data):
    return Product(username=request_data.get("user"),
                   name=request_data.get("name"),
                   surname=request_data.get("surname"),
                   password=request_data.get("password")
                   )


@app.route('/')
def main_page():
    return 'Hello on products store'


@app.route('/create')
def add_product():
    pass


if __name__ == '__main__':
    app.config