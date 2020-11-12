from flask_restful import Resource


class Test(Resource):
    @classmethod
    def get(cls):
        return {"message": "Welcome"}, 200
