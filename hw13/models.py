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
