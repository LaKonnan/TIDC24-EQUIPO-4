from flask import Flask, jsonify, request, Blueprint

from auth import AuthError, requires_role

import boto3

import os

blueprint = Blueprint('gastos', __name__, url_prefix='/')


dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


GASTO_COMBUSTIBLE = os.environ['GASTO_COMBUSTIBLE']

## Recibe Datos
@blueprint.route('/gastos')
def get_gastosc():
    gastos = dynamodb_client.scan(TableName = GASTO_COMBUSTIBLE)
    items = gastos['Items']
    response = jsonify(items)
    return response

## Crear gasto combustible
# @blueprint.route('/gastos', methods=['POST'])
# def create_gastosc():
#     folio = request.json.get('folio')
#     fechaEmision = request.json.get('fechaEmision')
#     horaEmision = request.json.get('horaEmision')
#     maquina = request.json.get('maquina')
#     montoTotal = request.json.get('montoTotal')
#     nombreEstacion = request.json.get('nombreEstacion')
#     qtyBencina = request.json.get('qtyBencina')
#     tipoComprobante = request.json.get('tipoComprobante')
# 
#     dynamodb_client.put_item(
#         TableName = OBRAS_TABLE,
#         Item ={
#             'folio': {'S': folio},
#             'fechaEmision': {'S': fechaEmision},
#             'horaEmision': {'S': horaEmision},
#             'maquina': {'S': maquina},
#             'montoTotal': {'S': montoTotal},
#             'nombreEstacion': {'S': nombreEstacion},
#             'qtyBencina': {'S': qtyBencina},
#             'tipoComprobante': {'S': tipoComprobante}
#         }
#     )

## Editar gasto combustible
@blueprint.route('/gastos', methods=['PUT'])
def edit_gastosc():
    folio = request.json.get('folio')
    fechaEmision = request.json.get('fechaEmision')
    horaEmision = request.json.get('horaEmision')
    maquina = request.json.get('maquina')
    montoTotal = request.json.get('montoTotal')
    nombreEstacion = request.json.get('nombreEstacion')
    qtyBencina = request.json.get('qtyBencina')
    tipoComprobante = request.json.get('tipoComprobante')

    key ={
        'folio':{'S': folio}
    }
    dynamodb_client.update_item(
        TableName = GASTO_COMBUSTIBLE,
        Key= key,
        ExpressionAttributeNames = {
            
            '#fechaE': 'fechaEmision',
            '#horaE': 'horaEmision',
            '#maq': 'maquina',
            '#montoT': 'montoTotal',
            '#estacion': 'nombreEstacion',
            '#qty': 'qtyBencina',
            '#tipo': 'tipoComprobante',
        
        },
        UpdateExpression= 
        "set #fechaE = :fechaEmision, #horaE = :horaEmision, #maq = :maquina, #montoT = :montoTotal, #estacion = :nombreEstacion, #qty = :qtyBencina, #tipo = :tipoComprobante "
        ,
        
        ExpressionAttributeValues={
            
            ':fechaEmision':{
                'S': fechaEmision
            },
             ':horaEmision':{
                'S': horaEmision
            },
             ':maquina':{
                'S': maquina
            },
             ':montoTotal':{
                'S': montoTotal
            },
             ':nombreEstacion':{
                'S': nombreEstacion
            },
             ':qtyBencina':{
                'S': qtyBencina
            },
             ':tipoComprobante':{
                'S': tipoComprobante
            }
        }
        
    )

@blueprint.route('/gastos/<string:folio>', methods=['DELETE'])
def delete_gastosc(folio):
    result = dynamodb_client.delete_item(
         TableName = GASTO_COMBUSTIBLE,
         Key = { 'folio': {'S': folio}}
    )
