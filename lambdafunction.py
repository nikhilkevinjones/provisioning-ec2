import boto3

AMI = 'ami-00ca32bbc84273381' # Take the latest from EC2 -> Images-> AMIs
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'ec2inst_SNOW' # Enter Key pair created
REGION = 'us-east-1'
SUBNET_ID = 'subnet-0c641febbc4766444'  #  Replace with your actual subnet ID
SECURITY_GROUP_ID = 'sg-0b746e5d687f3f769' # From VPC you get sec group

ec2 = boto3.client('ec2', region_name=REGION)


def lambda_handler(event, context):

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        SecurityGroupIds=[SECURITY_GROUP_ID],
        MaxCount=1,
        MinCount=1
    )
    
    print ("New instance created:")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)

    return instance_id
    
