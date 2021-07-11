import os
from re import I
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
GASTO_COMBUSTIBLE = os.environ['GASTO_COMBUSTIBLE']

@app.route('/obras/<string:obraId>')
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

@app.route('/obra/tipos/<string:tipo>')
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



@app.route('/obras')
@requires_role('manage:obras')
def get_obras():
    obras = dynamodb_client.scan(TableName = 'obras-dev')
    items = obras['Items']
    response = jsonify(items)
    return response


@app.route('/obras', methods=['POST'])
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

@app.route('/obras', methods=['PUT'])
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

@app.route('/obras/<string:obraId>', methods=['DELETE'])
@requires_role('manage:obras')
def delete_obra(obraId):
    result = dynamodb_client.delete_item(
         TableName = OBRAS_TABLE,
         Key = { 'obraId': {'S': obraId}}
    )
    return jsonify({'msg':'eliminado'})
   
## ------------ GESTIÓN DE GASTOS
## Recibe Datos
@app.route('/gastos')
def get_gastosc():
    gastos = dynamodb_client.scan(TableName = GASTO_COMBUSTIBLE)
    items = gastos['Items']
    response = jsonify(items)
    return response

## Crear gasto combustible
@app.route('/gastos', methods=['POST'])
def create_gastosc():
    folio = request.json.get('folio')
    fechaEmision = request.json.get('fechaEmision')
    horaEmision = request.json.get('horaEmision')
    maquina = request.json.get('maquina')
    montoTotal = request.json.get('montoTotal')
    nombreEstacion = request.json.get('nombreEstacion')
    qtyBencina = request.json.get('qtyBencina')
    tipoComprobante = request.json.get('tipoComprobante')

    dynamodb_client.put_item(
        TableName = OBRAS_TABLE,
        Item ={
            'folio': {'S': folio},
            'fechaEmision': {'S': fechaEmision},
            'horaEmision': {'S': horaEmision},
            'maquina': {'S': maquina},
            'montoTotal': {'S': montoTotal},
            'nombreEstacion': {'S': nombreEstacion},
            'qtyBencina': {'S': qtyBencina},
            'tipoComprobante': {'S': tipoComprobante}
        }
    )

## Editar gasto combustible
@app.route('/gastos', methods=['PUT'])
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

@app.route('/gastos/<string:folio>', methods=['DELETE'])
def delete_gastosc(folio):
    result = dynamodb_client.delete_item(
         TableName = GASTO_COMBUSTIBLE,
         Key = { 'folio': {'S': folio}}
    )

## ----------------------------------------------------------------------------------------------- GESTIÓN DE CAJAS COMBUSTIBLE
@app.route('/cajasChicas/combustible')
def get_cajaCombustible():
    cajas = dynamodb_client.scan(TableName=CAJAS_TABLE)
    items = cajas['Items']
    response = jsonify(items)
    return response


## ----------------------------------------------------------------------------------------------- GESTIÓN DE CAJAS CHICAS
@app.route('/cajasChicas')
def get_cajas():
    cajas = dynamodb_client.scan(TableName=CAJAS_TABLE)
    items = cajas['Items']
    response = jsonify(items)
    return response

@app.route('/cajasChicas/<string:id_caja1>')
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

@app.route('/cajasChicas', methods=['POST'])
def create_caja():
    try:
        ## RECIBIR DATOS
        id_obra = request.json.get('id_obra')
        tipo = request.json.get('tipo')
        estado = request.json.get('estado')
        fecha_inicio = request.json.get('fecha_inicio')
        fecha_termino = request.json.get('fecha_termino')
        monto_total = request.json.get('monto_total')
        monto_combustible = request.json.get('monto_combustible')

        # verificar que la obra se encuentre no se encuentre finalizada
        data = dynamodb_client.scan(
            TableName = CAJAS_TABLE,
            ScanFilter = { 
                "obraId": { 
                    "ComparisonOperator": "EQ", 
                    "AttributeValueList": [{ "S": id_obra } ]
                } 
            }
        )

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
    except:
        return jsonify({'message': 'OCURRIÓ UN ERROR:' })

@app.route('/cajasChicas/<string:id_caja>', methods=['DELETE'])
@requires_auth
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


## GESTION DE USUARIOS


@app.route('/usuarios')
@requires_role('manage:users')
def get_usuarios():
    items = auth0.users.list()
    response = jsonify(items["users"])
    return response


@app.route('/usuarios', methods=['POST'])
@requires_role('manage:users')
def create_usuario():
    rut = request.json.get('rut')
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    rol = request.json.get('idRol')
    user_metadata = {'rol': request.json.get('rol')}
    if not rut and name and email and password and rol:
        return jsonify({'error': 'Por favor ingrese todos los campos obligatorios'}), 400 
    auth0.users.create({
        'user_id': rut,
        'name': name,
        'email': email,
        'password': password,
        'user_metadata': user_metadata,
        'connection': 'Username-Password-Authentication'
    })
    auth0.users.add_roles('auth0|'+rut, [rol])
    return jsonify({'message': 'usuario creado'})


@app.route('/usuarios/<string:user_id>', methods=['PUT'])
@requires_role('manage:users')
def edit_usuario(user_id):
    email = request.json.get('email')
    name = request.json.get('name')
    password = request.json.get('password')
    if not email:
        return jsonify({'error': 'Por favor ingrese todos los campos obligatorios'}), 400 
    auth0.users.update(user_id, {
        'email': email,
        'name': name
    })
    auth0.users.update(user_id, {
        'password': password
    })
    return jsonify({'message': 'usuario modificado'})


@app.route('/usuarios/<string:user_id>', methods=['DELETE'])
@requires_role('manage:users')
def delete_usuarios(user_id):
    auth0.users.delete(user_id)
    return jsonify({'message': 'usuario eliminado'})


@app.route('/rol/<string:user_id>')
def get_rol(user_id):
    rol = auth0.users.list_roles(user_id)
    return jsonify(rol)


## FIN GESTION DE USUARIOS


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response