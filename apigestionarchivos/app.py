from flask import Flask

from blueprints.basic_endpoints import blueprint as basic_endpoints

from blueprints.file_management import blueprint as file_management

from flask_cors import CORS


app = Flask(__name__)

app.config.from_object("config")

app.register_blueprint(basic_endpoints)

app.register_blueprint(file_management)

CORS(app)
