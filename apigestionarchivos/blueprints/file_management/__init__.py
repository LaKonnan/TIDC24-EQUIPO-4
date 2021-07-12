from flask import Flask, jsonify, request, Blueprint, make_response,current_app

from helpers import *

from werkzeug.utils import secure_filename

# Definicion del blueprint donde el 1er arg corresponde al nombre del blueprint y url_prefix corresponde a la url de llamada
blueprint = Blueprint('file_api', __name__, url_prefix='/')

# Definición de extensión de archivos permitida
ALLOWED_EXTENSIONS = {'pdf'}
"""
    Las extensiones disponibles son:
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'

"""

# Ruta para subir el archivo reglamento.pdf al bucket S3 en AWS
@blueprint.route("/upload", methods=["POST"])
def upload_file():

	# Comprobación del campo user_file que contiene el archivo reglamento.pdf en la solicitud
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# Asiganción del archivo capturado a una variable para su mejor manejo
    file    = request.files["user_file"]

    """
        Estos atributos también estan disponibles

        file.filename
        file.content_type
        file.content_length
        file.mimetype

    """

	# Verificación del archivo capturado
    if file.filename == "":
        return "Por favor seleccione un archivo"

	# Subida del archivo al bucket S3 en AWS
    if file and allowed_file(file.filename):

        """
         Verificar el nombre del archivo para evitar modificaciones a otros archivos del bucket. Información adicional: https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
         
        """
        file.filename = secure_filename(file.filename)

        # Subir el archivo con la función "upload_file_to_s3"
        output   	  = upload_file_to_s3(file, current_app.config["S3_BUCKET"])

        return str(output)

# Función para subir el archivo pdf al bucket S3
def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Documentación oficial adicional: http://boto3.readthedocs.io/en/latest/guide/s3.html

    """

    try:
        # Subida del archivo 
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    # Retorna la url en donde se subió el archivo
    return "{}{}".format(current_app.config["S3_LOCATION"], file.filename)
    
# Función para leer los archivos permitidos
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Manejo de errores
@blueprint.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
