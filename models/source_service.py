from db import db
from typing import List


class SourceServiceModel(db.Model):
    __tablename__ = "source_service"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text())
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)

    # def json(self) -> SourceServiceJSON:
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description,
    #     }

    @classmethod
    def get_all(cls) -> List["SourceServiceModel"]:
        return cls.query.all()

    @classmethod
    def get_by_service_id(cls, service_id) -> List["SourceServiceModel"]:
        return cls.query.filter_by(service_id=service_id).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
