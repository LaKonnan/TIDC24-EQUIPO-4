from flask import Flask, jsonify, request, Blueprint

# Definición del blueprint donde el 1er arg corresponde al nombre del blueprint y url_prefix corresponde a la url de llamada
blueprint = Blueprint('basic_api', __name__, url_prefix='/')


# Ruta de prueba "Hello World"
@blueprint.route("/hello")
def hello():
    return jsonify(message='Hola desde blueprint api gestion de archivos!')
