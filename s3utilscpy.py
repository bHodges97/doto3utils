import threading
import time
import sys
import os

def parse_url(obj_url):
    obj_url = obj_url[5:]
    return obj_url.split('/',1)

def list_objects(resource,bucket_name):
    try:
        bucket = resource.Bucket(bucket_name)
        return [key.key for key in bucket.objects.all()]
    except resource.meta.client.exceptions.NoSuchBucket:
        print("No such bucket")
        return []

def delete_object(resource,obj_url):
    bucket_name,key_name = parse_url(obj_url)
    obj = resource.Object(bucket_name,key_name)
    obj.delete()

def create_bucket(resource,bucket_name):
    resource.create_bucket(Bucket=bucket_name)

def create_obj(resource,bucket_name,object_name,object_content):
    try:
        bucket = resource.Bucket(bucket_name)
    except resource.meta.client.exceptions.NoSuchBucket:
        print("No such bucket")
    resource.Object(bucket_name, object_name).put(Body=object_content)

def put_object(resource,location,blocksize=10485760):
    url,local_path,offset,length = location
    bucket_name,object_name = parse_url(url)
    with open(local_path,"br") as f:
        f.seek(offset)
        if length < blocksize:
            content = f.read(length)
        else:
            content = bytearray()
            for i in range(blocksize,length,blocksize):
                content.extend(f.read(blocksize))
            i = len(content)
            if i < length:
                content.extend(f.read(length-i))
        #obj = resource.Object(bucket_name, object_name)
        #obj.put(Body=content)
        #assert obj.content_length == length , "File upload incomplete!"
        del content


def put_objects(resource,locations):
    for location in locations:
        #put_object(resource,location)
        t = threading.Thread(target = put_object, args=(resource,location)).start()
