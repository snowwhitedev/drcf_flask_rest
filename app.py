from flask import Flask
from flask_restful import Api

from db import db
from resources.test import Test
from resources.test import TestList
from resources.service import Service


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

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
