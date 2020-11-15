from db import db
from typing import List
from sqlalchemy import or_
from settings.constant import USER_ROLES


class InventoryModel(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80))
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    image = db.Column(db.String(80))
    price = db.Column(db.Float)
    category = db.Column(db.String(80))
    inventoryStatus = db.Column(db.String(80))
    rating = db.Column(db.Float)
    role = db.Column(db.String(20), default=USER_ROLES["worker"])

    @classmethod
    def get_worker_inventory(cls) -> List["CategoryModel"]:
        return cls.query.filter_by(role=USER_ROLES["worker"]).all()

    @classmethod
    def get_supervisor_inventory(cls) -> List["CategoryModel"]:
        # return cls.query.filter(or_(role="", role = ""))
        return cls.query.filter(
            or_(InventoryModel.role == USER_ROLES["worker"], InventoryModel.role == USER_ROLES["supervisor"])
        ).all()

    @classmethod
    def get_all(cls) -> List["CategoryModel"]:
        return cls.query.all()

    @classmethod
    def get_by_id(cls, _id: int) -> "InventoryModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
