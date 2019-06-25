import pytest
import boto3
import boto3.session
from s3utils import *

access_key = '0579B3K2ZKALP5KEI081'
secret_key = 'rYmqDUvO9EBX3vMr8bxxRsKf2QnNsr4lCmsAeUJ6'

session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        )

bucket_name="my-new-bucket"


@pytest.fixture
def resource():
    return session.resource(
        service_name='s3',
        endpoint_url = 'http://136.156.133.10:80',)
