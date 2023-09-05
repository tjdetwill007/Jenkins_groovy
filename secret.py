import boto3
import json
import mysql.connector
#Using secret manager for credentials.

def get_secret():

    secret_name = "test/mydb/access"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except Exception as e:
       print("error:",e,"help me")

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    sec=json.loads(secret)
    return sec





    # Your code goes here.