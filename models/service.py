from db import db
from typing import Dict, List, Union

ServiceJSON = Dict[str, Union[int, str, str, str, str]]


class ServiceModel(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text())
    status = db.Column(db.String(30))
    image = db.Column(db.String())

    # def __init__(self, name: str, description: str, status: str, image: str):
    #     self.name = name
    #     self.description = description
    #     self.status = status
    #     self.image = image

    def json(self) -> ServiceJSON:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "image": self.image
        }

    @classmethod
    def get_all(cls) -> List["ServiceJSON"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
