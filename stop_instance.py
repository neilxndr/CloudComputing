import boto3
ec2 = boto3.client('ec2')
response = ec2.stop_instances(InstanceIds=['i-0eee947e8d1db8c49'],DryRun = False)
print("Success",response)