from ma import ma
from models.service import ServiceModel
from models.source_service import SourceServiceModel
from schemas.source_service import SourceServicSchema


class ServiceSchema(ma.SQLAlchemyAutoSchema):
    sources = ma.Nested(SourceServicSchema, many=True)

    class Meta:
        model = ServiceModel
        dump_only = ("id",)
