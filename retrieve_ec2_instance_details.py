import boto3

# Specify your AWS access key ID and secret access key
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'

# Specify your AWS session token (if you have one)
aws_session_token = 'your_session_token'

# Specify the region you want to interact with
region_name = 'us-east-1'

# Create a connection to the EC2 service using your credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region_name
)

# Use the session to interact with AWS resources (e.g. EC2 instances)
ec2 = session.resource('ec2')

# Example usage: get details of all EC2 instances in the region
for instance in ec2.instances.all():
    instance_id = instance.id
    status = instance.state['Name']
    region = region_name

    # Print the instance ID, status, and region
    print(f"Instance ID: {instance_id}, Status: {status}, Region: {region}")
