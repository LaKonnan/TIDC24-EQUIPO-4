import os
import boto3
from flask import Flask, jsonify, make_response, request


app = Flask(__name__)


dynamodb_client = boto3.client('dynamodb')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


OBRAS_TABLE = os.environ['OBRAS_TABLE']


@app.route('/obras/<string:obra_id>')
def get_obra(obra_id):
    result = dynamodb_client.get_item(
        TableName=OBRAS_TABLE, Key={'obraId': {'S': obra_id}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'No se encontro la obra: "obraId"'}), 404

    return jsonify(
        {
            'obraId': item.get('obraId').get('S'),
            'nombre': item.get('nombre').get('S'),
            'encargado': item.get('encargado').get('S'),
            'estado': item.get('estado').get('S')
        }
    )


@app.route('/obras')
def get_obras():
    obras = dynamodb_client.scan(TableName=OBRAS_TABLE)
    items = obras['Items']
    response = jsonify(items)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/obras', methods=['POST'])
def create_obra():
    obra_id = request.json.get('obraId')
    nombre = request.json.get('nombre')
    encargado = request.json.get('encargado')
    estado = request.json.get('estado')
    if not obra_id or not nombre or not encargado:
        return jsonify({'error': 'Por favor ingrese todos los campos obligatorios'}), 400

    if not estado:
        estado = "inactiva"

    dynamodb_client.put_item(
        TableName=OBRAS_TABLE,
        Item={
            'obraId': {'S': obra_id},
            'nombre': {'S': nombre},
            'encargado': {'S': encargado},
            'estado': {'S': estado}
            }
    )

    return jsonify({
        'message': 'obra creada',
        'Obra': {
            'obraId': obra_id,
            'nombre': nombre,
            'encargado': encargado,
            'estado': estado,
            }
        })


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
