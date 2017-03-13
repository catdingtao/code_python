import boto3
#import json


ec2 = boto3.resource('ec2')

#instances = ec2.instances.filter(
#    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instances = ec2.instances.all()

for instance in instances:
    for instance_tags in instance.tags:
        if(instance_tags['Key']=='Name'):
            instance_tags_name=instance_tags['Value']
    print(instance.id,instance_tags_name,instance.state['Name'],instance.vpc_id)

#for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
#    print(json.dumps(status,indent=1)) 






