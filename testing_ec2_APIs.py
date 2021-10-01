import boto3
import argparse
import logging
import pprint

#logging.getLogger().setLevel(logging.INFO)


def _genarate_clients(profile):

    global TG_CLIENT
    global EC2_CLIENT
    global CLOUDWATCH_CLIENT

    SESSION = boto3.Session(profile_name=profile)
    TG_CLIENT = SESSION.client("elbv2", region_name="ap-southeast-1")
    EC2_CLIENT = SESSION.client("ec2", region_name="ap-southeast-1")

def _create_tg_unhealthy_host_count_alarms():
    tgs = TG_CLIENT.describe_target_groups()['TargetGroups']
    print("Fetching Target groups....{tgs}".format(tgs=tgs))
    ec2s = EC2_CLIENT.describe_instances()['Reservations']
    print("Fetching EC2 Instances....{ec2s}".format(ec2s=ec2s))

    for tg in tgs:
        tg_name = tg['TargetGroupName']
        print("Scanning {tg_name} TG....".format(tg_name=tg_name))

    for ec2 in ec2s:
        ec2_is = ec2['Instances']
        for ec2_i in ec2_is:
            ec2_id = ec2_i['InstanceId']
            print('Scanning {ec2_id} ....'.format(ec2_id=ec2_id))

if __name__ == "__main__":
    
    _genarate_clients("default")
    _create_tg_unhealthy_host_count_alarms()
