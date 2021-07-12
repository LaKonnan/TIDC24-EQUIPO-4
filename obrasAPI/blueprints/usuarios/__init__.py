from flask import Flask, jsonify, request, Blueprint

import os

from auth import AuthError, requires_role

from dotenv import load_dotenv

from auth0.v3.authentication import GetToken

from auth0.v3.management import Auth0

# Conexión a la api de gestión de Auth0
load_dotenv('.env')
domain = os.getenv('AUTH0_DOMAIN')
non_interactive_client_id = os.getenv('CLIENT_ID')
non_interactive_client_secret = os.getenv('CLIENT_SECRET')
get_token = GetToken(domain)
token = get_token.client_credentials(non_interactive_client_id,
    non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']
auth0 = Auth0(domain, mgmt_api_token)


blueprint = Blueprint('usuarios', __name__, url_prefix='/')


# Ruta para obtener todos los usuarios 
@blueprint.route('/usuarios')
@requires_role('manage:users')
def get_usuarios():
    items = auth0.users.list()
    response = jsonify(items["users"])
    return response

# Ruta para crear un usuario
@blueprint.route('/usuarios', methods=['POST'])
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

# Ruta para editar un usuario
@blueprint.route('/usuarios/<string:user_id>', methods=['PUT'])
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

# Ruta para eliminar un usuario
@blueprint.route('/usuarios/<string:user_id>', methods=['DELETE'])
@requires_role('manage:users')
def delete_usuarios(user_id):
    auth0.users.delete(user_id)
    return jsonify({'message': 'usuario eliminado'})

# Ruta para obtener el rol de un usuario
@blueprint.route('/rol/<string:user_id>')
def get_rol(user_id):
    rol = auth0.users.list_roles(user_id)
    return jsonify(rol)

