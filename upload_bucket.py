import boto3
s3 = boto3.client('s3')
local_file_path = 'C:/Users/neilx/Screenshot(126).png'
bucket_name = "sampletestbucket"
s3_object_key = 'Screenshot(126).png'
#response = s3.upload_file(local_file_path,bucket_name,s3_object_key)
#print(response)


#with open(local_file_path,"rb") as data:
#	response = s3.upload_fileobj(data,bucket_name,s3_object_key)
#print(response)

with open(local_file_path,'rb') as data:
	response = s3.put_object(Bucket = bucket_name,Key = s3_object_key, Body =data)
print(response)

