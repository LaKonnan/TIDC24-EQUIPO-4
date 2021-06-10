import os
import boto3
from flask import Flask, jsonify, make_response, request
from dotenv import load_dotenv

load_dotenv('.env')
domain = os.getenv('AUTH0_DOMAIN')

## comentario de prueba W
app = Flask(__name__)


dynamodb_client = boto3.client('dynamodb')


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


OBRAS_TABLE = os.environ['OBRAS_TABLE']
CAJAS_TABLE = os.environ['CAJAS_TABLE']



@app.route('/obras/<string:obra_id>')
def get_obra(obra_id):
    result = dynamodb_client.get_item(
        TableName='obras-dev', Key={'obraId': {'S': obra_id}}
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


@app.route('/obras')
def get_obras():
    obras = dynamodb_client.scan(TableName='obras-dev')
    items = obras['Items']
    response = jsonify(domain)
    response.headers.add("Access-Control-Allow-Origin", "*")
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
    id_caja = request.json.get('id_caja')
    estado = request.json.get('estado')
    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')
    id_obra = request.json.get('id_obra')
    monto_gastos = request.json.get('monto_gastos')
    monto_total = request.json.get('monto_total')
    tipo = request.json.get('tipo')
    if not id_caja:
        return jsonify({'error': 'Por favor ingrese todos los campos obligatorios'}), 400

    dynamodb_client.put_item(
        TableName=CAJAS_TABLE,
        Item={
            'id_caja': {'S': id_caja},
            'estado': {'S': estado},
            'fecha_inicio': {'S': fecha_inicio},
            'fecha_termino': {'S': fecha_termino},
            'id_obra': {'S': id_obra},
            'monto_gastos': {'S': monto_gastos},
            'monto_total': {'S': monto_total},
            'tipo': {'S': tipo}
            }
    )

    return jsonify({
        'message': 'obra creada'
        })


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)