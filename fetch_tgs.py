import boto3

i = j = k = 0
TG_CLIENT = boto3.client('elbv2')
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
EC2_CLIENT = boto3.client('ec2')

tgs = TG_CLIENT.describe_target_groups()['TargetGroups']

for tg in tgs:
    i+=1
    print('{}. {}'.format(i, tg['TargetGroupName']))
   
alarms_metdata = CLOUDWATCH_CLIENT.describe_alarms(MaxRecords=100)
alarms = alarms_metdata['MetricAlarms']
next_token = alarms_metdata['NextToken']
while bool(next_token):
    alarms_metdata = CLOUDWATCH_CLIENT.describe_alarms(MaxRecords=100, NextToken=next_token)
    alarms_limited = alarms_metdata['MetricAlarms']
    try:
        next_token = alarms_metdata['NextToken']
    except KeyError:
        next_token = False
    alarms = alarms + alarms_limited

for alarm in alarms:
    j+=1
    print('{}. {}'.format(j, alarm['AlarmName']))

ec2_metadatas = EC2_CLIENT.describe_instances()['Reservations']

for ec2_metadata in ec2_metadatas:
    instances = ec2_metadata['Instances']
    for instance in instances:
        k+=1
        print('{}. {}'.format(k, instance['InstanceId']))

