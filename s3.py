import boto3

def createbucket(username):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('mywebservicetest')
    directory_name = f'{username}/'
    bucket.put_object(Key=directory_name)


    