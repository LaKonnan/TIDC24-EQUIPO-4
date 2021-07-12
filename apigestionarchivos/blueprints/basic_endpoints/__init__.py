from flask import Flask, jsonify, request, Blueprint


blueprint = Blueprint('basic_api', __name__, url_prefix='/')



@blueprint.route("/hello")
def hello():
    return jsonify(message='Hola desde blueprint api gestion de archivos!')
