from botocore.exceptions import DataNotFoundError
from flask import Flask, jsonify, request, Blueprint

from auth import AuthError, requires_role

import boto3

import os

blueprint = Blueprint('maquinas', __name__, url_prefix='/')


dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

TABLE_MAQUINAS = os.environ['TABLE_MAQUINAS']

@blueprint.route('/maquinas')
def get_maquinas():
    maquinas = dynamodb_client.scan(TableName=TABLE_MAQUINAS)
    items = maquinas['Items']
    response = jsonify(items)
    return response

@blueprint.route('/maquinas/<string:id_maq>')
def get_maquina(id_maq):
    result = dynamodb_client.scan(
        TableName = TABLE_MAQUINAS,
        ScanFilter = {
            "id_maqquina": {
                "ComparisonOperator": "EQ",
                "AttributeValueList": [{ "S": id_maq }]
            }
        }
    )

    items = result['Items']
    if not items:
        return jsonify({ 'error':'No se han encontrado' }), 404
    
    response = jsonify(items)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@blueprint.route('/maquinas', methods=['POST'])
def new_maq():
    # recibir datos
    id_maquina = request.json.get('id_maquina')
    patente = request.json.get('patente')
    nombre = request.json.get('nombre')
    ubicacion = request.json.get('ubicacion')

    dynamodb_client.put_item(
        TableName = TABLE_MAQUINAS,
        Item = {
            'id_maquina': {'S': id_maquina },
            'patente': {'S': patente },
            'nombre': {'S': nombre },
            'ubicacion': {'S': ubicacion }
        }
    )

    return jsonify({'message': 'creada'})

@blueprint.route('/maquinas/<string:id_maq>', methods=['DELETE'])
def delete_maq(id_maq):
    result = dynamodb_client.delete_item(
        TableName = TABLE_MAQUINAS,
        Key = {
            'id_maquina':  {'S': id_maq }
        }
    )


@blueprint.route('/maquinas/<string:id_maq>', methods=['PUT'])
def update_maq(id_maq):
    patente = request.json.get('patente')
    nombre = request.json.get('nombre')
    ubicacion = request.json.get('ubicacion')

    key = {
        'id_maquina': {'S': id_maq}
    }

    # actualizar caja combustible
    dynamodb_client.update_item (
        TableName = TABLE_MAQUINAS,
        key =  key,
        ExpressionAttributeNames = {
            '#patente': ':patente',
            '#nombre': ':nombre',
            '#ubicacion': ':ubicacion'
        },
        UpdateExpression= 
        "set #patente = :patente, #nombre = :nombre, #ubicacion = :ubicacion"
        ,
        ExpressionAttributeValues = {
            'patente': {
                ':patente': {
                    'S': patente
                },

                ':nombre': {
                    'S': nombre
                },

                ':ubicacion': {
                    'S': ubicacion
                }
            }

        }

    )