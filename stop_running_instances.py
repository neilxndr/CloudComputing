import boto3
ec2 = boto3.resource("ec2")
instances = ec2.instances.all()
for instance in instances:
	if instance.state["Name"] == "running":
		ec2 = boto3.client("ec2")
		response = ec2.stop_instances(InstanceIds=[instance.id],DryRun=False)
		print("Success",response)
	