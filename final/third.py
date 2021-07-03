import os.path

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{base_dir}/data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


class Building(db.Model):
    __tablename__ = "buildings"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(64), unique=True)
    floors_count = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "floors_count": self.floors_count,
        }

    def __repr__(self):
        return f"ID: {self.id}, Address: {self.address}, Floors Count: {self.floors_count}"


db.create_all()


@app.route("/")
def no():
    return ""


def create_building_from_json(request_data):
    return Building(address=request_data.get("address"),
                    floors_count=request_data.get("floors_count"),
                    )


@app.route("/buildings", methods=["GET", "POST"])
@app.route("/buildings/<building_id>", methods=["GET", "PUT", "DELETE"])
def handle_buildings(building_id=None):
    request_method = request.method
    if request_method == "GET":
        if building_id:

            building = Building.query.filter_by(id=building_id).first()
            if building:
                return jsonify(building.to_dict())
            abort(404, "Building not found")
        buildings = Building.query.filter_by().all()
        buildings = [u.to_dict() for u in buildings]

        return jsonify(buildings)

    if request_method == "POST":
        request_data = request.get_json()
        address = request_data.get("address")
        building = Building.query.filter_by(address=address).first()
        if building:
            abort(400, "Address is already in use")
        new_building = create_building_from_json(request_data)
        db.session.add(new_building)
        db.session.commit()
        return jsonify({"message": "Building created"})
    if request_method == "PUT":
        building = Building.query.filter_by(id=building_id).first()
        if not building:
            abort(404, "Building Not Found")
        request_data = request.get_json()
        if "address" in request_data:
            building.address = request_data.get("address")
        if "floors_count" in request_data:
            building.surname = request_data.get("floors_count")
        db.session.add(building)
        db.session.commit()
        return jsonify({"message": "Building Updated"})

    if request_method == "DELETE":
        if not building_id:
            abort(400, "Building id is required")
        building = Building.query.filter_by(id=building_id).first()
        if not building:
            abort(404, "Building not found")
        db.session.delete(building)
        db.session.commit()
        return jsonify({"message": "Building deleted"})
    else:
        abort(405, "Method not allowed")


if __name__ == '__main__':
    app.run(debug=True, port=8090, host='0.0.0.0')
