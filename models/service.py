from db import db
from typing import List


class ServiceModel(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text())
    status = db.Column(db.String(30))
    image = db.Column(db.String())
    sources = db.relationship("SourceServiceModel", backref="service")


    @classmethod
    def get_all(cls) -> List["ServiceModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
