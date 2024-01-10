from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api
from os import environ

# from src.utils.magicrypt import Magicrypt

from src.resource.forecast import forecast_ns

# from src.service.tracker import Tracker

# initialization
app = Flask(__name__)
authorizations = {
    "apikey": {
        "type": "apiKey", "in": "header", "name": "Authorization"
    }
}

api = Api(
    app,
    doc="/doc/",
    authorizations=authorizations,
    version="1.0",
    title="API - People",
    description="Documentação para consulta da API de testes de people"
)

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app, resources={r"/*": {
    "origins": "*"
}})


# @app.before_request
# def decompress():
#     if request.data != b"" and environ["ENV"] != "local":
#         request.data = Magicrypt().decrypt(request.data)
#         request._cached_data = request.data
#     if environ["ENV"] != "local":
#         Tracker().track(view_function=app.view_functions[request.endpoint], user_action="request")


# @app.after_request
# def compress(response):
#     if environ["ENV"] != "local":
#         Tracker().track(view_function=app.view_functions[request.endpoint], user_action="response")
#         response.data = Magicrypt().encrypt(response.data)
#     return response


# namespaces
api.add_namespace(forecast_ns)

