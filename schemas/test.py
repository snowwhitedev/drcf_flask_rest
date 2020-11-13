from ma import ma
from models.test import TestModel


class TestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestModel
        dump_only = ("id",)
