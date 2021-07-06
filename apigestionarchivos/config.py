import os

S3_BUCKET                 = 'imagenes-campodonico'
S3_KEY                    = 'AKIARXIKZW2WBU6Y244Q'
S3_SECRET                 = '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'
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000