from flask import request
from flask_restful import Resource
from models.category import CategoryModel
from schemas.category import CategorySchema

category_list_schema = CategorySchema(many=True)


class Category(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        category = CategoryModel(
            label=data["label"],
            value=data["value"]
        )
        try:
            category.save_to_db()
            return {"message": "OK"}, 200
        except:
            return {"message": "error"}, 400

    @classmethod
    def get(cls):
        try:
            return {"data": category_list_schema.dump(CategoryModel.get_all())}, 200
        except:
            return {"message": "error"}, 400

    @classmethod
    def delete(cls, id: int):
        return id
