from flask import Flask, jsonify, request, Blueprint

from botocore.exceptions import DataNotFoundError

from re import I

from auth import AuthError, requires_role

import boto3

import os

blueprint = Blueprint('cajas_chicas', __name__, url_prefix='/')


dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


CAJAS_TABLE = os.environ['CAJAS_TABLE']
CAJAS_COMBUSTIBLE = os.environ['CAJAS_COMBUSTIBLE']


@blueprint.route('/cajasChicas')
def get_cajas():
    cajas = dynamodb_client.scan(TableName=CAJAS_TABLE)
    items = cajas['Items']
    response = jsonify(items)
    return response

@blueprint.route('/cajasChicas/<string:id_caja1>')
def get_caja(id_caja1):
    result = dynamodb_client.scan(
        TableName = CAJAS_TABLE,
        ScanFilter = {
            "id_caja": {
                "ComparisonOperator": "EQ",
                "AttributeValueList": [{ "S": id_caja1 }]
            }
        }
    )

    items = result['Items']
    if not items:
        return jsonify({ 'error':'No se han encontrado' }), 404
    
    response = jsonify(items)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@blueprint.route('/cajasChicas', methods=['POST'])
def create_caja():
        ## RECIBIR DATOS
        id_obra = request.json.get('id_obra')
        tipo = request.json.get('tipo')
        estado = request.json.get('estado')
        fecha_inicio = request.json.get('fecha_inicio')
        fecha_termino = request.json.get('fecha_termino')
        monto_total = request.json.get('monto_total')
        monto_combustible = request.json.get('monto_combustible')
        
        print("REGISTRAR NUEVA CAJA")

        ## GENERAR IDs
        # identificador de tipo
        id_caja = ''
        if(tipo == 'Gerencia'):
            id_caja = 'G'

        elif(tipo == 'Oficina'):
            id_caja = 'OF'

        elif(tipo == 'Obra'):
            id_caja = 'O'
        
        id_caja = id_caja + id_obra + '-'
        id_caja_combustible = 'C' + id_obra + '-'

        # dar version de caja (O1, 02, 03...0N)
        result = dynamodb_client.scan(
            TableName = CAJAS_TABLE,
            ScanFilter = { 
                "id_obra": { 
                    "ComparisonOperator": "EQ" , 
                    "AttributeValueList": [ { "N": id_obra } ]
                } 
            }
        )

        items = result['Items']

        if not items:
            # la obra no posee ninguna caja
            id_caja += '01'
            id_caja_combustible += '01'

        # la obra posee caja(s) chica(s)
        else:
            # ordenar diccionario de cajas con metodo burbuja
            size = len(items)

            for i in range(size):
                min_i = i

                for x in range(i+1, size):
                    if items[min_i]["id_caja"]['S'] > items[x]["id_caja"]['S']:
                        min_i = x 
                
                temp = items[i]
                items[i] =  items[min_i]
                items[min_i] = temp
            
            # obtener última caja
            last = items[size-1]['id_caja']['S']

            # verificar que ultima caja este cerrada
            if(items[size-1]['estado']['S'] == 'Activa'):
                return jsonify({'message': 'activa'})

            elif(items[size-1]['estado']['S'] == 'Inactiva'):
                return jsonify({'message': 'inactiva'})

            else:
                temp_id = ''
                # obtener numero de ultima version
                size_id = len(last)
                for x in range (size_id):
                    if(x == size_id-2 | x == size_id-1):
                        if (int(temp_id) > int(last[size_id-1]) & temp_id !=  ''):
                            temp_id = temp_id + str(int(last[x]) + 1)
                        else:    
                            temp_id += last[x]
                
                id_caja += temp_id
                id_caja_combustible += temp_id
            

        ## REGISTRAR NUEVA CAJA CHICA
        dynamodb_client.put_item(
            TableName = CAJAS_TABLE,
            Item = {
                'id_caja': {'S': id_caja},
                'estado': {'S': estado},
                'fecha_inicio': {'S': fecha_inicio},
                'fecha_termino': {'S': fecha_termino},
                'id_obra': {'N': id_obra},
                'monto_gastos': {'S': '0'},
                'monto_total': {'S': monto_total},
                'tipo': {'S': tipo}
            }
        )

        ## REGISTRAR NUEVA CAJA COMBUSTIBLE ASOCIADA
        dynamodb_client.put_item(
            TableName = CAJAS_COMBUSTIBLE,
            Item = {
                'id_caja_asociada': {'S': id_caja},
                'id_caja_combustible': {'S': id_caja_combustible},
                'monto_maximo': {'S': monto_combustible },
                'monto_gastos': {'S': '0'}
            }
        )

        return jsonify({'message': 'creada', "id_caja": id_caja })

@blueprint.route('/cajasChicas/<string:id_caja>', methods=['DELETE'])
def delete_caja(id_caja):
    # eliminar caja chica
    result1 = dynamodb_client.delete_item(
        TableName = CAJAS_TABLE,
        Key = {
            'id_caja': {'S': id_caja }
        }
    )

    # eliminar caja combustible asociada
    result2 = dynamodb_client.delete_item(
        TableName = CAJAS_COMBUSTIBLE,
        Key = {
            'id_caja_asociada': {'S': id_caja }
        }
    )


@blueprint.route('/cajaChica/<string:id_caja>', methods=['PUT'])
def update_caja():
    ## RECIBIR DATOS
    id_caja = request.json.get('id_caja')
    estado = request.json.get('estado')
    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')
    monto_total = request.json.get('monto_total')
    monto_combustible = request.json.get('maximo_caja_combustible')

    key = {
        'id_caja': {'S': id_caja}
    }

    # actualizar caja chica
    dynamodb_client.update_item(
        TableName = CAJAS_TABLE,
        key = key,

        ExpressionAttributeNames = {
            '#estado': 'estado',
            '#fechaI': 'fecha_inicio',
            '#fechaF': 'fecha_final',
            '#monto': 'monto_total'
        },

        UpdateExpression = "set #estado = :estado, #fechaI = :fecha_inicio, #fechaT = :fecha_inicio, #fechaF = :fecha_final, #monto = :monto_total"
        ,

        ExpressionAttributeValues = {
            ':estado': {
                'S': estado
            },
            ':fecha_inicio': {
                'S': fecha_inicio
            },
            ':fecha_final': {
                'S': fecha_termino
            },
            ':monto_total': {
                'S': monto_total
            }
        }
    )
    
    key = {
        'id_caja_asociada': {'S': id_caja}
    }

    # actualizar caja combustible
    dynamodb_client.update_item (
        TableName = CAJAS_COMBUSTIBLE,
        key =  key,
        ExpressionAttributeNames = {
            '#monto': 'monto_total'
        },
        UpdateExpression= 
        "set #monto = :monto_total"
        ,
        ExpressionAttributeValues = {
            ':monto_total': {
                'S': monto_combustible
            }
        }

    )