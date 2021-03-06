import boto3, botocore

from config import S3_KEY, S3_SECRET, S3_BUCKET

# Conexión al bucket AWS S3 con la librería boto3
s3 = boto3.client(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)