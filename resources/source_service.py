from flask import request
from flask_restful import Resource
from models.source_service import SourceServiceModel
from schemas.source_service import SourceServicSchema

source_service_list_schema = SourceServicSchema(many=True)


class SourceService(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        source_service = SourceServiceModel(
            name=data["name"],
            description=data["description"],
            service_id=data["service_id"]
        )
        try:
            source_service.save_to_db()
            return {"message": "OK"}, 200
        except:
            return {"message": "Error"}, 400

    @classmethod
    def get(cls):
        try:
            return {"data": source_service_list_schema.dump(SourceServiceModel.get_all())}, 200
        except:
            return {"message": "error"}, 400


class SourceServiceFilter(Resource):
    @classmethod
    def get(cls, service_id: int):
        try:
            data = source_service_list_schema.dump(SourceServiceModel.get_by_service_id(service_id))
            return {"data": data, "message": "OK"}, 200
        except:
            return {"message": "error"}, 400
