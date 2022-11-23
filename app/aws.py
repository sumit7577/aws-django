import boto3
ec2 = boto3.resource('ec2')


def creatInstance():
    instances = ec2.create_instances(
        ImageId="ami-072bfb8ae2c884cc4",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="sumit"
    )
    print(instances)
    return instances

