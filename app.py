from flask import Flask
from flask_restful import Api

from db import db
from resources.test import Test
from resources.test import TestList
from resources.service import Service
from resources.source_service import SourceService
from resources.source_service import SourceServiceFilter


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(TestList, "/api/v1/test")
api.add_resource(Service, "/api/v1/service")
api.add_resource(SourceService, "/api/v1/source_service")
api.add_resource(SourceServiceFilter, "/api/v1/source_by_service/<int:service_id>")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
