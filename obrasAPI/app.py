from flask import Flask, jsonify, make_response

# import errores de auth0
from auth import AuthError

# Blueprints import
from blueprints.obras import blueprint as obras
from blueprints.gastos import blueprint as gastos
from blueprints.cajas_combustible import blueprint as cajas_combustible
from blueprints.cajas_chicas import blueprint as cajas_chicas
from blueprints.usuarios import blueprint as usuarios

# Import de Recursos de Origen Cruzado (CORS) para proteger peticiones HTTP
from flask_cors import CORS

# Inicio de instancia de Flask
app = Flask(__name__)

# Registro de blueprints en la app
# Gestión de Obras
app.register_blueprint(obras)

# Gestión de Gastos
app.register_blueprint(gastos)

# Gestión de Cajas combustible
app.register_blueprint(cajas_combustible)

# Gestión de Cajas chicas
app.register_blueprint(cajas_chicas)

# Gestión de Usuarios de auth0
app.register_blueprint(usuarios)

# Aplicar CORS en la API
CORS(app)

# Capturar el error de no encontar alguna ruta
@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

# Capturar un error de Auth0
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response