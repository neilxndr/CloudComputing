import boto3
ec2 = boto3.client("ec2")
response = ec2.start_instances(InstanceIds=['i-0eee947e8d1db8c49'])
print("Success",response)