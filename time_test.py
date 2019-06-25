
import time
import boto
import boto3.session
from s3utils import *

if __name__ == "__main__":
    access_key = '0579B3K2ZKALP5KEI081'
    secret_key = 'rYmqDUvO9EBX3vMr8bxxRsKf2QnNsr4lCmsAeUJ6'

    session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            )

    bucket_name="my-new-bucket"
    resource= session.resource(
            service_name='s3',
            endpoint_url = 'http://136.156.133.10:80',)

    create_bucket(resource,"testbucket")
    locations = [("s3://testbucket/test1","./big-file",0,104857600)]
    put_objects(resource, locations)

    locations = [("s3://testbucket/test2","./big-file",0,52428800),
            ("s3://testbucket/test3","./big-file",52428800,52428800)]
    put_objects(resource, locations)
    locations = [("s3://testbucket/test4","./big-file",0,26214400),
            ("s3://testbucket/test5","./big-file",26214400,26214400),
            ("s3://testbucket/test6","./big-file",52428800,26214400),
            ("s3://testbucket/test7","./big-file",78643200,26214400)]
    put_objects(resource, locations)
