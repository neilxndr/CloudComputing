import logging
import boto3
from botocore.exceptions import ClientError
import os

s31 = boto3.resource('s3') # for viewing resources
s3 = boto3.client('s3')  # for operations on bucket
##response = s3.list_buckets()
##buckets = [bucket['Name'] for bucket in response['Buckets']]
##print("Bucket List : %s" % buckets)

buk = s31.Bucket('napbucket2')
for obj in buk.objects.all():
	print(obj.key)

with open("Neil Alexander Perira Resume.pdf", "rb") as f:
	s3.upload_fileobj(f, "napbucket2", "Neil Alexander Perira Resume.pdf")
print("The file is uploaded")