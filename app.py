from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api

from db import db
from ma import ma
from resources.test import TestList
from resources.service import Service
from resources.source_service import SourceService
from resources.source_service import SourceServiceFilter
from resources.category import Category
from resources.inventory import Inventory
from resources.inventory import InventoryAction
from resources.inventory import InventoryList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
CORS(app)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(TestList, "/api/v1/test")
api.add_resource(Service, "/api/v1/service")
api.add_resource(SourceService, "/api/v1/source_service")
api.add_resource(SourceServiceFilter, "/api/v1/source_by_service/<int:service_id>")
api.add_resource(Category, "/api/v1/category")
api.add_resource(Inventory, "/api/v1/inventory")
api.add_resource(InventoryAction, "/api/v1/inventory/<int:inventory_id>")
api.add_resource(InventoryList, "/api/v1/inventories/<string:role>")


@app.route("/")
def index():
    return render_template("index.html")


db.init_app(app)
if __name__ == "__main__":
    ma.init_app(app)
    app.run(port=5000, debug=True)
