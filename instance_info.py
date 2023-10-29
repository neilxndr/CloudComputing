#Example to AWS EC2 using academy credentials
import boto3

ec2=boto3.resource('ec2')
instances=ec2.instances.all()

for instance in instances:
    print(f'EC2 instance {instance.id} information:')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance AMI: {instance.image.id}')
    print(f'Instance Platform: {instance.platform}')
    print(f'Instance Type: {instance.instance_type}')
    print(f'Public IPv4 address: {instance.public_ip_address}')
    print('-'*60)