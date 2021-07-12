from flask import Flask, jsonify, request, Blueprint, make_response,current_app

from helpers import *

from werkzeug.utils import secure_filename


blueprint = Blueprint('file_api', __name__, url_prefix='/')


ALLOWED_EXTENSIONS = {'pdf'}

@blueprint.route("/upload", methods=["POST"])
def upload_file():

	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file    = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output   	  = upload_file_to_s3(file, current_app.config["S3_BUCKET"])
        return str(output)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:

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

    return "{}{}".format(current_app.config["S3_LOCATION"], file.filename)
    

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
