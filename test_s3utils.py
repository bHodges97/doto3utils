import pytest
import boto3
import boto3.session
from s3utils import *

bucket_name="my-new-bucket"


def test_list_objects(resource) :
    out = list_objects(resource,bucket_name)
    assert out == []
    create_obj(resource,bucket_name,"test_1","test_1 contents");
    out = list_objects(resource,bucket_name)
    assert len(out) == 1 and out[0] == "test_1"



def test_delete_object(resource):
    delete_object(resource,"s3://my-new-bucket/test_1")
    out = list_objects(resource,bucket_name)
    assert out == []

def test_put_objects(resource):
    create_bucket(resource,"testbucket")
    locations = [("s3://testbucket/test1","./big-file",0,2048000),
            ("s3://testbucket/test2","./big-file",64, 2102000 ),
            ("s3://testbucket/test3","./big-file",64, 2102000)]
    put_objects(resource, locations)
    assert all(x in list_objects(resource,"testbucket") for x in ["test1","test2","test3"])


