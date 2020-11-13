from db import db
from typing import Dict, List, Union

TestJSON = Dict[str, Union[int, str]]


class TestModel(db.Model):
    __tablename__ = "test"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name: str):
        self.name = name

    def json(self) -> TestJSON:
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def get_all(cls) -> List["TestJSON"]:
        return cls.query.all()