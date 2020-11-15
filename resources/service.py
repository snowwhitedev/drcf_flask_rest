from flask import request
from flask_restful import Resource
from models.service import ServiceModel
from schemas.service import ServiceSchema

service_list_schema = ServiceSchema(many=True)


class Service(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        service = ServiceModel(
            name=data["name"],
            description=data["description"],
            status=data["status"],
            image=data["image"]
        )
        try:
            service.save_to_db()
            return {"message": "OK"}, 200
        except:
            return {"message": "error"}, 400

    @classmethod
    def get(cls):
        try:
            return {"data": service_list_schema.dump(ServiceModel.get_all())}, 200
        except:
            return {"message": "error"}, 400

    @classmethod
    def delete(cls, id: int):
        return id
