from flask import Flask, jsonify, request, Blueprint

from auth import AuthError, requires_role

import boto3

import os

blueprint = Blueprint('cajas_combustible', __name__, url_prefix='/')


dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


CAJAS_TABLE = os.environ['CAJAS_TABLE']
CAJAS_COMBUSTIBLE = os.environ['CAJAS_COMBUSTIBLE']


@blueprint.route('/combustible')
def get_cajaCombustible():
    cajas = dynamodb_client.scan(TableName=CAJAS_TABLE)
    items = cajas['Items']
    response = jsonify(items)
    return response

@blueprint.route('/combustible/<string:id_caja>')
def get_caja_comb(id_caja):
    result = dynamodb_client.scan(
        TableName = CAJAS_COMBUSTIBLE,
        ScanFilter = {
            "id_caja_asociada": {
                "ComparisonOperator": "EQ",
                "AttributeValueList": [{ "S": id_caja }]
            }
        }
    )
    
    items = result['Items']
    if not items:
        return jsonify({ 'error':'No se han encontrado' }), 404
    
    response = jsonify(items)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
