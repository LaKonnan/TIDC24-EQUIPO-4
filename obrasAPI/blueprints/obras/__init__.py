from flask import Flask, jsonify, request, Blueprint

from auth import AuthError, requires_role

from botocore.exceptions import DataNotFoundError

from re import I

import boto3

import os

blueprint = Blueprint('obras', __name__, url_prefix='/')


dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


OBRAS_TABLE = os.environ['OBRAS_TABLE']

@blueprint.route('/obras/<string:obraId>')
def get_obra(obraId):
    result = dynamodb_client.get_item(
        TableName = OBRAS_TABLE, Key={'obraId': {'S': obraId}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'No se encontro la obra: "obraId"'}), 404

    return jsonify(
        {
            'obraId': item.get('obraId').get('S'),
            'nombre': item.get('nombre').get('S'),
            'encargado': item.get('encargado').get('S'),
            'estado': item.get('estado').get('S'),
            'tipo': item.get('tipo').get('S')
        }
    )

@blueprint.route('/obra/tipos/<string:tipo>')
def obras_por_tipo(tipo):
    result = dynamodb_client.scan(
        TableName = OBRAS_TABLE,
        ScanFilter = {
            "tipo": {
                "ComparisonOperator": "EQ",
                "AttributeValueList": [{ "S": tipo }]
            }
        }
    )

    items = result['Items']
    if not items:
        return jsonify({ 'error':'No se han encontrado' }), 404
    response = jsonify(items)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



@blueprint.route('/obras')
@requires_role('manage:obras')
def get_obras():
    obras = dynamodb_client.scan(TableName = 'obras-dev')
    items = obras['Items']
    response = jsonify(items)
    return response


@blueprint.route('/obras', methods=['POST'])
@requires_role('manage:obras')
def create_obra():
    obraId = request.json.get('obraId')
    nombre = request.json.get('nombre')
    encargado = request.json.get('encargado')
    estado = request.json.get('estado')
    tipo = request.json.get('tipo')

    if not obraId or not nombre or not encargado:
        return jsonify({'error': 'Por favor ingrese todos los campos obligatorios'}), 400

    if not estado:
        estado = "inactiva"

    dynamodb_client.put_item(
        TableName = OBRAS_TABLE,
        Item ={
            'obraId': {'S': obraId},
            'nombre': {'S': nombre},
            'encargado': {'S': encargado},
            'estado': {'S': estado},
            'tipo': {'S': tipo}
        }
    )

    return jsonify({
        'message': 'obra creada',
        'Obra': {
            'obraId': obraId,
            'nombre': nombre,
            'encargado': encargado,
            'estado': estado,
            'tipo' : tipo,
            }
        })

@blueprint.route('/obras', methods=['PUT'])
@requires_role('manage:obras')
def edit_obra():
    obraId = request.json.get('obraId')
    nombre = request.json.get('nombre')
    encargado = request.json.get('encargado')
    estado = request.json.get('estado')
    tipo = request.json.get('tipo')

    key ={
        'obraId':{'S': obraId}
    }
    
    dynamodb_client.update_item(
        TableName = OBRAS_TABLE,
        Key= key,
        ExpressionAttributeNames = {
            
            '#name': 'nombre',
            '#enc': 'encargado',
            '#est': 'estado',
            '#tip': 'tipo'
        },
        UpdateExpression= 
        "set #name = :nombre, #enc = :encargado, #est = :estado, #tip = :tipo "
        ,
        
        ExpressionAttributeValues={
            
            ':nombre':{
                'S': nombre
            },
             ':encargado':{
                'S': encargado
            },
             ':estado':{
                'S': estado
            },
             ':tipo':{
                'S': tipo
            }
        }
        
    )
     
    return jsonify({'message': 'obra modificada'})

@blueprint.route('/obras/<string:obraId>', methods=['DELETE'])
@requires_role('manage:obras')
def delete_obra(obraId):
    result = dynamodb_client.delete_item(
         TableName = OBRAS_TABLE,
         Key = { 'obraId': {'S': obraId}}
    )
    return jsonify({'msg':'eliminado'})


@blueprint.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response