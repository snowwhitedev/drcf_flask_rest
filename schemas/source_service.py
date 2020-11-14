from ma import ma
from models.source_service import SourceServiceModel


class SourceServicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SourceServiceModel
        dump_only = ("id",)