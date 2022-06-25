
#import resource
from urllib import response
from venv import create
import boto3
from pprint import pprint
#print(dir(boto3))

## HOW TO CREAT A SESSION WITH BOTO3
#boto3.session.Session(profile_name="")
#if you are using a default profile .keep the session parathesis empty
# session = boto3.session.Session()
# client = session.client(service_name='s3', region_name='us-east-1')

# resource = session.resource(service_name='s3', region_name = 'us-east-1')
#print(dir(session))

'''
#HOW TO CREAT A CLIENT OBJECT
client = session.client(service_name='s3', region_name='us-east-1')
#pprint(dir(client))
def list_buckets():
   response = client.list_buckets()['Buckets']
   for bucket in response:
       print(bucket.get('Name'))
   
list_buckets()


#CREAT REASOURCE OBJECT USING BOTO3

session.resource(region_name = 'us-east', service_name = 's3')

'''
# WE ARE WRINTING A FUNCTION THAT WOULD CREAT S3 BUCKET USING A CLIENT OBJECT AND RESOURCE OBJECT
'''
def create_bucket_client(bucket_name):
    """Using client object to creat an s3 bucket
    parameter : bucket_name
    return:
    None 
    """
    try:
        response = client.create_bucket(
        ACL='private',
        Bucket='bucket_name',
    )
        print(response)
    except Exception as e:
        print(e)
bucket_name = input("please enter bucket name: ")
create_bucket_client(bucket_name)

#WE ARE NOW CREATING CREATING A BUCKET USING RESOURCE OBJECT
def create_bucket_resource(bucket_name):
    """Using client object to creat an s3 bucket
    parameter : bucket_name
    return:
    None 
    """
    response = response.create_bucket(
        bucket = bucket_name 
    )
    print(response)
    
create_bucket_resource("love.python.bkcets")
'''
'''
#HOW TO DELETE BUCKET
def client_delete_bucket(bucket_name):
    """Using client object to creat an s3 bucket
    parameter : bucket_name
    return:
    None 
    """
    try:
       bucket_name = client.delete_bucket(
       Bucket=bucket_name
    )
    except Exception as e:
        print(bucket_name) 

    
client_delete_bucket()
'''

"""Using resource object to list all s3 buckets.
"""
'''
def list_bucketWithResource():
    """List all buckets using resource object
    Parameter: None
    Reture: None
    """
    try:
        buckets = resource.bucket.all()
        for bucket in buckets:
            print(bucket.name)
        
    except Exception as err:
        print(err)
    #return: None
        
list_bucketWithResource()  
    
'''
session = boto3.session.Session()
client = session.client(service_name='ec2', region_name='us-east-1')

resource = session.resource(service_name='ec2', region_name = 'us-east-1')

def ec2service():
    pprint(session.region_name)
    
    
ec2service()