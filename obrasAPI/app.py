import os
import boto3
import json
from botocore.exceptions import DataNotFoundError
from flask import Flask, jsonify, make_response, request
from dotenv import load_dotenv
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
from auth import AuthError, requires_auth, requires_role
from flask_cors import CORS


##CONFIG AUTH0
load_dotenv('.env')
domain = os.getenv('AUTH0_DOMAIN')
non_interactive_client_id = os.getenv('CLIENT_ID')
non_interactive_client_secret = os.getenv('CLIENT_SECRET')
get_token = GetToken(domain)
token = get_token.client_credentials(non_interactive_client_id,
    non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']
auth0 = Auth0(domain, mgmt_api_token)


app = Flask(__name__)
CORS(app)

dynamodb_client = boto3.client('dynamodb', region_name='us-east-2')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


OBRAS_TABLE = os.environ['OBRAS_TABLE']
CAJAS_TABLE = os.environ['CAJAS_TABLE']
CAJAS_COMBUSTIBLE = os.environ['CAJAS_COMBUSTIBLE']


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
            'estado': item.get('estado').get('S'),
            'tipo': item.get('tipo').get('S')
        }
    )

@app.route('/obra/tipos/<string:tipo>')
def obras_por_tipo(tipo):
    result = dynamodb_client.scan(
        TableName = OBRAS_TABLE,
        ScanFilter = { "tipo": { "ComparisonOperator": "EQ", "AttributeValueList": [{ "S": tipo } ]} }
    )

    items = result['Items']
    if not items:
        return jsonify({ 'error':'No se han encontrado' }), 404
    response = jsonify(items)

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



@app.route('/obras')
def get_obras():
    obras = dynamodb_client.scan(TableName='obras-dev')
    items = obras['Items']
    response = jsonify(items)
    return response



@app.route('/obras', methods=['POST'])
def create_obra():
    obra_id = request.json.get('obraId')
    nombre = request.json.get('nombre')
    encargado = request.json.get('encargado')
    estado = request.json.get('estado')
    tipo = request.json.get('tipo')
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
            'estado': {'S': estado},
            'tipo': {'S': tipo}
        }
    )

    return jsonify({
        'message': 'obra creada',
        'Obra': {
            'obraId': obra_id,
            'nombre': nombre,
            'encargado': encargado,
            'estado': estado,
            'tipo' : tipo,
            }
        })

## ----------------------------------------------------------------------------------------------- GESTIÓN DE CAJAS CHICAS
@app.route('/cajasChicas')
def get_cajas():
    obras = dynamodb_client.scan(TableName=CAJAS_TABLE)
    items = obras['Items']
    response = jsonify(items)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/cajasChicas', methods=['POST'])
def create_caja():
    ## RECIBIR DATOS
    id_obra = request.json.get('id_obra')
    tipo = request.json.get('tipo')
    estado = request.json.get('estado')
    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')
    monto_total = request.json.get('monto_total')
    monto_combustible = request.json.get('monto_combustible')


    ## VALIDACIONES

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
        ScanFilter = { "obraId": { "ComparisonOperator": "CONTAINS", "AttributeValueList": [{ "S": id_obra } ]} }
    )

    items = result['Items']

    if not items:
        id_caja += '01'
        id_caja_combustible += '01'
    else:
        # ordenar lista
        print('aaa')
        # tomar ultimos dos valores del ultimo id


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

    return jsonify({
        'message': 'Caja chica creada'
    })


## GESTION DE USUARIOS
@app.route('/usuarios')
@requires_role('manage:users')
##@requires_auth
def get_auth():
    items = auth0.users.list()
    response = jsonify(items["users"])
    return response

## FIN GESTION DE USUARIOS


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response