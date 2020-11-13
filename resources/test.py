from flask_restful import Resource
from models.test import TestModel
from schemas.test import TestSchema

test_list_schema = TestSchema(many=True)


class Test(Resource):
    @classmethod
    def get(cls):
        data = TestModel.get_all()
        # if data:
        #     return data, 200
        return {"message": "Not Found"}, 400


class TestList(Resource):
    @classmethod
    def get(cls):
        return {"items": test_list_schema.dump(TestModel.get_all())}, 200
