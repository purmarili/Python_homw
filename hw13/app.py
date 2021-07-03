from app import db


class Dog(db.Model):
    __tablename__ = "Dogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    color = db.Column(db.String(64), nullable=True)
    breed = db.Column(db.String(64), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "breed": self.breed,
        }

    def __repr__(self):
        return f"ID: {self.id} name: {self.name}"


import os.path

from models import *
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{base_dir}/data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

db.create_all()


def create_dog_from_json(request_data):
    return Dog(name=request_data.get("name"),
               color=request_data.get("color"),
               breed=request_data.get("breed")
               )


@app.route('/read', methods=["GET"])
def get_dogs():
    request_method = request.method
    if request_method == "GET":
        dogs = Dog.query.filter_by().all()
        dogs = [u.to_dict() for u in dogs]

        return jsonify(dogs)
    else:
        return "Method not allowed"


@app.route('/create', methods=["POST"])
def add_dog():
    request_data = request.get_json()
    name = request_data.get("name")
    color = request_data.get("color")
    breed = request_data.get("breed")
    new_dog = create_dog_from_json(request_data)
    db.session.add(new_dog)
    db.session.commit()
    return jsonify({"message": "New dog created"})


if __name__ == '__main__':
    app.run(debug=True, port=5555, host='127.0.0.1')
