import os

# Configuración de variables de AWS privadas
S3_BUCKET                 = 'imagenes-campodonico'
S3_KEY                    = 'AKIARXIKZW2WBU6Y244Q'
S3_SECRET                 = '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'
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
SECRET_KEY                = os.urandom(32)

# Setting de la opción de DEBUG y el puerto en que se ejecuta la API
DEBUG                     = True
PORT                      = 5000