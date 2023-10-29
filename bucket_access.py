import boto3
s3=boto3.client('s3')
response = s3.list_buckets()
for bucket in response['Buckets']:
	print(f'{bucket["Name"]}')

buk = s31.bucket('napbucket1')
for obj in buk.objects.all():
	print(obj.key)

with open("start_instance.py","rb") as f:
	s3.upload_fileobj(f,"napbucket1","example.html")
print("The file is uploaded")