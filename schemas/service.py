from ma import ma
from models.service import ServiceModel


class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceModel
        dump_only = ("id",)