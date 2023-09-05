import boto3
import requests

bucket_name = 'testbucket1sept2023'
s3 = boto3.client('s3', region_name="us-east-1")
with open("artifact/artifact.zip",'rb') as file_name:
    data=file_name.read()
    presigned_url = s3.generate_presigned_url(
    ClientMethod='put_object',
    Params={
        'Bucket': bucket_name,
        'Key': "artifact.zip",
    },
    ExpiresIn=3600)
    print(presigned_url)
    response = requests.put(presigned_url, data=data)
