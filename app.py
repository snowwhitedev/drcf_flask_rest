from flask import Flask
from flask_restful import Api

from resources.test import Test

app = Flask(__name__)

api = Api(app)

api.add_resource(Test, "/api/v1/test")

if __name__ == "__main__":
    print("Running")
    app.run(port=5000, debug=True)