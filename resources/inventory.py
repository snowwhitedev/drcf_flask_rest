from flask import request
from flask_restful import Resource
from models.inventory import InventoryModel
from schemas.inventory import InventorySchema
from settings.constant import USER_ROLES

worker_items = ["id", "code", "name", "description", "image", "category", "inventoryStatus", "role"]
supervisor_items = ["id", "code", "name", "description", "image", "category", "inventoryStatus", "role", "price"]
statistics_items = ["id", "code", "name", "description", "image", "category", "inventoryStatus", "role", "price",
                    "rating"]
inventory_schema = InventorySchema()
inventory_list_schema = InventorySchema(many=True)
inventory_worker_schema = InventorySchema(many=True, only=worker_items)
inventory_worker_schema = InventorySchema(many=True, only=supervisor_items)
inventory_statistics_schema = InventorySchema(many=True, only=statistics_items)


class Inventory(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        inventory = InventoryModel(
            code=data["code"],
            name=data["name"],
            description=data["description"],
            image=data["image"],
            price=data["price"],
            category=data["category"],
            inventoryStatus=data["inventoryStatus"],
            rating=data["rating"],
            role=data["role"]
        )
        try:
            inventory.save_to_db()
            return {"message": "OK"}, 200
        except:
            return {"message": "error"}, 400


class InventoryAction(Resource):
    @classmethod
    def put(cls, inventory_id: int):
        inventory_json = request.get_json()
        inventory = InventoryModel.get_by_id(inventory_id)
        print("[before save]", inventory)
        if inventory:

            inventory = inventory_schema.load(inventory_json)
            print("[save]", inventory)
            inventory.save_to_db()

            return inventory_schema.dump(inventory), 200
        else:
            return {"message": "No inventory with this id"}, 404

    @classmethod
    def delete(cls, inventory_id: int):
        inventory = InventoryModel.get_by_id(inventory_id)
        if inventory:
            inventory.delete_from_db()
            return {"message": "OK"}, 200
        else:
            return {"message": "No inventory with that id"}, 404


class InventoryList(Resource):
    @classmethod
    def get(cls):
        role_json = request.get_json()
        role = role_json["role"]
        print(role)
        try:
            if role == USER_ROLES["worker"]:
                return {"data": inventory_list_schema.dump(InventoryModel.get_worker_inventory())}, 200
            if role == USER_ROLES["supervisor"]:
                return {"data": inventory_list_schema.dump(InventoryModel.get_supervisor_inventory())}, 200
            if role == USER_ROLES["statistics"]:
                return {"data": inventory_list_schema.dump(InventoryModel.get_all())}, 200
        except:
            return {"message": "error"}, 400
