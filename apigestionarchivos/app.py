from flask import Flask

# Blueprints import
from blueprints.basic_endpoints import blueprint as basic_endpoints

from blueprints.file_management import blueprint as file_management

# Import de Recursos de Origen Cruzado (CORS) para proteger peticiones HTTP
from flask_cors import CORS

# Inicio de instancia de Flask
app = Flask(__name__)

# Configuración de la instancia de Flask desde config.py
app.config.from_object("config")

# Registro de blueprints en la app
# endpoints de prueba ej:"Hello World"
app.register_blueprint(basic_endpoints)

# endpoint de gestion del archivo de reglamento en AWS S3
app.register_blueprint(file_management)

# Aplicar CORS en la API
CORS(app)
