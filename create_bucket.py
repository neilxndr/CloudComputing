import boto3
s3 = boto3.resource('s3')
bucket_name = "sampletestbucket"
response = s3.create_bucket(Bucket = bucket_name)
print(response)