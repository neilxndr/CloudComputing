import logging
import boto3
from botocore.exceptions import ClientError
import os
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

#response = [bucket['Name'] for bucket in response['Buckets']]
#print("Bucket List: %s" % buckets)

bucket = s3_resource.Bucket('demo-bucket-69420')
buk = 'demo-bucket-69420'
# for obj in buk.objects.all():
# print(obj.key)

response = s3_client.delete_object(Bucket=buk, Key='hello.txt')
print(response)

print('Object Deleted')