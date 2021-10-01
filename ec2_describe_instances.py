import boto3
import pprint
import json

pp = pprint.PrettyPrinter(indent=0)
ec2 = boto3.client('ec2')
response = ec2.describe_instances()

#json_object = json.dumps(response, indent = 4)
#with open("temp.txt","w") as file1:
#    file1.write(json_object)

a = response["Reservations"]
#print(a)

for b in a:
#    print(b)
    c = b["Instances"]
    for d in c:
        e = d["InstanceId"]
        print(f"Instance ID: {e}")

#b = a.get("Instances")

#for c in b:
#    print(c["InstanceId"])

#pp.pprint(response["Reservations"]["Instances"]["InstanceId"])



print(type(response))
