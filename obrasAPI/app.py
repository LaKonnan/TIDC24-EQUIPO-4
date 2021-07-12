from re import I
from botocore.exceptions import DataNotFoundError
from flask import Flask, jsonify, make_response, request
from auth import AuthError

from blueprints.obras import blueprint as obras

from blueprints.gastos import blueprint as gastos

from blueprints.cajas_combustible import blueprint as cajas_combustible

from blueprints.cajas_chicas import blueprint as cajas_chicas

from blueprints.usuarios import blueprint as usuarios

from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(obras)

app.register_blueprint(gastos)

app.register_blueprint(cajas_combustible)

app.register_blueprint(cajas_chicas)

app.register_blueprint(usuarios)

CORS(app)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response